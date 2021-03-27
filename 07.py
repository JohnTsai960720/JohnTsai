from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y-1,z,x+25,y-1,z+25,152)