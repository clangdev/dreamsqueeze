from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Screens.Screen import Screen
from Components.Label import Label
from DreamSqueezeConfig import DreamSqueezeConfig



class EinstellungenErweitertSpracheScreen(Screen):
    skin = """<screen position="center,center" size="800,600" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="800,520" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,560" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        self.config=DreamSqueezeConfig(self.session)
        mainmenulist = []
        mainmenulist.append(("Deutsch", "setDeutsch"))
        mainmenulist.append(("Englisch", "setEnglisch"))
        Screen.__init__(self, session)
        self["playername"] = Label("Sprache")
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
            if returnValue is "setDeutsch":
                self.config.saveLanguage("de")
            elif returnValue is "setEnglisch":
                self.config.saveLanguage("en")
            else:
                print "\n[MyShPrombt] cancel\n"
                self.close(None)
            self.close(None)
        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)