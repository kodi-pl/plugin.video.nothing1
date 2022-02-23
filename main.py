
from libka import SimplePlugin
from libka.logs import log


class Main(SimplePlugin):

    def home(self):
        import xbmcaddon
        # xbmcaddon.Addon().getSettings().setInt('dupa', 123)
        val = xbmcaddon.Addon().getSetting('kupa')
        log.info(f'kupa: {val!r}')
        # ok = xbmcaddon.Addon().setSettingBool('logiczny', True)
        # log.info(f'old: {ok}')
        xbmcaddon.Addon().getSettings().setString('pupa', 'blada')

        val = self.settings.get('val01', 1)
        log.info(f'val01: {val!r}')
        self.settings.val01 = val + 1

        with self.directory() as kd:
            kd.menu(self.settings)
            kd.item(f'Value {val!r}', self.settings)


Main().run()
