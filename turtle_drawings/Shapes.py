import turtle as tl

sc = tl.Screen()
sc.bgcolor('black')
sc.title('Si11_ibrahim')

dr = tl.Turtle()


tl.colormode('blue')
tl.title('Si11_ibrahim')

dr.speed(5)
dr.pencolor('white')
dr.pensize(10)

shape = str(input('Enter a Shape Name: '))

if shape == 'square':  ###################  Square  ##############
    for i in range(4):
        dr.right(90)
        dr.forward(200)

elif shape == 'rectangle':  #############  Rectangle  ############
    for i in range(2):
        dr.right(90)
        dr.forward(100)
        dr.right(90)
        dr.forward(200)


elif shape == 'triangle':   #############  Triangle  ##############
    for i in range(3):
        dr.left(120)
        dr.forward(200)

elif shape == 'circle':    ##############  Circle  ################
    for i in range(75):
        dr.speed(20)
        dr.right(5)
        dr.forward(5)

elif shape == 'rhombus':   ##############  Rhombus  ###############
    dr.right(45)
    dr.forward(200)
    dr.right(90)    
    dr.forward(200)
    dr.right(90)    
    dr.forward(200)
    dr.right(90)    
    dr.forward(200)

elif shape == 'parelellogram':    #######  Parelellogram  #########
    dr.setpos(400,0)
    dr.right(110)
    dr.forward(400)
    dr.right(70)
    dr.forward(400)
    dr.right(110)
    dr.forward(400)



    
elif shape == 'hexagon':    ##############  Hexagon  ###############
    for i in range(6):
        dr.right(60)
        dr.forward(80)

elif shape == 'bucket':     ##############  Bucket  ################
    dr.right(100)
    dr.forward(200)
    dr.right(80)
    dr.forward(100)
    dr.right(80)
    dr.forward(200)
    dr.right(100)
    dr.forward(170)
    dr.right(100)
    dr.forward(30)
    dr.right(80)
    dr.forward(160)
    dr.right(88)
    dr.forward(1)
    for i in range(60):
        dr.pencolor('black')
        dr.right(3)
        dr.forward(4.2)


elif shape == 'heart':      ############  Heart  ###################
    dr.fillcolor
    dr.pencolor('red')
    dr.speed(20)
    dr.left(90)
    dr.forward(1)
    for i in range(40):    
        dr.left(5)
        dr.forward(4)

    for i in range(3):   
        dr.left(7)
        dr.forward(20)
        dr.left(7)
        dr.forward(20)

    dr.left(50)
    for i in range(6):
        dr.left(7)
        dr.forward(20.5)

    for i in range(40):
        dr.left(5)
        dr.forward(3.5)



else:
    print('This shape is not available')


tl.done()





            ###################      ##########################           ########                ########
            ###################      ##########################          #########               #########
            ####                               #####                    #### #####              #### #####
            ####                               #####                   ####  #####             ####  #####
            ####                               #####                  ####   #####            ####   #####
            ###################                #####                         #####                   #####
            ###################                #####                         #####                   #####
                           ####                #####                         #####                   #####
                           ####                #####                         #####                   #####
                           ####                #####                         #####                   #####
            ###################      ##########################      #####################   #####################
            ###################      ##########################      #####################   #####################
