#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213
#SR3 - OBJ objects 

from gl import Renderer, color, V3, V2
from texture import Texture
import shader as s 
import math as m 

w = 700
h = 600

w2 = int( w / 2 )
h2 = int ( h / 2 )
ejex = int( w / 4 )
ejey = int( h / 9 )

rend = Renderer(w, h)
rend.glViewport(ejex,ejey,w2,h2)


#High
#position = V3(5,0,2)
#rend.glLookAt(position,V3(0,7,0))

#Low
#position = V3(5,0,2)
#rend.glLookAt(position,V3(0,-4,0))

#Medium
#position = V3(7,3,2)
#rend.glLookAt(position,V3(2,6,-3))

#Dutch
position = V3(7,-1,0)
rend.glLookAt(position, V3(0,1,0))


#MAIN
rend.active_shader = s.flat
rend.active_texture = Texture("model/earthDay.bmp")

rend.glLoadModel("model/coffee.obj",
                  translate = position,
                  rotate = V3(0, 0, 0),
                  scale = V3(6, 6, 6))

rend.glFinish("dutch_shot.bmp")

