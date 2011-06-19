from DreamSqueeze import DreamSqueeze
from Plugins.Plugin import PluginDescriptor





    
def main(session, **kwargs):
    session.open(DreamSqueeze)
      

       
def Plugins(**kwargs):
    return PluginDescriptor(
                            name="DreamSqueeze",
                            description="Squeezebox Client-Player",
                            where=PluginDescriptor.WHERE_PLUGINMENU,
                            icon="plugin.png",
                            fnc=main
                            )
        
