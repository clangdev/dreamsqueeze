import telnetlib
import SBSArtist


class SBSCLIInterface:
    def __init__(self, host, port, username="", password=""):
        self.tn=telnetlib.Telnet(host,port)
        
        
        
    
    
    def getArtists(self):
        self.lArtists=[]
        self.tn.write("info total artists ?\n")
        self.tn.read_until("info total artists ",20)
        nArtists=int(self.tn.read_eager())
        current=1
        last=0
        while last<nArtists:
            self.tn.write("artists "+str(last)+" "+str(current)+"\n")
            self.tn.read_until("%3A", 20)
            artistid=self.tn.read_until(" ", 20)
            self.tn.read_until("%3A", 20)
            artistname=self.tn.read_until(" ", 20)
            self.lArtists[last]=SBSArtist.SBSArtist(artistid, artistname)
            current=current+1
            last=last+1
            self.tn.read_eager();
        return self.lArtists
    