import unreal 

"""
Script spawns an array of Static Mesh Actors from 0,0,0 coordinates

"""

margin = 100.0  #
axis = "X"      #
origin_x = 0.0  #   Inputs via Widget
origin_y = 0.0  #   
origin_z = 0.0  #

def spawn_actor(mesh: unreal.StaticMesh, location: unreal.Vector = unreal.Vector(), rotation: unreal.Rotator = unreal.Rotator()):
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actor_class = unreal.StaticMeshActor
    mesh_actor: unreal.StaticMeshActor = editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)
    mesh_actor.static_mesh_component.set_static_mesh(mesh)

def array_placing():
    selected_assets = unreal.EditorUtilityLibrary().get_selected_assets()

    i = 0
    temp = unreal.Vector(origin_x, origin_y, origin_z)
    while i < len(selected_assets):
        asset = selected_assets[i]
        if len(selected_assets) == 0:
            print("No selection")
            return None
        
        if isinstance(asset, unreal.StaticMesh): # Main
            if(i == 0):
                spawn_actor(mesh = asset, location=temp)
            else:
                if axis == "X":
                    temp.x = temp.x + abs(asset.get_bounding_box().min.x)
                else:
                    temp.y = temp.y + abs(asset.get_bounding_box().min.y)

                spawn_actor(location = temp, mesh = asset)

            if axis == "X":
                temp.x = temp.x + asset.get_bounding_box().max.x + float(margin)
            else:
                temp.y = temp.y + asset.get_bounding_box().max.y + float(margin)
        else:
            selected_assets.pop(i)
            continue

        i = i + 1
    
def main():
    array_placing()

if __name__ == "__main__":
    main()