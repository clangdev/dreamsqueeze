from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Screens.Screen import Screen
from Components.Label import Label
from EinstellungenErweitertSpracheScreen import EinstellungenErweitertSpracheScreen




class EinstellungenErweitertScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        mainmenulist = []
        mainmenulist.append(("Remote-Musiksammlung", "loadRemoteMusiksammlungScreen"))
        mainmenulist.append(("Sprache", "loadSpracheScreen"))
        Screen.__init__(self, session)
        self["playername"] = Label("playername")
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
            if returnValue is "loadRemoteMusiksammlungScreen":
                print returnValue
            elif returnValue is "loadSpracheScreen":
                print returnValue
                self.session.open(EinstellungenErweitertSpracheScreen)
                
            else:
                print "\n[MyShPrombt] cancel\n"
                self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)