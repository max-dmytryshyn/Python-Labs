from saws_and_saws_parameters.mechanical_saw import MechanicalSaw
from saws_and_saws_parameters.material_to_saw import MaterialToSaw
from saws_and_saws_parameters.saw_material import SawMaterial
from person import Person


class TwoManSaw(MechanicalSaw):
    def __init__(self, made_of_material = SawMaterial(), user = Person(), length_in_cm = 100.0,
                 tooth_size_in_mm = 10.5, second_user = Person()):
        super().__init__(made_of_material, user, length_in_cm, tooth_size_in_mm)
        self._material_to_saw = MaterialToSaw.WOOD
        self.__second_user = second_user

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Second user: {self.__second_user}"

    @property
    def second_user(self):
        return self.__second_user

    def set_second_user(self, second_user: Person):
        self.__second_user = second_user
