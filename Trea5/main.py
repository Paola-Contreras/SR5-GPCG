#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213
#SR5 - Transformation

from gl import Renderer, color, V3, V2
from texture import Texture
import shader as s 


w = 700
h = 600

rend = Renderer(w, h)
position = V3(2,-1.2,1)

#High
#rend.glLookAt(position,V3(0,2,0))

#Low
#rend.glLookAt(position,V3(0,-4,0))

#Dutch
#rend.glLookAt(position,V3(0, -2, -0.5))

#Medium
rend.glLookAt(position,V3(1,0,-2))




#MAIN
rend.active_shader = s.flat
rend.active_texture = Texture("model/earthDay.bmp")

rend.glLoadModel("model/coffee.obj",
                  translate = position,
                  rotate = V3(0, 0, 0),
                  scale = V3(2,2,2))

rend.glFinish("medium_angle.bmp")


