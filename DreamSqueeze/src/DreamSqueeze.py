from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Screens.Screen import Screen
#from Components.Label import Label

class DreamSqueeze(Screen):
    skin = """<screen position="100,150" size="460,400" title="Ihad.tv tutorial e2-tutorial lesson 5" >
                <widget name="mainmenulist" position="10,10" size="420,380" scrollbarMode="showOnDemand" />
              </screen>"""

    def __init__(self, session, args=0):
        self.session = session
        mainmenulist = []
        mainmenulist.append(("Eigene Musik", "loadPersonalMusicScreen"))
        mainmenulist.append(("Internetradio", "loadInternetRadioScreen"))
        mainmenulist.append(("Favoriten", "loadFavoritesScreen"))
        mainmenulist.append(("Einstellungen", "loadSettingsScreen"))
        Screen.__init__(self, session)
        self["mainmenulist"] = MenuList(mainmenulist)
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
                                         "ok": self.go,
                                         "cancel": self.cancel
                                         }, -1)
