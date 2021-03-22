from abc import ABC
from saws_and_saws_parameters.material_to_saw import MaterialToSaw
from saws_and_saws_parameters.drive_type import DriveType
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class Saw(ABC):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0):
        self._material_to_saw = MaterialToSaw.WOOD
        self._drive_type = DriveType.MECHANICAL
        self._made_of_material = made_of_material
        self._user = user
        self._length_in_cm = length_in_cm

    def __str__(self):
        return f"Material to saw: {self._material_to_saw.name}\n"\
               f"Drive type: {self._drive_type.name}\n"\
               f"{self._made_of_material}\n" \
               f"User: {self._user}\n"\
               f"Length: {self._length_in_cm} cm"

    @property
    def material_to_saw(self):
        return self._material_to_saw

    @property
    def drive_type(self):
        return self._drive_type

    @property
    def made_of_material(self):
        return self._made_of_material

    @property
    def user(self):
        return self._user

    @property
    def length_in_cm(self):
        return self._length_in_cm

    def set_user(self, user: Person):
        self._user = user
