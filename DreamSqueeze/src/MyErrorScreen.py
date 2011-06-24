from Components.ActionMap import ActionMap
from Components.Label import Label
from Screens.Screen import Screen


class MyErrorScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="errorlabel" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        e=args
        Screen.__init__(self, session)
        self["playername"] = Label("Interpreten")
        self["errorlabel"] = Label(str(e))
        self["statusbar"] = Label("test")
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
                                         "ok": self.cancel,
                                         "cancel": self.cancel
                                         }, -1)
    
    
    
        
    

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)
