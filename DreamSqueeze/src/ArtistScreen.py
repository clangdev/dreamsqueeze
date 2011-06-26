from AlbumScreen import AlbumScreen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from SBSArtist import SBSArtist
from SBSCLIInterface import SBSCLIInterface
from Screens.Screen import Screen
#from MyErrorScreen import MyErrorScreen
from __common__ import printl2 as printl

class ArtistScreen(Screen):
    skin = """<screen position="center,center" size="800,600" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="800,520" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,560" size="800,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        self.CLI = SBSCLIInterface(self.session);
        self.artistlist=[]
        try:
            self.artistlist = self.CLI.getArtists2()
        except Exception, e:
            #self.session.open(MyErrorScreen)
            printl(e)
        mainmenulist = []
        i = 0
        while i < len(self.artistlist):
            artist = SBSArtist
            artist = self.artistlist[i]
            mainmenulist.append((artist.getName(), artist.getID())) 
            i = i + 1
        size = len(mainmenulist)
        if int(size) is 0:
            mainmenulist.append(("Zurueck", "loadback")) 
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
        printl(returnValue)
        if returnValue is not None:
            if str(returnValue) is "loadback":
                self.cancel()
            else:
# Vielleicht a als Variable bergeben
# Wenn args=retzunValue kommt Greenscreen
                self.session.open(AlbumScreen, returnValue)
        else:
            print "\n[MyShPrombt] cancel\n"
            self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)
