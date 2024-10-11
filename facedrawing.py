from graphics import *

win = GraphWin('A face', 680, 520)
shape = Circle(Point(340, 240), 150)
shape.setOutline('teal')
shape.setFill('teal')
shape.draw(win)

eye1 = Circle(Point(260, 200), 35)
eye1.setOutline('white')
eye1.setFill('white')
eye1.draw(win)

dot1 = Circle(Point(260, 200), 15)
dot1.setOutline('black')
dot1.setFill('black')
dot1.draw(win)

eye2 = Circle(Point(420, 200), 35)
eye2.setOutline('white')
eye2.setFill('white')
eye2.draw(win)

dot2 = Circle(Point(420, 200), 15)
dot2.setOutline('black')
dot2.setFill('black')
dot2.draw(win)

aRectangle = Rectangle (Point ( 330, 200) , Point (350,280))
aRectangle.setOutline('red')
aRectangle.setFill('red')
aRectangle.draw(win)

aRectangle = Rectangle (Point ( 330, 200) , Point (350,280))
aRectangle.setOutline('red')
aRectangle.setFill('red')
aRectangle.draw(win)
