/* eslint-disable no-invalid-this */
import { UPlugin } from '@classes';

export default class CumcordLoader extends UPlugin {
  public appId = Astra.commands.registerSection({
    name: 'Cumcord',
    icon: 'https://avatars.githubusercontent.com/u/81397549?s=500'
  });
  public window = window as any;
  start(): void {
    fetch('https://raw.githubusercontent.com/Cumcord/Cumcord/stable/dist/build.js').then(res =>
      res.text().then(text => {
        eval(text);
        Astra.commands.registerCommand('Cumcord', {
          name: 'plugin',
          description: 'Manage Cumcord plugins.',
          aliases: [],
          applicationId: this.appId,
          execute: async eArgs => {
            const { options } = eArgs;
            if (options.add) {
              let plugUrl = options.add;
              if (
                plugUrl.match(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&//=]*)/g)
              ) {
                plugUrl = options.add.replace(/\/\s*$/, '');
                const res = await fetch(`${plugUrl}/plugin.json`);
                const manifest = await res.json();
                console.log(manifest.name);
                this.window.cumcord.plugins.importPlugin(plugUrl);
                return {
                  content: `Added \`${manifest.name}\``
                };
              }
              return {
                content: 'Invalid plugin URL!'
              };
            }

            if (options.remove) return {
              content: `Removed \`${options.remove}\``
            };
          },
          options: [
            {
              name: 'add',
              description: 'The plugin to add.',
              type: 3
            },
            {
              name: 'remove',
              description: 'The plugin to remove.',
              type: 3,
              choices: this.window.cumcord.plugins.pluginCache
                ? Object.keys(this.window.cumcord.plugins.pluginCache).map(plugin => ({
                  name: this.window.cumcord.plugins.pluginCache[plugin].manifest.name,
                  value: plugin
                }))
                : []
            }
          ]
        });
      }));
  }
  stop(): void {
    this.window.cumcord.uninject();
    Astra.commands.unregisterSection(this.appId);
    Astra.commands.unregisterCommands('hi');
    Astra.n11s.show('Cumcord has unloaded.');
  }
}
