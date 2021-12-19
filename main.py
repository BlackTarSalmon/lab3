class sphere:
    def __init__(self, r,x,y,z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4*3.14*pow(self.r,3))/3

    def get_square(self):
        return 4*3.14*pow(self.r,2)

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self,r):
        self.r = r

    def set_center(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return pow((x-self.x),2) + pow((y-self.y),2) + pow((z-self.z),2) < pow(self.r,2)


class Matrix:
    def __init__(self, r1, r2):
        if len(r1) != len(r2) and len(r1) !=2:
            print('nah chief')
        else:
            l = []
            l.append(r1)
            l.append(r2)
            self.mat = l
            self.det = l[0][0]*l[1][1]-l[0][1]*l[1][0]

    def __str__(self):
        m = self.mat
        for j in m:
            for i in j:
                print(i, end=" ")
            print()
        return ''

    def __gt__(self, other):
        return (self.det > other.det)

    def __lt__(self, other):
        return (self.det < other.det)

    def __eq__(self, other):
        return (self.det == other.det)

    def __add__(self, other):
        m1 = self.mat
        m2 = other.mat
        out = [[0,0],[0,0]]
        for x in range(2):
            for y in range(2):
                out[x][y] = m1[x][y] + m2[x][y]
        return Matrix(out[0], out[1])

    def __mul__(self, other):
        m1 = self.mat
        m2 = other.mat
        out = [[0, 0], [0, 0]]
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    out[x][y] += m1[x][z] * m2[z][y]
        return Matrix(out[0], out[1])


s = sphere(2,0,0,0)
print(s.get_center())
print(s.get_radius())
print(s.get_square())
print(s.get_volume())
print(s.is_point_inside(0.5,0.2,1))

print()
mat = Matrix([2,3],[-1,0])
print('det')
print(mat.det)
print('compare')
print(Matrix([1,0],[0,1]) > Matrix([2,0],[1,1]))
print('add')
print(Matrix([1,0],[0,1]) + Matrix([2,0],[1,1]))
print('multiply')
print(Matrix([1,0],[0,1]) * Matrix([2,0],[1,1]))