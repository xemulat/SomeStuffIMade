import { Plugin } from '@vizality/entities';
import electron from 'electron'

export default class cumcordLoader extends Plugin {
  async start () {
    electron.webFrame.top.context.eval(await (await fetch('https://raw.githubusercontent.com/Cumcord/Cumcord/stable/dist/build.js')).text())
  }

  stop () {
    cumcord.uninject()
  }
}