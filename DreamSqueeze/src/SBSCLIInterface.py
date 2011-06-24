from SBSAlbum import SBSAlbum
from SBSArtist import SBSArtist
import telnetlib
from DreamSqueezeConfig import DreamSqueezeConfig
from SBSTitle import SBSTitle





class SBSCLIInterface:
    def __init__(self, session):
        self.session=session
        self.config = DreamSqueezeConfig(self.session)
    
    def getArtists2(self):
        lArtists = []
        if str(self.config.getHost())!="":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                tn.write("login "+self.config.getUsername()+" "+self.config.getPassword()+"\n")
                tn.write("info total artists ?\n")
                tn.read_until("info total artists ", 20)
                nArtists = int(tn.read_eager())
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
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
                        if to is -1:
                            to = response.find(" count", von)
                        artistname = response[von:to]
                        lArtists.append(SBSArtist(artistid, str(artistname)))
                        index = response.find(" id%3A", to)
            except Exception, e:
                raise e
        return lArtists

    
   
        
    
    def getAlbums2(self):
        lAlbums = []
        if str(self.config.getHost())!="":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                tn.write("login "+self.config.getUsername()+" "+self.config.getPassword()+"\n")
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
                    if to is -1:
                        to = response.find(" count", von)
                    albumname = response[von:to]
                    lAlbums.append(SBSAlbum(albumid, str(albumname)))
                    index = response.find(" id%3A", to)
            except Exception, e:
                raise e
        return lAlbums

    def getAlbumsByID(self, artistid):
        lAlbums = []
        if str(self.config.getHost())!="":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                tn.write("login "+self.config.getUsername()+" "+self.config.getPassword()+"\n")
                tn.write("albums 0 1 artist_id:" + str(artistid) + "\n")
                tn.read_until("count%3A", 20)
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
                    if to is -1:
                        to = response.find(" count", von)
                    albumname = response[von:to]
                    lAlbums.append(SBSArtist(albumid, str(albumname)))
                    index = response.find(" id%3A", to)
            except Exception, e:
                raise e
        return lAlbums


    def getTitlesByID(self, artistid):
        lTitles = []
        if str(self.config.getHost())!="":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                tn.write("login "+self.config.getUsername()+" "+self.config.getPassword()+"\n")
                tn.write("titles 0 1 album_id:" + str(artistid) + "\n")
                tn.read_until("count%3A", 20)
                nAlbums = int(tn.read_eager())
                tn.write("titles 0 " + str(nAlbums)+" album_id:" + str(artistid) + "\n")
                response = tn.read_until("count", 20)
                tn.close()
                index=0
                while index > -1:
                    von = response.find(" id%3A", index)+6
                    to = response.find(" title%3A", von)
                    id = int(response[von:to])
                    von = response.find(" title%3A", to)+9
                    to = response.find(" genre%3A", von)
                    title = response[von:to]
                    von = response.find(" genre%3A", to)+9
                    to = response.find(" artist%3A", von)
                    genre = response[von:to]
                    von = response.find(" artist%3A", to)+10
                    to = response.find(" album%3A", von)
                    artist = response[von:to]
                    von = response.find(" album%3A", to)+9
                    to = response.find(" duration%3A", von)
                    album = response[von:to]
                    von = response.find(" duration%3A", to)+12
                    to = response.find(" id%3A", von)
                    if to is -1:
                        to = response.find(" count", von)
                    duration = response[von:to]
                    lTitles.append(SBSTitle(id, title,genre,artist,album,duration))
                    index = response.find(" id%3A", to)
            except Exception, e:
                raise e
        return lTitles

    def playTitle(self,playerid,id):
        try:
            tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
            tn.write("login "+self.config.getUsername()+" "+self.config.getPassword()+"\n")
            tn.write(self.config.getPlayername()+" playlistcontrol cmd:delete\n")
            tn.read_until("count%3A", 20)
            tn.read_eager()
            tn.write(self.config.getPlayername()+" playlistcontrol cmd:load track_id:"+id+"\n")
            tn.read_until("count%3A", 20)
            tn.read_eager()
        except Exception, e:
            raise e
            


    
    def utf8ToNormal(self, utfString):
        utfString.replace(utfString, "%20", " ")
        utfString.replace(utfString, "%26", "&")
        return utfString.replace(utfString, "%3A", ":")

