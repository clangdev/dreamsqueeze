from Screens.Screen import Screen
from Components.config import config, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.ActionMap import ActionMap
       
class DreamSqueezeConfigScreen(ConfigListScreen,Screen):
    skin = """
        <screen position="100,100" size="550,400" title="DreamSqueeze Setup" >
        <widget name="config" position="0,0" size="550,360" scrollbarMode="showOnDemand" />
        <widget name="buttonred" position="10,360" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;18"/> 
        <widget name="buttongreen" position="120,360" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;18"/> 
        </screen>"""
    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
        self.list = []
        self.list.append(getConfigListEntry(_("DreamSqueeze Username"), config.plugins.DreamSqueeze.username))
        self.list.append(getConfigListEntry(_("Password"), config.plugins.DreamSqueeze.password))
        self.list.append(getConfigListEntry(_("send now playing Audio Tracks"), config.plugins.DreamSqueeze.sendSubmissions))
        self.list.append(getConfigListEntry(_("use DreamSqueezeProxy"), config.plugins.DreamSqueeze.useproxy))
        self.list.append(getConfigListEntry(_("DreamSqueezeProxy Port"), config.plugins.DreamSqueeze.proxyport))
        self.list.append(getConfigListEntry(_("Recommentation Level"), config.plugins.DreamSqueeze.recommendedlevel))
        self.list.append(getConfigListEntry(_("show Coverart"), config.plugins.DreamSqueeze.showcoverart))
        self.list.append(getConfigListEntry(_("Timeout Statustext (Seconds)"), config.plugins.DreamSqueeze.timeoutstatustext))
        self.list.append(getConfigListEntry(_("Timeout to select a Tab (Seconds)"), config.plugins.DreamSqueeze.timeouttabselect))
        self.list.append(getConfigListEntry(_("Interval to refresh Metadata (Seconds)"), config.plugins.DreamSqueeze.metadatarefreshinterval))

        self.list.append(getConfigListEntry(_("use Screensaver"), config.plugins.DreamSqueeze.sreensaver.use))
        self.list.append(getConfigListEntry(_("wait before Screensaver"), config.plugins.DreamSqueeze.sreensaver.wait))
        self.list.append(getConfigListEntry(_("show Coverart in Screensaver"), config.plugins.DreamSqueeze.sreensaver.showcoverart))
        self.list.append(getConfigListEntry(_("do Coverartanimation in Screensaver"), config.plugins.DreamSqueeze.sreensaver.coverartanimation))
        self.list.append(getConfigListEntry(_("Speed for Coverartanimation"), config.plugins.DreamSqueeze.sreensaver.coverartspeed))
        self.list.append(getConfigListEntry(_("Interval for Coverartanimation"), config.plugins.DreamSqueeze.sreensaver.coverartinterval))
        
        ConfigListScreen.__init__(self, self.list)
        self["buttonred"] = Label(_("cancel"))
        self["buttongreen"] = Label(_("ok"))
        self["setupActions"] = ActionMap(["SetupActions"],
        {
            "green": self.save,
            "red": self.cancel,
            "save": self.save,
            "cancel": self.cancel,
            "ok": self.save,
        }, -2)

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
