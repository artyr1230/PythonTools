import unreal 

"""
Script spawns an array of Static Mesh Actors from 0,0,0 coordinates

"""

MARGIN = 100

def spawn_actor(mesh: unreal.StaticMesh, location: unreal.Vector = unreal.Vector(), rotation: unreal.Rotator = unreal.Rotator()):
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actor_class = unreal.StaticMeshActor
    mesh_actor: unreal.StaticMeshActor = editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)
    mesh_actor.static_mesh_component.set_static_mesh(mesh)

def array_placing():
    selected_assets = unreal.EditorUtilityLibrary().get_selected_assets()

    i = 0
    temp = unreal.Vector()
    while i < len(selected_assets):
        asset = selected_assets[i]
        if len(selected_assets) == 0:
            print("No selection")
            return None
        
        if isinstance(asset, unreal.StaticMesh): # Main
            if(i == 0):
                spawn_actor(mesh = asset)
            else:
                temp.x = temp.x + abs(asset.get_bounding_box().min.x)
                spawn_actor(location= unreal.Vector(x = temp.x), mesh = asset)

            temp.x = temp.x + asset.get_bounding_box().max.x + MARGIN
        else:
            selected_assets.pop(i)
            continue

        i = i + 1
    
def main():
    array_placing()

if __name__ == "__main__":
    main()