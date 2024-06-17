import unreal

@unreal.uclass()
class PyScriptToolMenu(unreal.ToolMenuEntryScript):
    script_name = "ScriptName"
    @unreal.ufunction(override=True)
    def execute(self, context):
        unreal.PythonScriptLibrary.execute_python_command(self.script_name)

@unreal.uclass()
class RenameMenu(PyScriptToolMenu):
    script_name = "RenamingTool.py"


def add_to_right_mouse_menu(added_section_name: str, tool_name: str, tool_tip: str, tool_class: PyScriptToolMenu):
    edit_menu = unreal.ToolMenus.get().find_menu("ContentBrowser.AssetContextMenu")
    edit_menu.add_section(
        section_name = added_section_name,
        label=added_section_name,
        insert_name="CommonAssetActions",
        insert_type=unreal.ToolMenuInsertType.BEFORE
    )
    
    py_menu = tool_class
    py_menu.init_entry(
        owner_name=edit_menu.menu_name,
        menu=edit_menu.menu_name,
        section=added_section_name,
        name=tool_name,
        label=tool_name,
        tool_tip=tool_tip
    )
    py_menu.register_menu_entry()

def add_to_tools_menu(added_section_name: str, tool_name: str, tool_tip: str, tool_class: PyScriptToolMenu):
    edit_menu = unreal.ToolMenus.get().find_menu("LevelEditor.MainMenu.Tools")
    edit_menu.add_section(
        section_name = added_section_name,
        label=added_section_name,
        insert_name="ExperimentalTabSpawners",
        insert_type=unreal.ToolMenuInsertType.BEFORE
    )

    py_menu = tool_class
    py_menu.init_entry(
        owner_name=edit_menu.menu_name,
        menu=edit_menu.menu_name,
        section=added_section_name,
        name=tool_name,
        label=tool_name,
        tool_tip=tool_tip
    )
    py_menu.register_menu_entry()


add_to_right_mouse_menu("Python Tools", "Renaming Tool", "RENAME IT", RenameMenu())
add_to_tools_menu("Python Tools", "Renaming Tool", "RENAME IT", RenameMenu())