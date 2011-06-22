from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Screens.Screen import Screen
from SBSCLIInterface import SBSCLIInterface
from SBSAlbum import SBSAlbum

class AlbumScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0,artistid=0):
        self.session = session
        self.CLI = SBSCLIInterface(self,"ts439-pro-ii", 9090);
        if artistid>0:
            self.albumlist = self.CLI.getAlbums2()
        else:
            self.albumlist=self.CLI.getAlbumsByID(artistid)    
        mainmenulist = []
        i = 0
        while i < len(self.albumlist):
            album=SBSAlbum
            album = self.albumlist[i]
            mainmenulist.append((album.getName(), album.getID())) 
            i=i+1
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
            print returnValue
        else:
            print "\n[MyShPrombt] cancel\n"
            self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)