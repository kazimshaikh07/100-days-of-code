import turtle
import random 
jimmy = turtle.Turtle()
my_screen = turtle.Screen()
jimmy.shape("turtle")
jimmy.color("grey")

#drawing square without loops
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)

#drawing square using for loop
# for square in range(0,4):
#     jimmy.left(90)
#     jimmy.forward(100)

#USING DASH LINE
# for dash_line in range(5):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)


#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# # 1.triangle
# for triangle in range(3):
#     jimmy.forward(100)
#     jimmy.right(120)
# #2.square
# for square in range(4):
#     jimmy.color("red")
#     jimmy.forward(100)
#     jimmy.right(90)
# #3.pentagon
# for pentagon in range(5):
#     jimmy.color("purple")
#     jimmy.forward(100)
#     jimmy.right(72)
# # 4.hexagon
# for hexagon in range(6):
#     jimmy.color("green")
#     jimmy.forward(100)
#     jimmy.right(60)
# #5.heptagon
# for heptagon in range(7):
#     jimmy.color("orange")
#     jimmy.forward(100)
#     jimmy.right(51.428)
# # #6.octagon
# for octagon in range(8):
#     jimmy.color("blue")
#     jimmy.forward(100)
#     jimmy.right(45)
# # #7.nanagon
# for nanagon in range(9):
#     jimmy.color("pink")
#     jimmy.forward(100)
#     jimmy.right(40)
# # #8.decagon
# for decagon in range(10):
#     jimmy.color("black")
#     jimmy.forward(100)
#     jimmy.right(36)

#using loops Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# color = ["blue","green","orange","red","purple","dodger blue", "sienna","light coral","moccasin"]
# def draw_shape(shape_sides):
#     angle_shape = 360/shape_sides
#     for shapes in range(shape_sides):
#         jimmy.forward(100)
#         jimmy.right(angle_shape)
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#     jimmy.color(random.choice(color))


#drawing random lines
# jimmy.shape("arrow")
# jimmy.pensize(5)
# jimmy.speed("fastest")
# color = ["blue","green","orange","red","purple","dodger blue", "sienna","light coral","moccasin"]
# direction = [0,90,180,270]
# for random_lines in range(500):
#     jimmy.forward(random.randint(15,25))
#     jimmy.setheading(random.choice(direction))
#     jimmy.color(random.choice(color))


#draw a spirograph
# jimmy.shape("arrow")
# jimmy.pensize(2)
# jimmy.speed("fastest")
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b= random.randint(0,255)
#     color = (r,g,b)
#     return color
# def spirograph (size_of_gap):
#     for spirograph_circle in range(int(360/size_of_gap)):
#         jimmy.circle(50)
#         jimmy.color(random_color())
#         jimmy.setheading(jimmy.heading()+20)
# spirograph(10)




# print(my_screen.exitonclick())