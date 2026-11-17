"""Aja Blenderin taustatilassa. Luo STL:t ja muokattavan blend-tiedoston."""
import bpy
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.scale_length = 0.001

def cover(name, ymin, ymax):
    xmin, xmax, radius, height = -31, 163, 5, 10
    contour=[]
    for cx,cy,start in [(xmax-radius,ymax-radius,0),(xmin+radius,ymax-radius,90),(xmin+radius,ymin+radius,180),(xmax-radius,ymin+radius,270)]:
        for i in range(17):
            a=math.radians(start+i*90/16)
            contour.append((cx+radius*math.cos(a),cy+radius*math.sin(a)))
    n=len(contour)
    vertices=[(x,y,z) for z in (0,height) for x,y in contour]
    faces=[tuple(reversed(range(n))),tuple(range(n,2*n))]
    faces += [(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    mesh=bpy.data.meshes.new(name)
    mesh.from_pydata(vertices,[],faces)
    mesh.update()
    obj=bpy.data.objects.new(name,mesh)
    bpy.context.collection.objects.link(obj)
    # Pyöristä vain ulkokehän ylä- ja alareunat ennen reikien leikkaamista.
    bpy.context.view_layer.objects.active=obj
    obj.select_set(True)
    bevel=obj.modifiers.new('Ulkoreunat R4.8 mm','BEVEL')
    bevel.width=4.8
    bevel.segments=20
    bevel.limit_method='ANGLE'
    bevel.angle_limit=math.radians(30)
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    for x,diameter,depth,z in [(-18,6.8,12,5),(150,12.6,12,5),(-18,12.6,7.01,3.495)]:
        bpy.ops.mesh.primitive_cylinder_add(vertices=96,radius=diameter/2,depth=depth,location=(x,30,z))
        cutter=bpy.context.object
        bpy.context.view_layer.objects.active=obj
        mod=obj.modifiers.new('Läpireikä','BOOLEAN')
        mod.operation='DIFFERENCE'
        mod.solver='EXACT'
        mod.object=cutter
        bpy.ops.object.modifier_apply(modifier=mod.name)
        bpy.data.objects.remove(cutter,do_unlink=True)
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active=obj
    bpy.ops.wm.stl_export(filepath=str(OUT/(name+'.stl')),export_selected_objects=True)
    return obj

lid=cover('luukku_v6',-5,80)
bpy.context.view_layer.objects.active=lid
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'luukku_v6.blend'))
