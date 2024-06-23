import unreal

"""
Script will add menus each time the Project starts

"""

@unreal.uclass()
class PyScript(unreal.ToolMenuEntryScript): # Class for all scripts
    menu_section_name = "Python Tools"
    script_name = "ScriptName"
    tool_name = "ToolName"
    tool_tip = "tip"
    icon = "BreadcrumbTrail.Delimiter"
    
    @unreal.ufunction(override=True)
    def execute(self, context):
        unreal.PythonScriptLibrary.execute_python_command(self.script_name)
    
    def set_icon(self):
        self.data.set_editor_property(name="icon", value=unreal.ScriptSlateIcon("EditorStyle", self.icon))

@unreal.uclass()
class RenameMenu(PyScript):
    script_name = "renaming_tool.py"
    tool_name = "Renaming Tool"
    tool_tip = "Batch Renaming"
    icon = "ContentBrowser.AssetActions.Rename"

@unreal.uclass()
class ArrayPlacing(PyScript):
    script_name = "array_placing.py"
    tool_name = "Array Placing"
    tool_tip = "Place static meshes in line"
    icon = "Kismet.VariableList.MapValueTypeIcon"


def add_script_to_right_mouse_menu(script_class: PyScript):
    edit_menu = unreal.ToolMenus.get().find_menu("ContentBrowser.AssetContextMenu")
    edit_menu.add_section(
        section_name = script_class.menu_section_name,
        label=script_class.menu_section_name,
        insert_name="CommonAssetActions",
        insert_type=unreal.ToolMenuInsertType.AFTER
    )
    
    py_menu = script_class
    py_menu.set_icon()

    py_menu.init_entry(
        owner_name=edit_menu.menu_name,
        menu=edit_menu.menu_name,
        section=script_class.menu_section_name,
        name=script_class.tool_name,
        label=script_class.tool_name,
        tool_tip=script_class.tool_tip
    )

    py_menu.register_menu_entry()

def add_script_to_tools_menu(script_class: PyScript):
    edit_menu = unreal.ToolMenus.get().find_menu("LevelEditor.MainMenu.Tools")
    edit_menu.add_section(
        section_name = script_class.menu_section_name,
        label=script_class.menu_section_name,
        insert_name="ExperimentalTabSpawners",
        insert_type=unreal.ToolMenuInsertType.BEFORE
    )

    py_menu = script_class
    py_menu.set_icon()

    py_menu.init_entry(
        owner_name=edit_menu.menu_name,
        menu=edit_menu.menu_name,
        section=script_class.menu_section_name,
        name=script_class.tool_name,
        label=script_class.tool_name,
        tool_tip=script_class.tool_tip
    )

    py_menu.register_menu_entry()
            
def main():
    add_script_to_right_mouse_menu(RenameMenu())
    add_script_to_tools_menu(RenameMenu())
    add_script_to_right_mouse_menu(ArrayPlacing())
    add_script_to_tools_menu(ArrayPlacing())

if __name__ == "__main__":
    main()
