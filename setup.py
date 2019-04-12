import setuptools

setuptools.setup(
    name="nbvscodeproxy",
    version='0.7.0',
    url="https://github.com/jupyterhub/nbvscodeproxy",
    author="Ryan Lovett",
    description="Jupyter extension to proxy vscode session",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'notebook',
        'nbserverproxy >= 0.5.1'
    ],
    package_data={'nbvscodeproxy': ['static/*']},
)
