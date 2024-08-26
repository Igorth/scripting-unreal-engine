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


def get_static_mesh_lod_data():
    """
        Returns the triangles of the mesh
    """
    PML = unreal.ProceduralMeshLibrary()
    static_meshes = get_asset_class('StaticMesh')

    static_mesh_lod_data = []

    for static_mesh in static_meshes:
        static_mesh_tri_count = []         
        num_lods = static_mesh.get_num_lods()

        for i in range(num_lods):
            num_sections = static_mesh.get_num_sections(i)
            lod_tri_count = 0

            for j in range(num_sections):
                section_data = PML.get_section_from_static_mesh(static_mesh, i, j)
                section_tri_count = (len(section_data[1]) / 3)
                lod_tri_count += section_tri_count

            static_mesh_tri_count.append(lod_tri_count)

        static_mesh_reductions = [100]

        for i in range(1, len(static_mesh_tri_count)):
            static_mesh_reductions.append(int((static_mesh_tri_count[i]/static_mesh_tri_count[0]) * 100 ))


        # unreal.log(f"Name: {static_mesh.get_name()}")
        # unreal.log(f"Static Mesh Triangles: {static_mesh_tri_count}")
        # unreal.log(f"Static Mesh Reductions: {static_mesh_reductions}")
        # unreal.log("----------------------------------------")
        try:
            lod_data = (static_mesh.get_name(), static_mesh_tri_count[1])
        except:
            pass
        static_mesh_lod_data.append(lod_data)
    
    return static_mesh_lod_data



def get_static_mesh_instance_counts():
    EAS = unreal.EditorActorSubsystem()
    level_actors = EAS.get_all_level_actors()

    static_mesh_actors = []
    static_mesh_actor_counts = []

    for level_actor in level_actors:
        if level_actor.get_class().get_name() == 'StaticMeshActor':
            static_mesh_component = level_actor.static_mesh_component  # # static_mesh_component is a property
            static_mesh = static_mesh_component.static_mesh  # static_mesh is a property
            static_mesh_actors.append(static_mesh.get_name())

    processed_actors = []
    for static_mesh_actor in static_mesh_actors:
        if static_mesh_actor not in processed_actors:
            actor_counts = (static_mesh_actor, static_mesh_actors.count(static_mesh_actor))
            static_mesh_actor_counts.append(actor_counts)
            processed_actors.append(static_mesh_actor)

    static_mesh_actor_counts.sort(key= lambda a: a[1], reverse=True)

    # for item in static_mesh_actor_counts:
    #     unreal.log(item)

    load_data = get_static_mesh_lod_data()

    # for item in load_data:
    #     unreal.log(item)

    aggregate_tri_counts = []
    for i in range(len(static_mesh_actor_counts)):
        for j in range(len(load_data)):
            if static_mesh_actor_counts[i][0] == load_data[j][0]:
                aggregate_tri_count = (static_mesh_actor_counts[i][0], static_mesh_actor_counts[i][1] * load_data[j][1])
                aggregate_tri_counts.append(aggregate_tri_count)

    aggregate_tri_counts.sort(key=lambda a: a[1], reverse=True)
    for item in aggregate_tri_counts:
        unreal.log(item)



get_static_mesh_instance_counts()