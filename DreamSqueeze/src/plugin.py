from Components.ActionMap import ActionMap
from Components.Label import Label
from DreamSqueeze import DreamSqueeze
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen




    
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
        
