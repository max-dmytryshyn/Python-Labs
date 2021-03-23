import unittest
from saws_and_saws_parameters.saw_manager import SawManager, SortOrder
from saws_and_saws_parameters.jigsaw import Jigsaw
from saws_and_saws_parameters.chainsaw import Chainsaw
from saws_and_saws_parameters.ripping_saw import RippingSaw
from saws_and_saws_parameters.hacksaw import Hacksaw
from saws_and_saws_parameters.fretsaw import Fretsaw
from saws_and_saws_parameters.two_man_saw import TwoManSaw
from saws_and_saws_parameters.saw_material import SawMaterial
from saws_and_saws_parameters.drive_type import DriveType
from person import Person


class TestSawManager(unittest.TestCase):

    def setUp(self):
        self.jigsaw = Jigsaw(made_of_material=SawMaterial(blade_material="copper", handle_material="plastic"),
                             user=Person(name="Max", age=17), length_in_cm=14, operating_voltage=240)
        self.chain_saw = Chainsaw(made_of_material=SawMaterial(blade_material="steel", handle_material="plastic"),
                                  user=Person(name="Danylo", age=19), length_in_cm=30, tank_volume=5)
        self.ripping_saw = RippingSaw(made_of_material=SawMaterial(blade_material="lead", handle_material="wood"),
                                      user=Person(name="La Kosta", age=18), length_in_cm=16, tooth_size_in_mm=5)
        self.hacksaw = Hacksaw(made_of_material=SawMaterial(blade_material="steel", handle_material="plastic"),
                               user=Person(name="Dmytro", age=13), length_in_cm=12, blade_manufacturer="Blades CO")
        self.fretsaw = Fretsaw(made_of_material=SawMaterial(blade_material="aluminium", handle_material="wood"),
                               user=Person(name="Ivan", age=18), length_in_cm=13, arc_length_in_cm=20.5)
        self.two_man_saw = TwoManSaw(made_of_material=SawMaterial(blade_material="steel", handle_material="wood"),
                                     user=Person(name="Max", age=17), length_in_cm=40,
                                     second_user=Person(name="Andrew", age=18))
        self.mechanical_saws = [self.ripping_saw, self.hacksaw, self.fretsaw, self.two_man_saw]
        self.electric_saws = [self.jigsaw]
        self.saws_with_internal_combustion_engine = [self.chain_saw]
        self.saws_with_steel_blade_and_plastic_handle = [self.chain_saw, self.hacksaw]
        self.saws_in_asc_order = [self.hacksaw, self.fretsaw, self.jigsaw, self.ripping_saw, self.chain_saw, self.two_man_saw]
        self.saws_in_desc_order = list(reversed(self.saws_in_asc_order))
        self.saw_manager = SawManager()
        self.saw_manager.add_saw(self.jigsaw)
        self.saw_manager.add_saw(self.chain_saw)
        self.saw_manager.add_saw(self.ripping_saw)
        self.saw_manager.add_saw(self.hacksaw)
        self.saw_manager.add_saw(self.fretsaw)
        self.saw_manager.add_saw(self.two_man_saw)

    def test_search_by_drive_type(self):
        self.assertListEqual(self.saw_manager.search_by_drive_type(DriveType.MECHANICAL), self.mechanical_saws)
        self.assertListEqual(self.saw_manager.search_by_drive_type(DriveType.ELECTRIC), self.electric_saws)
        self.assertListEqual(self.saw_manager.search_by_drive_type(DriveType.INTERNAL_COMBUSTION_ENGINE),
                             self.saws_with_internal_combustion_engine)

    def test_search_by_made_of_material(self):
        self.assertListEqual(self.saw_manager.search_by_made_of_material(
                             SawMaterial(blade_material = "steel", handle_material = "plastic")),
                             self.saws_with_steel_blade_and_plastic_handle)

    def test_sort_by_length(self):
        self.assertListEqual(self.saw_manager.sort_by_length(self.saw_manager.saws, SortOrder.ASC),
                             self.saws_in_asc_order)
        self.assertListEqual(self.saw_manager.sort_by_length(self.saw_manager.saws, SortOrder.DESC),
                             self.saws_in_desc_order)


if __name__ == "__main__":
    unittest.main()
