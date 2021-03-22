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
from colour_print import colour_print


def print_saws(saws = []):
    for saw in saws:
        print(saw)
        print("-------------------------------")


def test_search_by_drive_type(saws_manager = SawManager()):
    mechanical_saws = saws_manager.search_by_drive_type(DriveType.MECHANICAL)
    colour_print("Saws with mechanical drive:", "OKGREEN")
    print_saws(mechanical_saws)
    electric_saws = saws_manager.search_by_drive_type(DriveType.ELECTRIC)
    colour_print("Saws with electric drive:", "OKGREEN")
    print_saws(electric_saws)
    saws_with_internal_combustion_engine = saws_manager.search_by_drive_type(DriveType.INTERNAL_COMBUSTION_ENGINE)
    colour_print("Saws with internal combustion engine:", "OKGREEN")
    print_saws(saws_with_internal_combustion_engine)


def test_search_by_made_of_material(saws_manager = SawManager()):
    saws_with_steel_blade_and_plastic_handle = saws_manager.search_by_made_of_material(
                                               SawMaterial(blade_material = "steel", handle_material = "plastic")
                                               )
    colour_print("Saws with steel blade and plastic handle:", "OKGREEN")
    print_saws(saws_with_steel_blade_and_plastic_handle)


def test_sort_by_length(saws_manager = SawManager()):
    sorted_saws = saws_manager.saws
    saws_manager.sort_by_length(sorted_saws, SortOrder.ASC)
    colour_print("Saws sorted by length in ascending order:", "OKGREEN")
    print_saws(sorted_saws)
    saws_manager.sort_by_length(sorted_saws, SortOrder.DESC)
    colour_print("Saws sorted by length in descending order:", "OKGREEN")
    print_saws(sorted_saws)


if __name__ == '__main__':
    jigsaw = Jigsaw(made_of_material = SawMaterial(blade_material = "copper", handle_material = "plastic"),
                    user = Person(name = "Max", age = 17), length_in_cm = 14, operating_voltage = 240)
    chain_saw = Chainsaw(made_of_material = SawMaterial(blade_material = "steel", handle_material = "plastic"),
                         user = Person(name = "Danylo", age = 19), length_in_cm = 30, tank_volume = 5)
    ripping_saw = RippingSaw(made_of_material = SawMaterial(blade_material = "lead", handle_material = "wood"),
                             user = Person(name = "La Kosta", age = 18), length_in_cm = 16, tooth_size_in_mm = 5)
    hacksaw = Hacksaw(made_of_material = SawMaterial(blade_material = "steel", handle_material = "plastic"),
                      user = Person(name = "Dmytro", age = 13), length_in_cm = 12, blade_manufacturer = "Blades CO")
    fretsaw = Fretsaw(made_of_material = SawMaterial(blade_material = "aluminium", handle_material = "wood"),
                      user = Person(name = "Ivan", age = 18), length_in_cm = 13, arc_length_in_cm = 20.5)
    two_man_saw = TwoManSaw(made_of_material = SawMaterial(blade_material = "steel", handle_material = "wood"),
                            user = Person(name = "Max", age = 17), length_in_cm = 40,
                            second_user = Person(name = "Andrew", age = 18))
    saw_manager = SawManager()
    saw_manager.add_saw(jigsaw)
    saw_manager.add_saw(chain_saw)
    saw_manager.add_saw(ripping_saw)
    saw_manager.add_saw(hacksaw)
    saw_manager.add_saw(fretsaw)
    saw_manager.add_saw(two_man_saw)
    colour_print("Saws in saw manager:", "OKGREEN")
    print_saws(saw_manager.saws)
    test_search_by_drive_type(saw_manager)
    test_search_by_made_of_material(saw_manager)
    test_sort_by_length(saw_manager)





