#!/usr/bin/python          
import math

# Projectile Calculations Using Runge-Kutta Method

def f(p,q,C):
	return -C*p*math.sqrt(p**2+q**2)

def g(p,q,C,G):
    return -C*q*math.sqrt(p**2+q**2)-G

# Main Program Starts Here

# Set the initial angle (degrees) and velocity (ft/s)

V     = 500.0
angle = 50.0

# Set Acceleration due to gravity (ft/s^2) 
G = 32.0

# C is the coefficient of friction due to air

C = 0.0025

# Set stepsize value

h = 0.01

# Set the initial value of x and y

t = 0.0;
y = 0.0;
x = 0.0;

# Set the initial values for the x and y velocity components

p = V*math.cos(angle*math.pi/180.0)
q = V*math.sin(angle*math.pi/180.0)

print str(x) + "  " + str(y)

# Begin Runge-Kutta Method Here for Systems

while (y >= 0 ):
	f1 = f(p,q,C);
	g1 = g(p,q,C,G)
	f2 = f(p+h*f1/2,q+h*g1/2,C) 
	g2 = g(p+h*f1/2,q+h*g1/2,C,G) 
	f3 = f(p+h*f2/2,q+h*g2/2,C) 
	g3 = g(p+h*f2/2,q+h*g2/2,C,G) 
	f4 = f(p+h*f3,q+h*g3,C) 
	g4 = g(p+h*f3,q+h*g3,C,G) 
	dp = (f1 + 2*f2 + 2*f3 + f4 ) / 6
	dq = (g1 + 2*g2 + 2*g3 + g4 ) / 6
	x = x + p*h + 0.5*dp*h**2 
	y = y + q*h + 0.5*dq*h**2 
	p = p + dp*h
	q = q + dq*h
	t = t + h
	print str(t) + "  " + str(x) + "  " + str(y)
