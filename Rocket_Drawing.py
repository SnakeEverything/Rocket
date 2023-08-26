from Focus_Roots import*


def change():
    draw_rect(170,100,150,300,0,color=color_firebrick)# Rocket Body
    draw_polygon([[100,100],[390,100],[240,10]],0,color=color_sky_blue)#Rocket Nose
    draw_polygon([[170,200],[100,400],[170,400]],0,color=color_sky_blue)#Right Wing
    draw_polygon([[320,200],[400,400],[320,400]],0,color=color_sky_blue)#Left Wing
    draw_circle(240,150,30,0,color=color_banana)#Top Window
    draw_circle(240,250,30,0,color=color_banana)#Middle Window
    draw_circle(240,350,30,0,color=color_banana)#Bottom Window
    write_text(text = "Boarding for Mars!", x = 250, y = 440, size = 34)#Text
draw(change)