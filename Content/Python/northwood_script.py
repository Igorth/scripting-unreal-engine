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


def get_all_actors():
    EAS = unreal.EditorActorSubsystem()
    actors = EAS.get_all_level_actors()

    for actor in actors:
        unreal.log(actor.get_name())


def get_selected_actors():
    EAS = unreal.EditorActorSubsystem()
    selected_actors = EAS.get_selected_level_actors()

    for actor in selected_actors:
        unreal.log(actor.get_name())

get_selected_actors()