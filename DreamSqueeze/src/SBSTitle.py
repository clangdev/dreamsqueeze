class SBSTitle:
       
    
    def __init__(self, titleid, titlename, genre, artist, album, duration,tracknum):
        self.titleid = titleid
        self.titlename = titlename
        self.genre = genre
        self.artist = artist
        self.album = album
        self.duration = duration
        self.tracknum=tracknum
        
    def getID(self):
        return self.titleid
    
    def getTitle(self):
        return self.titlename
    
    def getGenre(self):
        return self.genre
    
    def getArtist(self):
        return self.artist
    
    def getAlbum(self):
        return self.album
    
    def getDuration(self):
        return self.duration
    
    def getTracknum(self):
        return self.tracknum
    