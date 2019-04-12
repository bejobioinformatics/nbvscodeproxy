# vim: set et sw=4 ts=4:
import os
import getpass
import pwd
import tempfile

from urllib.parse import urlunparse, urlparse

from tornado import web

from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler

from nbserverproxy.handlers import SuperviseAndProxyHandler


class AddSlashHandler(IPythonHandler):
    """Handler for adding trailing slash to URLs that need them"""
    @web.authenticated
    def get(self, *args):
        src = urlparse(self.request.uri)
        dest = src._replace(path=src.path + '/')
        self.redirect(urlunparse(dest))


class VSCodeProxyHandler(SuperviseAndProxyHandler):
    '''Manage an VSCode rsession instance.'''

    name = 'vscode'

    def get_env(self):
        env = {}

        # vscode needs USER to be set to something sensible,
        # otherwise it'll throw up an authentication page
        if not os.environ.get('USER', ''):
            env['USER'] = getpass.getuser()

        return env

    def get_cmd(self):
        # vscode command. Augmented with user-identity and www-port.
        basedir = env['NOTEBOOK_DIR']
        configdir = os.path.join(basedir, ".vscode")
        return [
            'code-server',
            '--allow-http',
            '--no-auth',
            '--host=0.0.0.0',
            '--port=' + str(self.port),
            '--user-data-dir=' + os.path.join(configdir, "user_data"),
            '--extensions-dir=' + os.path.join(configdir, "extensions"),
        ]

def setup_handlers(web_app):
    web_app.add_handlers('.*', [
        (ujoin(web_app.settings['base_url'], 'vscode/(.*)'), VSCodeProxyHandler, dict(state={})),
        (ujoin(web_app.settings['base_url'], 'vscode'), AddSlashHandler),
    ])

