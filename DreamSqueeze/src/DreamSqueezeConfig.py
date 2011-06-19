from Components.config import config, ConfigSubsection, ConfigInteger,  ConfigText
       
class DreamSqueezeConfig():
   
    def __init__(self, session, args = 0):
        self.session = session
        config.plugins.DreamSqueeze = ConfigSubsection()
        config.plugins.DreamSqueeze.username = ConfigText("",fixed_size=False)
        config.plugins.DreamSqueeze.password = ConfigText("",fixed_size=False)
        config.plugins.DreamSqueeze.port = ConfigInteger(9001,limits = (1, 65536))
        config.plugins.DreamSqueeze.CLIport = ConfigInteger(9,limits = (1, 65536))
        config.plugins.DreamSqueeze.playername = ConfigText("playername",fixed_size=False)
        config.plugins.DreamSqueeze.username = ConfigText("en",fixed_size=False)
   
        
        

    def saveUsername(self,username):
        print "saving Username"
        config.plugins.DreamSqueeze.username.value=username
        config.plugins.DreamSqueeze.username.save()
        
        
    def getUsername(self):
        return config.plugins.DreamSqueeze.username.value   
    
    def savePlayername(self,playername):
        print "saving Playername"
        config.plugins.DreamSqueeze.playername.value=playername
        config.plugins.DreamSqueeze.playername.save()
        
        
    def getPlayername(self):
        return config.plugins.DreamSqueeze.playername.value  