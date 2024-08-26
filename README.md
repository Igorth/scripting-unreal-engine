# Unreal Engine Python Utility Scripts

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Unreal Engine](https://img.shields.io/badge/Unreal%20Engine-5-blue.svg)

This repository contains a collection of Python scripts for automating various tasks in Unreal Engine 5. These scripts utilize the Unreal Python API to interact with assets, actors, and other elements within the Unreal Editor, providing a powerful toolkit for developers and artists.

## Resources
[Utilizing Python for Editor Scripting in Unreal Engine](https://dev.epicgames.com/community/learning/courses/wk4/utilizing-python-for-editor-scripting-in-unreal-engine/qOm5/utilizing-python-for-editor-scripting-in-unreal-engine-overview)
## Scripts Overview

### 1. `list_asset_paths()`
- **Description**: Retrieves the paths for every asset in the `/Game` directory.
- **Usage**: Use this function to get a list of all asset paths within the specified directory.

### 2. `get_select_content_browser()`
- **Description**: Logs the names of assets selected in the Content Browser.
- **Usage**: This function is helpful for identifying and logging selected assets.

### 3. `get_all_actors()`
- **Description**: Logs the names of all actors currently present in the level.
- **Usage**: Use this to get an overview of all actors within the current level.

### 4. `get_selected_actors()`
- **Description**: Logs the names of actors selected in the level.
- **Usage**: Useful for logging or processing selected actors in the level.

### 5. `get_asset_class(class_type)`
- **Description**: Retrieves all assets of a specified class type.
- **Usage**: Pass the desired class type (e.g., `StaticMesh`) to get a list of assets of that type.

### 6. `get_static_mesh_data()`
- **Description**: Retrieves and logs LOD group information for all static meshes.
- **Usage**: Use this to analyze and modify the LOD group settings for static meshes.

### 7. `get_textures_twod()`
- **Description**: Logs sRGB settings for all `Texture2D` assets.
- **Usage**: This script is useful for verifying or modifying texture settings.

### 8. `get_static_mesh_lod_data()`
- **Description**: Retrieves LOD (Level of Detail) data and triangle counts for static meshes.
- **Usage**: This function helps in analyzing the LOD structure and complexity of static meshes.

### 9. `get_static_mesh_instance_counts()`
- **Description**: Logs the number of instances for each static mesh in the level, as well as the aggregate triangle counts.
- **Usage**: Useful for optimizing levels by understanding static mesh usage and impact.

### 10. `return_material_information_smc()`
- **Description**: Applies a specified material to every element of static mesh actors in the level.
- **Usage**: This script is beneficial for batch processing material assignments in the level.

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Igorth/scripting-unreal-engine
    ```

2. **Add Scripts to Unreal Engine**:
    - Place the Python scripts in your Unreal Engine project's `/Scripts` directory or any other appropriate folder.

3. **Run Scripts**:
    - Execute the scripts within the Unreal Engine Editor by accessing the Python editor or by scripting automation tasks.

## Prerequisites

- **Unreal Engine 5**: Ensure Unreal Engine 5 is installed and configured.
- **Python Integration**: Python must be enabled and set up in Unreal Engine.
