from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Screens.Screen import Screen
from SBSCLIInterface import SBSCLIInterface
from SBSAlbum import SBSAlbum
from __common__ import printl2 as printl
from TitleScreen import TitleScreen

class AlbumScreen(Screen):
    skin = """<screen position="center,center" size="1024,576" title="" flags="wfNoBorder">
               <widget name="playername" position="0,0" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
                <widget name="mainmenulist" position="0,40" size="1024,496" zPosition="2" scrollbarMode="showOnDemand" />
                <widget name="statusbar" position="0,536" size="1024,40" zPosition="2" valign=\"center\" halign=\"left\" foregroundColor=\"white\" font=\"Regular;20\" />
              </screen>"""
              
    def __init__(self, session, args=0):
        self.session = session
        self.CLI = SBSCLIInterface(self.session);
        self.albumlist=[]
        if args>0:
            try:
                self.albumlist = self.CLI.getAlbumsByID(args)
            except Exception,e:
                printl(e)
        else:
            try:
                self.albumlist=self.CLI.getAlbums2()
            except Exception,e:
                printl(e)
        mainmenulist = []
        i = 0
        while i < len(self.albumlist):
            album=SBSAlbum
            album = self.albumlist[i]
            mainmenulist.append((album.getName(), album.getID())) 
            i=i+1
        size = len(mainmenulist)
        if int(size) is 0:
            mainmenulist.append(("Zurueck", "loadback"))
        if args>0 and int(size) > 1:
            mainmenulist.append(("Alle abspielen", "playAll"))
        Screen.__init__(self, session)
        self["playername"] = Label("Alben")
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
                printl("I Want To Cancel!!", self, "D")
                self.close(None)
            else:
# Vielleicht a als Variable bergeben
# Wenn args=retzunValue kommt Greenscreen
                #self.session.open(TitleScreen, returnValue)
                printl("Öffne TitleScreen mit Paramateter:"+returnValue,self,"D")
        else:
            print "\n[MyShPrombt] cancel\n"
            self.close(None)

        
        
    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)

