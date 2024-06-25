import unreal
import shutil
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import startup

"""
Execute this file to setup

"""

def copy_scripts_to_project_dir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir = unreal.Paths.project_dir() + "Content/"
    new_folder = "UE_PythonTools"

    if unreal.Paths.directory_exists(project_dir + new_folder):
        return None
    
    shutil.copytree(src = current_dir, dst = project_dir + new_folder)

def add_startup_script_to_config():
    section = "[/Script/PythonScriptPlugin.PythonScriptPluginSettings]"
    startup_path = unreal.Paths.project_dir() + "Content/UE_PythonTools/startup.py"
    config_path = unreal.Paths.project_config_dir() + "DefaultEngine.ini"
    startup_scripts = "+StartupScripts=startup.py"
    additional_paths = f"+AdditionalPaths=(Path=\'{startup_path}\')"

    with open(config_path, mode="r") as config:
        config_str = config.read()
        if (section in config_str) and (startup_scripts in config_str) and (additional_paths in config_str):
            return None
        else:
            config_str_new = config_str.replace(section, section + "\n" + startup_scripts + "\n" + additional_paths)
            if config_str_new == config_str:
                config_str_new = config_str + "\n" + section + "\n" + startup_scripts + "\n" + additional_paths

            with open(config_path, mode="w") as config:
                config.write(config_str_new)

def main():
    copy_scripts_to_project_dir()
    add_startup_script_to_config()
    startup.main()
    print("Setup is over. Check Tools menu and Content/UE_PythonTools Folder.")

if __name__ == "__main__":
    main()