import unreal

# Get the path for every asset in the directory
def list_asset_paths():
    EAL = unreal.EditorAssetLibrary()
    asset_paths = EAL.list_assets('/Game')
    
    for asset in asset_paths:
        unreal.log(asset)


def get_select_content_browser():
    EUL = unreal.EditorUtilityLibrary()
    selected_assets = EUL.get_selected_assets()

    for asset in selected_assets:
        unreal.log(asset.get_fname())