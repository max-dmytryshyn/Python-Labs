from saws_and_saws_parameters import saw
from saws_and_saws_parameters.material_to_saw import MaterialToSaw
from saws_and_saws_parameters.drive_type import DriveType
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class Jigsaw(saw.Saw):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0, operating_voltage = 220):
        super().__init__(made_of_material, user, length_in_cm)
        self._material_to_saw = MaterialToSaw.WOOD
        self._drive_type = DriveType.ELECTRIC
        self.__operating_voltage = operating_voltage

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Operating voltage: {self.__operating_voltage} V"

    @property
    def operating_voltage(self):
        return self.__operating_voltage
