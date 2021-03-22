from saws_and_saws_parameters.mechanical_saw import MechanicalSaw
from saws_and_saws_parameters.material_to_saw import MaterialToSaw
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class Fretsaw(MechanicalSaw):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0,
                 tooth_size_in_mm = 10.5, blade_manufacturer="unknown", arc_length_in_cm=10.0):
        super().__init__(made_of_material, user, length_in_cm, tooth_size_in_mm)
        self._material_to_saw = MaterialToSaw.WOOD
        self.__blade_manufacturer = blade_manufacturer
        self.__arc_length_in_cm = arc_length_in_cm

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Blade manufacturer: {self.__blade_manufacturer} \n" \
               f"Arc length: {self.__arc_length_in_cm} cm"

    @property
    def blade_manufacturer(self):
        return self.__blade_manufacturer

    @property
    def arc_length_in_cm(self):
        return self.__arc_length_in_cm

    def change_blade(self, tooth_size_in_mm=10.5, blade_manufacturer="unknown"):
        self._tooth_size_in_mm = tooth_size_in_mm
        self.__blade_manufacturer = blade_manufacturer
