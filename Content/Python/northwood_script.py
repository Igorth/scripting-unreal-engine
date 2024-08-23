import unreal

# Get the path for every asset in the directory
def list_asset_paths():
    EAL = unreal.EditorAssetLibrary()
    asset_paths = EAL.list_assets('/Game')
    
    # for asset in asset_paths:
    #     unreal.log(asset)
    return asset_paths

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


def get_asset_class(class_type):
    EAL = unreal.EditorAssetLibrary()
    asset_paths = list_asset_paths()

    assets = []

    for asset_path in asset_paths:
        asset_data = EAL.find_asset_data(asset_path)
        asset_class = asset_data.asset_class
        # unreal.log(f"Asset Class: {asset_class}")  # Verify asset class name
        if asset_class == class_type:
            assets.append(asset_data.get_asset())

    # for asset in assets:
    #     unreal.log(f"Assets: {asset}")

    return assets


def get_static_mesh_data():
    static_meshes = get_asset_class('StaticMesh')
    
    for static_mesh in static_meshes:
        # asset_import_data = static_mesh.get_editor_property('asset_import_data')
        # fbx_file_path = asset_import_data.extract_filenames()
        # unreal.log(f"Static Mesh: {fbx_file_path}")
        lod_group_info = static_mesh.get_editor_property('lod_group')
        unreal.log(f"LOD Group: {lod_group_info}") 

        if lod_group_info == 'None':
            if static_mesh.get_num_lods() == 1:
                static_mesh.set_editor_property('lod_group', 'LargeProp')


def get_textures_twod():
    textures = get_asset_class('Texture2D')

    for texture in textures:
        texture_srgb = texture.get_editor_property('srgb')
        unreal.log(f"Texture sRGB: {texture_srgb}")

get_static_mesh_data()