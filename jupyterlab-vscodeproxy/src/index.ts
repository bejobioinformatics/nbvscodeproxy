// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import {
  JupyterLab, JupyterLabPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette
} from '@jupyterlab/apputils';

import {
  IMainMenu
} from '@jupyterlab/mainmenu';

import {
  Message
} from '@phosphor/messaging';

import {
  Menu
} from '@phosphor/widgets';

import {
  PageConfig, URLExt
} from '@jupyterlab/coreutils';

import '../style/index.css';

/**
 * The command IDs used by the vscode plugin.
 */
namespace CommandIDs {
  export
  const launch = 'vscode:launch';
};

/**
 * The class name for the rstudio icon
 */
const VSCODE_ICON_CLASS = 'jp-VSCodeIcon';


/**
 * Activate the vscode extension.
 */
function activate(app: JupyterLab, palette: ICommandPalette, mainMenu: IMainMenu): void {
  let counter = 0;
  const category = 'VSCode';
  const namespace = 'vscode-proxy';
  const command = CommandIDs.launch;
  const { commands, shell } = app;

  commands.addCommand(command, {
    label: 'Launch VSCode',
    caption: 'Start a new VSCode Session',
    execute: () => {
        window.open(PageConfig.getBaseUrl() + 'vscode/', 'VSCode Session');
    }
  });

  // Add commands and menu itmes.
  let menu = new Menu({ commands });
  menu.title.label = category;
  [
    CommandIDs.launch,
  ].forEach(command => {
    palette.addItem({ command, category });
    menu.addItem({ command });
  });
  mainMenu.addMenu(menu, {rank: 98});
}

/**
 * The rsession handler extension.
 */
const plugin: JupyterLabPlugin<void> = {
  id: 'jupyterlab_vscodeproxy',
  autoStart: true,
  requires: [ICommandPalette, IMainMenu],
  activate: activate,
};


/**
 * Export the plugin as default.
 */
export default plugin;
