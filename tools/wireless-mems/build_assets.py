"""Run with Blender on ai-tools: coloured STEP tessellation -> glTF + Cycles stills.
Usage: blender -b -t 6 --python build_assets.py -- /path/to/private/job
"""
import bpy,sys,json,math,hashlib,bmesh
from pathlib import Path
from mathutils import Vector
P=Path(sys.argv[sys.argv.index('--')+1]);out=P/'assets';out.mkdir(exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def linear(v): return v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4
for i,g in enumerate(json.loads((P/'meshes.json').read_text())):
 mesh=bpy.data.meshes.new(f"{g['category']}_{i:02d}")
 mesh.from_pydata([[v*.001 for v in p] for p in g['vertices']],[],g['faces']);mesh.update()
 bm=bmesh.new();bm.from_mesh(mesh);bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-8);bm.to_mesh(mesh);bm.free()
 for poly in mesh.polygons: poly.use_smooth=True
 mesh.set_sharp_from_angle(angle=math.radians(35));mesh.update()
 obj=bpy.data.objects.new(mesh.name,mesh);bpy.context.collection.objects.link(obj)
 mat=bpy.data.materials.new(mesh.name);mat.diffuse_color=tuple(linear(c) for c in g['color'][:3])+(1,);mat.use_nodes=True
 shader=mat.node_tree.nodes.get('Principled BSDF');shader.inputs['Base Color'].default_value=mat.diffuse_color
 shader.inputs['Roughness'].default_value=.42
 shader.inputs['Metallic'].default_value=.55 if g['category'] in ['connector','antenna','components'] else .08
 mesh.materials.append(mat)
 # Preserve CAD surface edges; source geometry includes package envelopes.
 obj['source_category']=g['category']
bpy.ops.export_scene.gltf(filepath=str(out/'assembly.glb'),export_format='GLB',export_yup=True,export_apply=True,export_cameras=False,export_lights=False,export_extras=True)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=True
prefs=bpy.context.preferences.addons['cycles'].preferences
try:
 if '--cpu' in sys.argv: raise RuntimeError('CPU requested to avoid another GPU workload')
 prefs.compute_device_type='HIP';prefs.get_devices()
 gpu=[d for d in prefs.devices if d.type=='HIP']
 if not gpu: raise RuntimeError('No HIP device')
 for d in prefs.devices: d.use=d.type=='HIP'
 scene.cycles.device='GPU';device='HIP'
except Exception: scene.cycles.device='CPU';device='CPU'
scene.world.color=(.25,.25,.25)
scene.view_settings.view_transform='AgX'
scene.view_settings.exposure=-.7
scene.render.image_settings.file_format='PNG';scene.render.film_transparent=False
scene.render.resolution_x=1400;scene.render.resolution_y=1000;scene.render.resolution_percentage=100
bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.00086));floor=bpy.context.object;floor.name='studio_floor'
mat=bpy.data.materials.new('Studio navy');mat.use_nodes=True;mat.node_tree.nodes.get('Principled BSDF').inputs['Base Color'].default_value=(.018,.035,.059,1);mat.node_tree.nodes.get('Principled BSDF').inputs['Roughness'].default_value=.7;floor.data.materials.append(mat)
def area(name,pos,power,size):
 data=bpy.data.lights.new(name,'AREA');data.energy=power;data.shape='DISK';data.size=size
 o=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(o);o.location=pos;o.rotation_euler=(-o.location).to_track_quat('-Z','Y').to_euler()
area('Key',(.015,-.02,.04),.03,.045);area('Fill',(-.03,.01,.02),.02,.03);area('Rim',(.01,.025,.025),.025,.025)
bpy.ops.object.camera_add(location=(.024,-.031,.028));cam=bpy.context.object;scene.camera=cam;cam.data.type='ORTHO';cam.data.ortho_scale=.037;cam.data.clip_start=.0001;cam.data.clip_end=10
cam.rotation_euler=(Vector((0,0,.0006))-cam.location).to_track_quat('-Z','Y').to_euler()
for name,pos in [('beauty',(.024,-.031,.028)),('top',(0,-.00001,.05)),('rear',(-.025,.03,.025))]:
 cam.location=pos;cam.rotation_euler=(Vector((0,0,.0006))-cam.location).to_track_quat('-Z','Y').to_euler()
 scene.render.filepath=str(out/(name+'.png'));bpy.ops.render.render(write_still=True)
(out/'asset-build.json').write_text(json.dumps({'renderer':'Blender Cycles','device':device,'samples':32,'geometry':'FreeCAD STEP tessellation; identity physical pose; glTF Y-up proper rotation','glb_bytes':(out/'assembly.glb').stat().st_size},indent=2))
print('WIRELESS_MEMS_ASSETS_COMPLETE',device,(out/'assembly.glb').stat().st_size)
