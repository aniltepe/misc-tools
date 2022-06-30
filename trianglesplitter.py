import math

class vector:
    def __init__(self, x, y, z):
        self.x = x #float
        self.y = y #float
        self.z = z #float
class vertex:
    def __init__(self, pos):
        self.pos = pos #vector
class triangle:
    def __init__(self, v1, v2, v3):
        self.normal = None #vector
        self.vertices = [v1, v2, v3] #vertice[]
        self.center = vector((v1.pos.x + v2.pos.x + v3.pos.x) / 3,
                             (v1.pos.y + v2.pos.y + v3.pos.y) / 3,
                             (v1.pos.z + v2.pos.z + v3.pos.z) / 3)
        self.todolist = [self]
        self.donelist = []


def veclen(a): #a:vector
    return math.sqrt(pow(a.x, 2) + pow(a.y, 2) + pow(a.z, 2)) 
def cross(a, b): #a:vector, b:vector
    return vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)
def normalize(a): #a:vector
    return vector(a.x / veclen(a), a.y / veclen(a), a.z / veclen(a)) if veclen(a) > 0.0 else vector(0.0, 0.0, 0.0)
def add(a, b): #a:vector, b:vector
    return vector(a.x + b.x, a.y + b.y, a.z + b.z)
def substract(a, b): #a:vector, b:vector
    return vector(a.x - b.x, a.y - b.y, a.z - b.z)
def halfsplit(t): #t:triangle
    new_vs = []
    new_ts = []
    for j in range(3):
        edge = substract(t.vertices[j % 3].pos, t.vertices[(j + 1) % 3].pos)
        edge_half = vector(edge.x / 2, edge.y / 2, edge.z / 2)
        new_v = vertex(add(t.vertices[(j + 1) % 3].pos, edge_half))
        new_vs.append(new_v)
    for j in range(3):
        new_t = triangle(t.vertices[j % 3], new_vs[j % 3], new_vs[(j - 1) % 3])
        new_ts.append(new_t)
    new_ts.append(triangle(new_vs[0], new_vs[1], new_vs[2]))
    return (new_vs, new_ts)
def area(t): #t:triangle
    edge1_len = veclen(substract(t.vertices[0].pos, t.vertices[1].pos))
    edge2_len = veclen(substract(t.vertices[1].pos, t.vertices[2].pos))
    edge3_len = veclen(substract(t.vertices[2].pos, t.vertices[0].pos))
    s = (edge1_len + edge2_len + edge3_len) / 2
    return math.sqrt(s * (s - edge1_len) * (s - edge2_len) * (s - edge3_len))


vertices = []
triangles = []

f = open("/Users/nazimaniltepe/Downloads/" + "righteyebrowdomain.obj", "r")
rows = f.read().split("\n")
for row in rows:
    if row.startswith("v "):
        splittedrow = row.split(" ")
        # if double whitespace exists in v and x y z
        if splittedrow[1] == "":
            pos = vector(float(splittedrow[2]), float(splittedrow[3]), float(splittedrow[4]))
        else:
            pos = vector(float(splittedrow[1]), float(splittedrow[2]), float(splittedrow[3]))
        newVertex = vertex(pos)
        vertices.append(newVertex)
    if row.startswith("f "):
        splittedrow = row.strip().split(" ")
        splittedrow = splittedrow[1:]
        if (len(splittedrow) == 4 and splittedrow[3] == "") or len(splittedrow) == 3:
            v1_idx = int(splittedrow[0] if "/" not in splittedrow[0] else splittedrow[0].split("/")[0]) - (1 if splittedrow[0][0] != "-" else 0)
            v2_idx = int(splittedrow[1] if "/" not in splittedrow[1] else splittedrow[1].split("/")[0]) - (1 if splittedrow[1][0] != "-" else 0)
            v3_idx = int(splittedrow[2] if "/" not in splittedrow[2] else splittedrow[2].split("/")[0]) - (1 if splittedrow[2][0] != "-" else 0)
            new_triangle = triangle(vertices[v1_idx], vertices[v2_idx], vertices[v3_idx])
            triangles.append(new_triangle)
   

# passed_tri_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#                   13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
#                   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
#                   35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

# accepted_tri_idx = [28, 52, 53, 56, 35]
accepted_tri_idx = [52]
rejected_tri_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                  24, 25, 26, 27, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 54, 55]

# accepted_tri_idx = [28, 52, 53, 56]
# 29, 30, 31, 32, 33, 34,
#                   35, 36, 37 
degree = 2
for tri_idx in range(len(triangles)):
    face = triangles[tri_idx]
    # face_area = area(face)
    if tri_idx not in accepted_tri_idx:
        continue
    if tri_idx in rejected_tri_idx:
        continue
    for i in range(degree):
        new_vertices = []
        new_triangles = []
        new_done = []
        while len(face.todolist) > 0:
            tri = face.todolist[0]
            ret_tuple = halfsplit(tri)
            new_vertices.extend(ret_tuple[0])
            new_triangles.extend(ret_tuple[1])
            new_done.append(tri)
            face.todolist.remove(tri)
        face.donelist.append(new_done)
        face.todolist.extend(new_triangles)

new_file = open("/Users/nazimaniltepe/Downloads/" + "righteyebrowdomain_instrns.txt", "w+")
new_line = ""
for tri in triangles:
    if triangles.index(tri) not in accepted_tri_idx:
        continue
    if triangles.index(tri) in rejected_tri_idx:
        continue
    for t in tri.todolist:
        new_line += "%6.5f" % t.center.x + " " + "%6.5f" % t.center.y + " " + "%6.5f" % t.center.z + " "
new_file.write(new_line[:-1])
new_file.close()

print("done")



