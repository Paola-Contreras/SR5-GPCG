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

#High
#position = V3(5,0,2)
#rend.glLookAt(position,V3(0,7,0))

#Low
#position = V3(5,0,2)
#rend.glLookAt(position,V3(0,-4,0))

#Medium
#position = V3(7,3,2)
#rend.glLookAt(position,V3(2,1,-2))

#Dutch
position = V3(2,-1.2,1)
rend.glLookAt(position,V3(0, -2, -0.5))


#MAIN
rend.active_shader = s.flat
rend.active_texture = Texture("model/earthDay.bmp")

rend.glLoadModel("model/coffee.obj",
                  translate = position,
                  rotate = V3(-10, 0, 0),
                  scale = V3(1.5,1.5,1.5))

rend.glFinish("Dutch_angle.bmp")


