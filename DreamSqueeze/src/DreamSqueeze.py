from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from DreamSqueezeConfig import DreamSqueezeConfig
from EinstellungenScreen import EinstellungenScreen
from SBSScreen import SBSScreen
from Screens.Screen import Screen
from __common__ import printl2 as printl
from enigma import eServiceReference
from twisted.internet import reactor


class DreamSqueeze(Screen):
    skin = """<screen position="center,center" size="800,600" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="800,520" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,560" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""

    def __init__(self, session, args=0):
        self.session = session
        config = DreamSqueezeConfig(self.session)
        self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
        if config.useLogin() is True:
            try:
                url = "http://" + config.getUsername() + ":" + config.getPassword() + "@" + config.getHost() + ":" + str(config.getPort()) + "/stream.mp3"
                printl("stopping current Service")
                self.session.nav.stopService()
                strpass=""
                for char in config.getPassword():
                    strpass=strpass+"*"
                printl("starting Stream:" + "http://" + config.getUsername() + ":" + strpass + "@" + config.getHost() + ":" + str(config.getPort()) + "/stream.mp3")
                reactor.callLater(1, self._delayedPlay, eServiceReference(4097, 0, url))
                #self.session.nav.playService(eServiceReference(4097, 0, url))
            except Exception, e:
                printl(e)
        else:
            try:
                url = "http://" + config.getHost() + ":" + str(config.getPort()) + "/stream.mp3"
                printl("stopping current Service")
                self.session.nav.stopService()
                printl("starting Stream:" + url)
                reactor.callLater(1, self._delayedPlay, eServiceReference(4097, 0, url))
                printl("stream should be started")
                #self.session.nav.playService(eServiceReference(4097, 0, url))
            except Exception, e:
                printl(e)
        
        
        
        
        mainmenulist = []
        if str(config.getHost()) != "":
            mainmenulist.append(("Eigene Musik", "loadPersonalMusicScreen"))
            #mainmenulist.append(("Internetradio", "loadInternetRadioScreen"))
            #mainmenulist.append(("Favoriten", "loadFavoritesScreen"))
        mainmenulist.append(("Einstellungen", "loadSettingsScreen"))
        Screen.__init__(self, session)
        
        self["playername"] = Label(config.getPlayername())
        self["mainmenulist"] = MenuList(mainmenulist)
        self["statusbar"] = Label("test")
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
                                         "ok": self.go,
                                         "cancel": self.cancel
                                         }, -1)

    def go(self):
        returnValue = self["mainmenulist"].l.getCurrentSelection()[1]
        if returnValue is not None:
            if returnValue is "loadPersonalMusicScreen":
                print returnValue
                self.session.open(SBSScreen)
            elif returnValue is "loadInternetRadioScreen":
                print returnValue
            elif returnValue is "loadFavoritesScreen":
                print returnValue
            elif returnValue is "loadSettingsScreen":
                print returnValue
                self.session.open(EinstellungenScreen)
            else:
                print "\n[MyShPrombt] cancel\n"
                self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.session.nav.playService(self.oldService)
        self.close(None)
        
        
        
        
    def _delayedPlay(self, sref):
        self.session.nav.playService(sref)
        
        
        
        
    




