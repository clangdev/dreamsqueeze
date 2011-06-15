from DreamSqueeze import DreamSqueeze
from Plugins.Plugin import PluginDescriptor
#from Components.config import config, ConfigSubsection, ConfigInteger, ConfigYesNo, ConfigText


###############################################################################        
plugin_path = ""
###############################################################################        

#config.plugins.DreamSqueeze = ConfigSubsection()
#config.plugins.DreamSqueeze.showcoverart = ConfigYesNo(default = True)
#config.plugins.DreamSqueeze.username = ConfigText("user",fixed_size=False)
#config.plugins.DreamSqueeze.password = ConfigText("passwd",fixed_size=False)
#config.plugins.DreamSqueeze.port = ConfigInteger(6676,limits = (1, 65536))
#config.plugins.DreamSqueeze.CLIport = ConfigInteger(6676,limits = (1, 65536))
#config.plugins.DreamSqueeze.playername = ConfigText("playername",fixed_size=False)

###############################################################################        
    
def main(session, **kwargs):
        session.open(DreamSqueeze)    


       
def Plugins(path, **kwargs):
    global plugin_path
    plugin_path = path
    return PluginDescriptor(
                            name="DreamSqueeze",
                            description="Squeezebox Client/Player",
                            where=PluginDescriptor.WHERE_PLUGINMENU,
                            icon="plugin.png",
                            fnc=main
                            )
        
############################################################################### 



   
            
