import unreal

def get_selected_content_browser_assets():
    selected_assets = unreal.EditorUtilityLibrary().get_selected_assets()
    return selected_assets

def remove_prefix(asset, prefix):
    name = asset.get_name()
    separated = str(name).split('_')
    
    i = 0
    while i < len(separated):
        print(i)
        print(str(len(separated[i])) + " length")
        if len(separated[i]) > 2 and str(separated[i] + '_') not in prefix:
            print(separated[i] + '_')
            break
        else:
            print(str(separated[i]) + " removed")
            separated.pop(i)

    return '_'.join(i for i in separated)

def generate_new_asset_name(asset): 
    prefixes = {
            unreal.MaterialInstance : "MI_",
            unreal.Material : "M_",
            unreal.Texture : "T_",
            unreal.Blueprint : "BP_",   
            unreal.StaticMesh : "S_",
            unreal.MaterialFunction : "MF_",            
            unreal.SkeletalMesh : "SK_",
            unreal.Skeleton : "SKEL_",
            unreal.AnimSequence : "A_",
            unreal.LevelSequence : "LS_",
            unreal.BlendSpace : "BS_",
            unreal.BlendSpace1D : "BS_",
            unreal.MorphTarget : "MT_",
            unreal.PhysicsAsset : "PHYS_",
            unreal.NiagaraSystem : "NS_"
            }

    for i in prefixes:
        if isinstance(asset, i):
            prefix = prefixes[i]
            prefixlist = [prefixes[b] for b in prefixes]
            return  prefix + remove_prefix(asset, prefixlist)

    return asset.get_name()

def change_selected_assets_names():
    selected_assets = get_selected_content_browser_assets()
    for i in range(len(selected_assets)):
        asset = selected_assets[i]

        old_name = asset.get_name()
        new_name = generate_new_asset_name(asset)
        #print(asset)
        if old_name == new_name:
            print(new_name + " does not changed")
            continue

        old_path = asset.get_path_name()
        asset_folder = unreal.Paths.get_path(old_path)
        new_path = asset_folder + "/" + new_name
        print(f"{old_name} -> {new_name}")
        rename_success = unreal.EditorAssetLibrary.rename_asset(old_path, new_path)
        if not rename_success:
            unreal.log_error("Could not rename" + old_path)

def run():
    print(get_selected_content_browser_assets())
    change_selected_assets_names()

run()