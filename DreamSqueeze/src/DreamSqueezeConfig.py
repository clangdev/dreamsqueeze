from Components.config import config, ConfigSubsection, ConfigInteger, \
    ConfigText, ConfigYesNo



       
class DreamSqueezeConfig():
   
    def __init__(self, session, args=0):
        self.session = session
        config.plugins.DreamSqueeze = ConfigSubsection()
        config.plugins.DreamSqueeze.useLogin = ConfigYesNo(False)
        config.plugins.DreamSqueeze.username = ConfigText("", fixed_size=False)
        config.plugins.DreamSqueeze.password = ConfigText("", fixed_size=False)
        config.plugins.DreamSqueeze.host = ConfigText("", fixed_size=False)
        config.plugins.DreamSqueeze.port = ConfigInteger(9001, limits=(1, 65536))
        config.plugins.DreamSqueeze.cliport = ConfigInteger(9090, limits=(1, 65536))
        config.plugins.DreamSqueeze.playername = ConfigText("", fixed_size=False)
        config.plugins.DreamSqueeze.language = ConfigText("", fixed_size=False)
           
    def getUsername(self):
        return config.plugins.DreamSqueeze.username.value 
    
    def getPassword(self):
        return config.plugins.DreamSqueeze.password.value  
    
    def getHost(self):
        return config.plugins.DreamSqueeze.host.value  
    
    def getPort(self):
        return config.plugins.DreamSqueeze.port.value  
    
    def getCLIPort(self):
        return config.plugins.DreamSqueeze.cliport.value  
      
    def getPlayername(self):
        return config.plugins.DreamSqueeze.playername.value  
    
    def getLanguage(self):
        return config.plugins.DreamSqueeze.language.value
    
    def saveLanguage(self,language):
        config.plugins.DreamSqueeze.language.value=language
        config.plugins.DreamSqueeze.language.save()
    
    def useLogin(self):
        return config.plugins.DreamSqueeze.useLogin.value
        
