"""Riippuvuukseton STL-vienti yhteiseen tasojakoon perustuvista kerroksista."""
import math
import struct
from collections import Counter
from pathlib import Path

HEIGHT = 10
POCKET_DEPTH = 7

def make(name, ymin, ymax):
    outer = []
    for cx, cy, a in [(158, ymax-5, 0), (-26, ymax-5, 90), (-26, ymin+5, 180), (158, ymin+5, 270)]:
        outer += [(cx+5*math.cos(math.radians(a+i*90/16)), cy+5*math.sin(math.radians(a+i*90/16))) for i in range(17)]
    circles = [(-18, 3.4), (150, 6.3), (-18, 6.3), (150, 6.3)]
    holes = [[(cx+r*math.cos(i*math.tau/96), 30+r*math.sin(i*math.tau/96)) for i in range(96)] for cx, r in circles]
    loops = [outer]+holes
    xs = sorted(set(round(x, 8) for loop in loops for x, y in loop))
    def val(edge, x):
        (a,b),(c,d) = edge
        return b+(d-b)*(x-a)/(c-a)
    def spans(loop, x):
        return sorted([(p,q) for p,q in zip(loop,loop[1:]+loop[:1]) if min(p[0],q[0]) < x < max(p[0],q[0])], key=lambda e: val(e,x))
    cells = []
    for l, r in zip(xs, xs[1:]):
        mid = (l+r)/2
        edges = sorted([edge for loop in loops for edge in spans(loop,mid)], key=lambda e: val(e,mid))
        for low, high in zip(edges,edges[1:]):
            if val(high,mid)-val(low,mid)<1e-9: continue
            cy = (val(low,mid)+val(high,mid))/2
            inside = []
            for hole in holes:
                he = spans(hole,mid)
                inside.append(len(he)==2 and val(he[0],mid)<cy<val(he[1],mid))
            if inside[0] or inside[1]: continue
            cells.append(([(l,val(low,l)),(r,val(low,r)),(r,val(high,r)),(l,val(high,l))], not(inside[2] or inside[3])))
    def key(p): return tuple(round(v,6) for v in p)
    levels = {}
    for cell, bottom in cells:
        for x,y in cell: levels.setdefault(round(x,6),set()).add(round(y,6))
    polygons=[]
    for cell,bottom in cells:
        poly=[]
        for p,q in zip(cell,cell[1:]+cell[:1]):
            p,q=key(p),key(q)
            if p==q: continue
            poly.append(p)
            if p[0]==q[0]:
                ys=sorted(y for y in levels[p[0]] if min(p[1],q[1])<y<max(p[1],q[1]))
                if q[1]<p[1]: ys.reverse()
                poly += [(p[0],y) for y in ys]
        polygons.append((poly,bottom))
    tris=[]
    for z0,z1,lower in [(0,POCKET_DEPTH,True),(POCKET_DEPTH,HEIGHT,False)]:
        boundary=Counter()
        for poly,bottom in polygons:
            if lower and not bottom: continue
            center=key(tuple(sum(p[i] for p in poly)/len(poly) for i in (0,1)))
            for p,q in zip(poly,poly[1:]+poly[:1]):
                if p==q: continue
                tris += [((*center,z1),(*p,z1),(*q,z1)),((*center,z0),(*q,z0),(*p,z0))]
                boundary[(p,q)]+=1
        for (p,q),n in boundary.items():
            if boundary[(q,p)]: continue
            tris += [((*p,z0),(*q,z0),(*q,z1)),((*p,z0),(*q,z1),(*p,z1))]
    faces={}
    for tri in tris:
        k=tuple(sorted(tri))
        if k in faces: del faces[k]
        else: faces[k]=tri
    with open(Path(__file__).with_name(name+'.stl'),'wb') as f:
        f.write(b'Bird feeder lid v3, units mm'.ljust(80,b'\0'))
        f.write(struct.pack('<I',len(faces)))
        for a,b,c in faces.values():
            u=[b[i]-a[i] for i in range(3)]; v=[c[i]-a[i] for i in range(3)]
            normal=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
            length=math.sqrt(sum(t*t for t in normal))
            normal=[t/length if length else 0 for t in normal]
            f.write(struct.pack('<12fH',*normal,*a,*b,*c,0))
    print(name+'.stl luotu')

make('luukku_v3',-5,80)
make('sovitusliuska_v3',21,39)
