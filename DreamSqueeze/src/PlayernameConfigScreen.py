from Screens.Screen import Screen
from Components.config import config, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.ActionMap import ActionMap
       
class PlayernameConfigScreen(ConfigListScreen,Screen):
    skin = """<screen position="center,center" size="800,600" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="800,520" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,560" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
        self.list = []
        self.list.append(getConfigListEntry(_("Squeezebox-Name: "), config.plugins.DreamSqueeze.playername))
       
        
        ConfigListScreen.__init__(self, self.list)
        self["playername"] = Label("Einstellungen")
        self["statusbar"] = Label("test")
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
                                         "ok": self.save,
                                         "cancel": self.cancel
                                         }, -1)

    def save(self):
        print "saving"
        for x in self["config"].list:
            x[1].save()
        self.close(True)

    def cancel(self):
        print "cancel"
        for x in self["config"].list:
            x[1].cancel()
        self.close(False)
