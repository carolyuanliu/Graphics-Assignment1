from turtle import *
import math



#binary tree
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end 

# quad tree

def tree4(n, l, pen):
     # termination
     if n==0 or l<2:
          return
 
     # recursive contruction
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)
#end tree4

# fern fractal
def fern(n, l, pen):
     #termination
     if n==0 or l<2: return
     #recursive construction
     pen.forward(0.3*l)
     pen.left(55); fern(n-1, l/2, pen); pen.right(55)
     pen.forward(0.7*l)
     pen.right(40);fern(n-1, l/2, pen); pen.left(40)
     pen.forward(l)
     pen.left(10); fern(n-1, 0.8*l, pen); pen.right(10)
     pen.backward(2*l)
#end fern



# serpinsky gasket

def s(n,l, pen):

      #termination

      if n==0 or l<2:

           # draw an equilateral triangle

           for i in range(3):

                pen.forward(l)

                pen.left(120)

           #end for

           return

      #end if
 
     #recursive definition

      for i in range(3):

           s(n-1, l/2, pen)

           pen.forward(l)

           pen.left(120)

      #end for

 # end s

def koch(n, l, pen):
    if n == 0:
        pen.forward(l)
        return
    koch(n-1, l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)
    pen.right(120)
    koch(n-1, l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)

# koch snowflake
def snowFlake(n, l, pen):
     for i in range(3):
    
          koch(n,l,pen)
          pen.right(120)
   
# koch anti-snowflake

def antiSnowFlake(n, l, pen):
     for i in range(3):
    
          koch(n, l, pen)
          pen.left(120)


def gasket(n, l, pen):
    if n == 0:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        return
    for i in range(4):
        gasket(n-1, l/3, pen)
        pen.forward(l)
        pen.left(90)

# circular fractal
def cr(n, l, pen):
    if n == 0:
        pen.circle(l)
        return

    pen.circle(l)
    for i in range(4):
        
        cr(n-1, l/2, pen)

        pen.up()
        pen.left(90)
        pen.forward(l)
        pen.down()

        cr(n-1, l/2, pen)
        
        
        pen.right(90)
        
        cr(n-1, l/2, pen)

        
        pen.right(90)
        
        cr(n-1, l/2, pen)
        
        pen.up()
       
        pen.forward(l)
        pen.left(90)
        pen.down()
        
        return


# rhombus flower

def rf(n,l, pen):

     if n == 0 or l <2:
         for i in range(4):
             pen.left(60)
             pen.forward(l)
             
         return
    
         

     for i in range(6):
        rf(n-1, l, pen)
        pen.left(60)
    

#  Spiral
def fs(n, l, pen):
    if n == 0:
        pen.circle(l,180)
        return

    for i in range(n):
        pen.circle(l,180)
        fs(n-1, 2*l, pen)
        return
 
 
 
 
 
 
 
