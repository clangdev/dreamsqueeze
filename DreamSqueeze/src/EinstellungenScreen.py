from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Screens.Screen import Screen
from Components.Label import Label
from EinstellungenErweitertScreen import EinstellungenErweitertScreen


class EinstellungenScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        mainmenulist = []
        mainmenulist.append(("Squeezebox-Name", "loadSqueezeboxNameScreen"))
        mainmenulist.append(("Player waehlen", "loadPlayerwaehlenScreen"))
        mainmenulist.append(("Synchronisieren", "loadSynchronisierenScreen"))
        mainmenulist.append(("Erweitert", "loadErweitertScreen"))
        Screen.__init__(self, session)
        self["playername"] = Label("Einstellungen")
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
            if returnValue is "loadSqueezeboxNameScreen":
                print returnValue
            elif returnValue is "loadPlayerwaehlenScreen":
                print returnValue
            elif returnValue is "loadSynchronisierenScreen":
                print returnValue
            elif returnValue is "loadErweitertScreen":
                print returnValue
                self.session.open(EinstellungenErweitertScreen)
            else:
                print "\n[MyShPrombt] cancel\n"
                self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)