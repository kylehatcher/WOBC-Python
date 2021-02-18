import sys

class Sphere:
    def __init__(self, radius, surface, volume):
        self.radius = radius
        self.surface = surface
        self.volume = volume

    def get_surface_area(s):
        surface = 4*3.14*(s.radius**2)
        s.surface = surface

    def get_volume(s):
        volume = 4/3*3.14*(s.radius**3)
        s.volume = volume

    def set_radius(s, num):
        s.radius += num
        Sphere.get_surface_area(s)
        Sphere.get_volume(s)

for i in range(1,len(sys.argv)):
    try:
        s = Sphere(float(sys.argv[i]),0,0)
        Sphere.get_surface_area(s)
        Sphere.get_volume(s)
        print(s.surface)
        print(s.volume)
        Sphere.set_radius(s, 1)
        print(s.surface)
        print(s.volume)
        print()
    except:
        next