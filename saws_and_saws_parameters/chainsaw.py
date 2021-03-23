from saws_and_saws_parameters import saw
from saws_and_saws_parameters.material_to_saw import MaterialToSaw
from saws_and_saws_parameters.drive_type import DriveType
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class Chainsaw(saw.Saw):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0, tank_volume = 3):
        super().__init__(made_of_material, user, length_in_cm)
        self._material_to_saw = MaterialToSaw.WOOD
        self._drive_type = DriveType.INTERNAL_COMBUSTION_ENGINE
        self.__tank_volume = tank_volume

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Tank volume: {self.__tank_volume} l"

    @property
    def tank_volume(self):
        return self.__tank_volume
