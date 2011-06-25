from DreamSqueezeConfig import DreamSqueezeConfig
from SBSAlbum import SBSAlbum
from SBSArtist import SBSArtist
from SBSTitle import SBSTitle
from __common__ import printl2 as printl
from enigma import eServiceReference
from twisted.internet import reactor
import string
import telnetlib





class SBSCLIInterface:
    def __init__(self, session):
        self.session = session
        self.config = DreamSqueezeConfig(self.session)
    
    def getArtists2(self):
        lArtists = []
        if str(self.config.getHost()) != "":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                printl("Trying to Login with " + self.config.getUsername() + " and a pass (len=" + str(len(self.config.getPassword())) + ")")
                tn.write("login " + self.config.getUsername() + " " + self.config.getPassword() + "\n")
                d = tn.read_until("******",20)
                d=d+tn.read_eager()
                printl(d)
                tn.write("info total artists ?\n")
                tn.read_until("info total artists ", 20)
                nArtists = int(tn.read_eager())
                tn.write("artists 0 " + str(nArtists) + "\n")
                response = tn.read_until("count", 20)
                response=self.utf8ToNormal(response)
                tn.close()
                index = 0
                if index > -1: 
                    while index > -1:
                        von = response.find(" id:", index) + 4
                        to = response.find(" artist:", von)
                        artistid = int(response[von:to])
                        von = response.find(" artist:", to) + 8
                        to = response.find(" id:", von)
                        if to is - 1:
                            to = response.find(" count", von)
                        artistname = response[von:to]
                        #artistname = self.utf8ToNormal(artistname)
                        printl("Artistname: " + artistname)
                        lArtists.append(SBSArtist(artistid, artistname))
                        index = response.find(" id:", to)
            except Exception, e:
                raise e
        return lArtists

    
   
        
    
    def getAlbums2(self):
        lAlbums = []
        if str(self.config.getHost()) != "":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                printl("Trying to Login with " + self.config.getUsername() + " and a pass (len=" + str(len(self.config.getPassword())) + ")")
                d = tn.read_until("******",20)
                d=d+tn.read_eager()
                printl(d)
                tn.write("info total albums ?\n")
                tn.read_until("info total albums ")
                nAlbums = int(tn.read_eager())
                tn.write("albums 0 " + str(nAlbums) + "\n")
                response = tn.read_until("count", 20)
                response=self.utf8ToNormal(response)
                tn.close()
                index = 0
                while index > -1:
                    von = response.find(" id:", index) + 4
                    to = response.find(" album:", von)
                    albumid = int(response[von:to])
                    von = response.find(" album:", to) + 7
                    to = response.find(" id:", von)
                    if to is - 1:
                        to = response.find(" count", von)
                    albumname = response[von:to]
                    #albumname = self.utf8ToNormal(albumname)
                    printl("Albumname: " + albumname)
                    lAlbums.append(SBSAlbum(albumid, albumname))
                    index = response.find(" id:", to)
            except Exception, e:
                raise e
        return lAlbums

    def getAlbumsByID(self, artistid):
        lAlbums = []
        if str(self.config.getHost()) != "":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                printl("Trying to Login with " + self.config.getUsername() + " and a pass (len=" + str(len(self.config.getPassword())) + ")")
                tn.write("login " + self.config.getUsername() + " " + self.config.getPassword() + "\n")
                d = tn.read_until("******",20)
                d=d+tn.read_eager()
                printl(d)
                tn.write("albums 0 1 artist_id:" + str(artistid) + "\n")
                tn.read_until("count%3A", 20)
                nAlbums = int(tn.read_eager())
                tn.write("albums 0 " + str(nAlbums) + " artist_id:" + str(artistid) + "\n")
                response = tn.read_until("count", 20)
                response=self.utf8ToNormal(response)
                tn.close()
                index = 0
                while index > -1:
                    von = response.find(" id:", index) + 4
                    to = response.find(" album:", von)
                    albumid = int(response[von:to])
                    von = response.find(" album:", to) + 7
                    to = response.find(" id:", von)
                    if to is - 1:
                        to = response.find(" count", von)
                    albumname = response[von:to]
                    #albumname = self.utf8ToNormal(albumname)
                    printl("Albumname: " + albumname)
                    lAlbums.append(SBSAlbum(albumid, albumname))
                    index = response.find(" id:", to)
            except Exception, e:
                raise e
        return lAlbums


    def getTitlesByID(self, albumid):
        lTitles = []
        if str(self.config.getHost()) != "":
            try:
                tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
                printl("Trying to Login with " + self.config.getUsername() + " and a pass (len=" + str(len(self.config.getPassword())) + ")")
                tn.write("login " + self.config.getUsername() + " " + self.config.getPassword() + "\n")
                d = tn.read_until("******",20)
                d=d+tn.read_eager()
                printl(d)
                tn.write("titles 0 1 album_id:" + str(albumid) + " sort:tracknum\n")
                tn.read_until("count%3A", 20)
                nTitles = int(tn.read_eager())
                tn.write("titles 0 " + str(nTitles) + " album_id:" + str(albumid) + " sort:tracknum\n")
                response = tn.read_until("count", 20)
                response=self.utf8ToNormal(response)
                tn.close()
                index = 0
                while index > -1:
                    von = response.find(" id:", index) + 4
                    to = response.find(" title:", von)
                    id = int(response[von:to])
                    von = response.find(" title:", to) + 7
                    to = response.find(" genre:", von)
                    title = response[von:to]
                    von = response.find(" genre:", to) + 7
                    to = response.find(" artist:", von)
                    genre = response[von:to]
                    von = response.find(" artist:", to) + 8
                    to = response.find(" album:", von)
                    artist = response[von:to]
                    von = response.find(" album:", to) + 7
                    to = response.find(" duration:", von)
                    album = response[von:to]
                    von = response.find(" duration:", to) + 10
                    if(nTitles>1):
                        to = response.find(" tracknum:", von)
                        duration = response[von:to]
                        von = response.find(" tracknum:", to) + 10
                        to = response.find(" id:", von)
                        if to is - 1:
                            to = response.find(" count", von)
                            tracknum = response[von:to]
                    else:
                        to = response.find(" id:", von)
                        if to is - 1:
                            to = response.find(" count", von)
                            duration = response[von:to]
                        tracknum="1"
                    #title = self.utf8ToNormal(title)
                    lTitles.append(SBSTitle(id, title, genre, artist, album, duration, tracknum))
                    index = response.find(" id:", to)
            except Exception, e:
                raise e
        return lTitles

    def playTitle(self, playerid, id):
        try:
            printl("Playing Track_id:" + str(id))
            tn = telnetlib.Telnet(self.config.getHost(), self.config.getCLIPort())
            printl("Trying to Login with " + self.config.getUsername() + " and a pass (len=" + str(len(self.config.getPassword())))
            tn.write("login " + self.config.getUsername() + " " + self.config.getPassword() + "\n")
            d = tn.read_until("******",20)
            d=d+tn.read_eager()
            printl(d)
            tn.write(str(playerid) + " playlistcontrol cmd:delete\n")
            tn.read_until("count%3A", 20)
            tn.read_eager()
            tn.write(str(playerid) + " playlistcontrol cmd:load track_id:" + str(id) + "\n")
            tn.read_until("count%3A", 20)
            tn.read_eager()
            try:
                url = "http://" + self.config.getHost() + ":" + str(self.config.getPort()) + "/stream.mp3?bitrate=96"
                reactor.callLater(1, self._delayedPlay, eServiceReference(4097, 0, url))
                #self.session.nav.playService(eServiceReference(4097, 0, url))
            except Exception, e:
                printl(e)
        except Exception, e:
            raise e
            
        

    
    def utf8ToNormal(self, utfString):
        utfString = string.replace(utfString, "%20", " ")
        utfString = string.replace(utfString, "%26", "&")
        utfString = string.replace(utfString, "%3A", ":")
        return utfString


    def _delayedPlay(self, sref):
        self.session.nav.playService(sref)
