#Question:3
# Write a program that prompts the user to enter a radius and then calculates the volume and surface area of a sphere. 
#The formulas for volume and surface area are V = (4/3) _ pi _ r^3 and A = 4 _ pi _ r^2, respectively.

#(4/3) _ pi _ r^3 and A = 4 _ pi _ r^2
#calculate the volume
#calculate the surface area 
import math 
def calculate_sphere_properties(radius):
volume = (4/3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

radius= float(input("enter your radius of sphere"))
#calculate sphere
sphere_volume, sphere_surface_area = calculate_sphere_properties(radius)
#print
