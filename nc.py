# Simple example
import rhino3dm
import sys


# make list of 5 points
pList = rhino3dm.Point3dList()
pList.Add(0.0,3,0)
pList.Add(3.0,3,0)
pList.Add(4.0,2,0)
pList.Add(5.0,1,0)
pList.Add(6.0,1,0)

# create nurbs curve
is_periodic = False
degree = 3
nc = rhino3dm.NurbsCurve.Create(is_periodic, degree, pList)

# files to write curves to
fy = open('fy_curve.csv', 'w')
fz = open('fz_curve.csv', 'w')

# Sample the curve to create a lot of points
for n in range(101):
  pt = nc.PointAt(2*n/100.0).Encode()

  #print("{},{},{}".format(pt['X'], pt['Y'], 0.0))
  fy.write("{},{},{}\n".format(pt['X'], pt['Y'],     0.0))
  fz.write("{},{},{}\n".format(pt['X'],     0.0, pt['Y']))


'''
points = nc.Points
print("\nprinting {}".format('number of points'))
print(len(points))

start = nc.PointAtStart
print("\nprinting {}".format('start'))
print(start)
mid = nc.PointAt(0.5)
print("\nprinting {}".format('mid'))
print(mid)

# print the control points
for i in range(len(points)):
  pt = points[i].Encode()
  print("xyzw = {} {} {} {}".format(pt['X'], pt['Y'],
    pt['Z'], pt['W']))
  #print("xyzw = {}".format(pt))
'''

'''
center = rhino3dm.Point3d(1,2,3)
arc = rhino3dm.Arc(center, 10, 1)
nc = arc.ToNurbsCurve()

#print("printing {}".format('arc'))
#print(arc)
#
#print("printing {}".format('nc'))
#print(nc)

p0 = rhino3dm.Point3d(0,3,0)
p1 = rhino3dm.Point3d(2,3,0)
p2 = rhino3dm.Point3d(3,2,0)
p3 = rhino3dm.Point3d(4,1,0)
p4 = rhino3dm.Point3d(6,1,0)

'''
