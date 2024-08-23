import unreal

# Get the path for every asset in the directory
def list_asset_paths():
    EAL = unreal.EditorAssetLibrary()
    asset_paths = EAL.list_assets('/Game')
    
    for asset in asset_paths:
        unreal.log(asset)

list_asset_paths()