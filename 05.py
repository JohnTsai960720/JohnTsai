from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,5)
time(0.5)
mc.setBlock(x,y+1,z,5)
time(0.5)
mc.setBlock(x,y+2,z,5)

