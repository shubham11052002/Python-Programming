import math

def calculate_circle_area(radius):
    """Calculate and return the area of a circle."""
    return math.pi * radius ** 2


radius = float(input("Enter the radius: "))
print(f"Area of the circle: {calculate_circle_area(radius):.2f}")