import unreal

"""
Script adds prefixes to the selected assets

"""

def remove_prefix(asset: unreal.Object, prefixes):
    name = asset.get_name()
    separated = str(name).split('_')
    i = 0
    if len(separated) == 1:
        return '_'.join(i for i in separated)
    
    while i < len(separated):
        if len(separated[i]) > 2 and str(separated[i] + '_') not in prefixes:
            break
        else:
            separated.pop(i)

    return '_'.join(i for i in separated)

def generate_new_asset_name(asset: unreal.Object):
    prefixes = {
            unreal.MaterialInstance : "MI_",
            unreal.EditorUtilityWidgetBlueprint : "EUW_",
            unreal.Material : "M_",
            unreal.Texture : "T_",
            unreal.Blueprint : "BP_",   
            unreal.StaticMesh : "SM_",
            unreal.MaterialFunction : "MF_",
            unreal.SkeletalMesh : "SK_",
            unreal.Skeleton : "SKEL_",
            unreal.AnimSequence : "A_",
            unreal.LevelSequence : "LS_",
            unreal.BlendSpace : "BS_",
            unreal.BlendSpace1D : "BS_",
            unreal.MorphTarget : "MT_",
            unreal.PhysicsAsset : "PHYS_",
            unreal.NiagaraSystem : "NS_",
            unreal.NiagaraEmitter : "NE_"
            }

    for i in prefixes:
        if isinstance(asset, i):
            prefix = prefixes[i]
            prefixlist = [prefixes[b] for b in prefixes]
            return  prefix + remove_prefix(asset, prefixlist)

    return asset.get_name()

def change_selected_assets_names():
    selected_assets = unreal.EditorUtilityLibrary().get_selected_assets()
    for i in range(len(selected_assets)):
        asset: unreal.Object = selected_assets[i]
        old_name = asset.get_name()
        new_name = generate_new_asset_name(asset)
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

def main():
    change_selected_assets_names()

if __name__ == "__main__":
    main()