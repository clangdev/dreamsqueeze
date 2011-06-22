from SBSAlbum import SBSAlbum
from SBSArtist import SBSArtist
import telnetlib



class SBSCLIInterface:
    def __init__(self, host, port, username="", password=""):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        
        
    
    
    def getArtists(self):
        lArtists = []
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("info total artists ?\n")
        tn.read_until("info total artists ", 20)
        nArtists = int(tn.read_eager())
        current = 1
        last = 0
        while last < nArtists:
            tn = telnetlib.Telnet("ts439-pro-ii", 9090)
            tn.write("artists " + str(last) + " " + str(current) + "\n")
            tn.read_until("%3A", 20)
            artistid = tn.read_until(" ", 20)
            tn.read_until("%3A", 20)
            artistname = tn.read_until(" ", 20)
            lArtists.append(SBSArtist(artistid, str(self.utf8ToNormal(artistname))))
            current = current + 1
            last = last + 1
            tn.read_eager();
        tn.close()
        return lArtists
    
    
    def getArtists2(self):
        lArtists = []
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("info total artists ?\n")
        tn.read_until("info total artists ", 20)
        nArtists = int(tn.read_eager())
       
       
       
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("artists 0 " + str(nArtists)+"\n")
        response = tn.read_until("count", 20)
        tn.close()
        index = 0
        if index > -1: 
            while index > -1:
                von = response.find(" id%3A", index)+6
                to = response.find(" artist%3A", von)
                artistid = int(response[von:to])
                von = response.find(" artist%3A", to)+10
                to = response.find(" id%3A", von)
                artistname = response[von:to]
                lArtists.append(SBSArtist(artistid, str(artistname)))
                index = response.find(" id%3A", to)
        return lArtists
    
    def getAlbums(self, artistid="0"):
        lAlbums = []
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("info total albums ")
        if int(artistid) > 0:
            tn.write("artist_id:" + str(artistid) + " ?\n")
            tn.read_until("info total albums artist_id:" + str(artistid) + " ", 20)
        else:
            tn.write("?\n")
            tn.read_until("info total albums ")
        nAlbums = int(tn.read_eager())
        current = 1
        last = 0
        while last < nAlbums:
            tn = telnetlib.Telnet("ts439-pro-ii", 9090)
            tn.write("albums " + str(last) + " " + str(current) + " ")
            if int(artistid) > 0:
                tn.write("artist_id:" + str(artistid) + " ?\n")
                tn.read_until("%3A", 20)
            else:
                tn.write("?\n")
                tn.read_until("%3A", 20)
            albumid = tn.read_until(" ", 20)
            tn.read_until("%3A", 20)
            albumname = tn.read_until(" ", 20)
            lAlbums.append(SBSAlbum(albumid, self.utf8ToNormal(albumname)))
            current = current + 1
            last = last + 1
            tn.read_eager();
        tn.close()
        return lAlbums

    def getAlbums2(self):
        lAlbums = []
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("info total albums ?\n")
        tn.read_until("info total albums ")
        nAlbums = int(tn.read_eager())
        tn.write("albums 0 " + str(nAlbums)+"\n")
        response = tn.read_until("count", 20)
        tn.close()
        index=0
        while index > -1:
            von = response.find(" id%3A", index)+6
            to = response.find(" album%3A", von)
            albumid = int(response[von:to])
            von = response.find(" album%3A", to)+9
            to = response.find(" id%3A", von)
            albumname = response[von:to]
            lAlbums.append(SBSAlbum(albumid, str(albumname)))
            index = response.find(" id%3A", to)
        return lAlbums


    def getAlbumsByID(self, artistid):
        lAlbums = []
        tn = telnetlib.Telnet("ts439-pro-ii", 9090)
        tn.write("albums 0 1 artist_id:" + str(artistid) + " ?\n")
        tn.read_until("count ", 20)
        nAlbums = int(tn.read_eager())
        tn.write("albums 0 " + str(nAlbums)+" artist_id:" + str(artistid) + "\n")
        response = tn.read_until("count", 20)
        tn.close()
        index=0
        while index > -1:
            von = response.find(" id%3A", index)+6
            to = response.find(" album%3A", von)
            albumid = int(response[von:to])
            von = response.find(" album%3A", to)+9
            to = response.find(" id%3A", von)
            albumname = response[von:to]
            lAlbums.append(SBSArtist(albumid, str(albumname)))
            index = response.find(" id%3A", to)
        return lAlbums

    
    def utf8ToNormal(self, utfString):
        utfString.replace(utfString, "%20", " ")
        utfString.replace(utfString, "%26", "&")
        return utfString.replace(utfString, "%3A", ":")

