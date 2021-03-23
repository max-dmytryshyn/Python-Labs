from saws_and_saws_parameters import saw
from saws_and_saws_parameters.drive_type import DriveType
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class MechanicalSaw(saw.Saw):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0, tooth_size_in_mm = 10.5):
        super().__init__(made_of_material, user, length_in_cm)
        self._drive_type = DriveType.MECHANICAL
        self._tooth_size_in_mm = tooth_size_in_mm

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Tooth size: {self._tooth_size_in_mm} mm"

    @property
    def tooth_size_in_mm(self):
        return self._tooth_size_in_mm
