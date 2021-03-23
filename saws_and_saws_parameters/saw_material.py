class SawMaterial:
    def __init__(self, handle_material="unknown", blade_material="unknown"):
        self.__handle_material = handle_material
        self.__blade_material = blade_material

    @property
    def handle_material(self):
        return self.__handle_material

    @property
    def blade_material(self):
        return self.__blade_material

    def __eq__(self, other):
        is_handle_materials_equal = self.__handle_material == other.__handle_material
        is_blade_materials_equal = self.__blade_material == other.__blade_material
        return is_handle_materials_equal and is_blade_materials_equal

    def __str__(self):
        return f"Handle material: {self.__handle_material} \n" \
               f"Blade material: {self.__blade_material}"

