import telnetlib
from SBSArtist import SBSArtist
from SBSAlbum import SBSAlbum

class SBSCLIInterface:
    def __init__(self, host, port, username="", password=""):
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        
        
    
    
    def getArtists(self):
        lArtists=[]
        tn = telnetlib.Telnet("ts439-pro-ii",9090)
        tn.write("info total artists ?\n")
        tn.read_until("info total artists ",20)
        nArtists=int(tn.read_eager())
        current=1
        last=0
        while last<nArtists:
            #tn = telnetlib.Telnet("ts439-pro-ii",9090)
            tn.write("artists "+str(last)+" "+str(current)+"\n")
            tn.read_until("%3A", 20)
            artistid=tn.read_until(" ", 20)
            tn.read_until("%3A", 20)
            artistname=tn.read_until(" ", 20)
            lArtists.append(SBSArtist(artistid, artistname))
            current=current+1
            last=last+1
            tn.read_eager();
        tn.close()
        return lArtists
    
    def getAlbums(self):
        lAlbums=[]
        tn = telnetlib.Telnet("ts439-pro-ii",9090)
        tn.write("info total albums ?\n")
        tn.read_until("info total albums ",20)
        nAlbums=int(tn.read_eager())
        current=1
        last=0
        while last<nAlbums:
            tn.write("albums "+str(last)+" "+str(current)+"\n")
            tn.read_until("%3A", 20)
            artistid=tn.read_until(" ", 20)
            tn.read_until("%3A", 20)
            artistname=tn.read_until(" ", 20)
            lAlbums.append(SBSAlbum(artistid, artistname))
            current=current+1
            last=last+1
            tn.read_eager();
        tn.close()
        return lAlbums
    