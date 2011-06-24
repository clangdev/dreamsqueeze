from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from SBSCLIInterface import SBSCLIInterface
from SBSTitle import SBSTitle
from Screens.Screen import Screen
from __common__ import printl2 as printl
import socket

class TitleScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        self.CLI = SBSCLIInterface(self.session);
        self.titlelist = self.CLI.getTitlesByID(args)
        mainmenulist = []
        i = 0
        while i < len(self.titlelist):
            title=SBSTitle
            title = self.titlelist[i]
            mainmenulist.append((title.getTitle(), title.getID())) 
            i=i+1
        size=len(mainmenulist)
        if int(size) is 0:
            mainmenulist.append(("Zurueck", "loadback")) 
        elif int(size) > 1:
            mainmenulist.append(("Alle abspielen", "playAll")) 
        Screen.__init__(self, session)
        self["playername"] = Label("Interpreten")
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
            if returnValue is "loadback":
                print returnValue
                self.cancel()
            else:
                try:
                    printl("Local IP: "+socket.getaddrinfo(socket.gethostname(), None)[0][4][0])
                    self.CLI.playTitle(str(socket.getaddrinfo(socket.gethostname(), None)[0][4][0]), returnValue)
                except Exception,e:
                    printl(e)
                    
# Vielleicht a als Variable bergeben
# Wenn args=retzunValue kommt Greenscreen
                #self.session.open(TitleScreen,returnValue)
        else:
            print "\n[MyShPrombt] cancel\n"
            self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)
