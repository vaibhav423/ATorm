from dataclasses import dataclass
from typing import List

@dataclass
class Element:
    atomic_number: int
    symbol: str
    name: str
    atomic_mass: float
    category: str = "Unknown"

ELEMENTS = {
    1: Element(1, "H", "Hydrogen", 1.008, "Nonmetal"),
    2: Element(2, "He", "Helium", 4.003, "Noble Gas"),
    
    3: Element(3, "Li", "Lithium", 6.941, "Alkali Metal"),
    4: Element(4, "Be", "Beryllium", 9.012, "Alkaline Earth"),
    5: Element(5, "B", "Boron", 10.811, "Metalloid"),
    6: Element(6, "C", "Carbon", 12.011, "Nonmetal"),
    7: Element(7, "N", "Nitrogen", 14.007, "Nonmetal"),
    8: Element(8, "O", "Oxygen", 15.999, "Nonmetal"),
    9: Element(9, "F", "Fluorine", 18.998, "Halogen"),
    10: Element(10, "Ne", "Neon", 20.180, "Noble Gas"),
    
    11: Element(11, "Na", "Sodium", 22.990, "Alkali Metal"),
    12: Element(12, "Mg", "Magnesium", 24.305, "Alkaline Earth"),
    13: Element(13, "Al", "Aluminum", 26.982, "Metal"),
    14: Element(14, "Si", "Silicon", 28.086, "Metalloid"),
    15: Element(15, "P", "Phosphorus", 30.974, "Nonmetal"),
    16: Element(16, "S", "Sulfur", 32.065, "Nonmetal"),
    17: Element(17, "Cl", "Chlorine", 35.453, "Halogen"),
    18: Element(18, "Ar", "Argon", 39.948, "Noble Gas"),
    
    19: Element(19, "K", "Potassium", 39.098, "Alkali Metal"),
    20: Element(20, "Ca", "Calcium", 40.078, "Alkaline Earth"),
    21: Element(21, "Sc", "Scandium", 44.956, "Transition Metal"),
    22: Element(22, "Ti", "Titanium", 47.867, "Transition Metal"),
    23: Element(23, "V", "Vanadium", 50.942, "Transition Metal"),
    24: Element(24, "Cr", "Chromium", 51.996, "Transition Metal"),
    25: Element(25, "Mn", "Manganese", 54.938, "Transition Metal"),
    26: Element(26, "Fe", "Iron", 55.845, "Transition Metal"),
    27: Element(27, "Co", "Cobalt", 58.933, "Transition Metal"),
    28: Element(28, "Ni", "Nickel", 58.693, "Transition Metal"),
    29: Element(29, "Cu", "Copper", 63.546, "Transition Metal"),
    30: Element(30, "Zn", "Zinc", 65.38, "Transition Metal"),
    31: Element(31, "Ga", "Gallium", 69.723, "Metal"),
    32: Element(32, "Ge", "Germanium", 72.630, "Metalloid"),
    33: Element(33, "As", "Arsenic", 74.922, "Metalloid"),
    34: Element(34, "Se", "Selenium", 78.971, "Nonmetal"),
    35: Element(35, "Br", "Bromine", 79.904, "Halogen"),
    36: Element(36, "Kr", "Krypton", 83.798, "Noble Gas"),
    
    37: Element(37, "Rb", "Rubidium", 85.468, "Alkali Metal"),
    38: Element(38, "Sr", "Strontium", 87.62, "Alkaline Earth"),
    39: Element(39, "Y", "Yttrium", 88.906, "Transition Metal"),
    40: Element(40, "Zr", "Zirconium", 91.224, "Transition Metal"),
    41: Element(41, "Nb", "Niobium", 92.906, "Transition Metal"),
    42: Element(42, "Mo", "Molybdenum", 95.95, "Transition Metal"),
    43: Element(43, "Tc", "Technetium", 98.907, "Transition Metal"),
    44: Element(44, "Ru", "Ruthenium", 101.07, "Transition Metal"),
    45: Element(45, "Rh", "Rhodium", 102.906, "Transition Metal"),
    46: Element(46, "Pd", "Palladium", 106.42, "Transition Metal"),
    47: Element(47, "Ag", "Silver", 107.868, "Transition Metal"),
    48: Element(48, "Cd", "Cadmium", 112.414, "Transition Metal"),
    49: Element(49, "In", "Indium", 114.818, "Metal"),
    50: Element(50, "Sn", "Tin", 118.710, "Metal"),
    51: Element(51, "Sb", "Antimony", 121.760, "Metalloid"),
    52: Element(52, "Te", "Tellurium", 127.60, "Metalloid"),
    53: Element(53, "I", "Iodine", 126.904, "Halogen"),
    54: Element(54, "Xe", "Xenon", 131.294, "Noble Gas"),
    
    55: Element(55, "Cs", "Cesium", 132.905, "Alkali Metal"),
    56: Element(56, "Ba", "Barium", 137.327, "Alkaline Earth"),
    57: Element(57, "La", "Lanthanum", 138.905, "Lanthanide"),
    58: Element(58, "Ce", "Cerium", 140.116, "Lanthanide"),
    59: Element(59, "Pr", "Praseodymium", 140.908, "Lanthanide"),
    60: Element(60, "Nd", "Neodymium", 144.242, "Lanthanide"),
    61: Element(61, "Pm", "Promethium", 145.0, "Lanthanide"),
    62: Element(62, "Sm", "Samarium", 150.36, "Lanthanide"),
    63: Element(63, "Eu", "Europium", 151.964, "Lanthanide"),
    64: Element(64, "Gd", "Gadolinium", 157.25, "Lanthanide"),
    65: Element(65, "Tb", "Terbium", 158.925, "Lanthanide"),
    66: Element(66, "Dy", "Dysprosium", 162.500, "Lanthanide"),
    67: Element(67, "Ho", "Holmium", 164.930, "Lanthanide"),
    68: Element(68, "Er", "Erbium", 167.259, "Lanthanide"),
    69: Element(69, "Tm", "Thulium", 168.934, "Lanthanide"),
    70: Element(70, "Yb", "Ytterbium", 173.045, "Lanthanide"),
    71: Element(71, "Lu", "Lutetium", 174.967, "Lanthanide"),
    72: Element(72, "Hf", "Hafnium", 178.49, "Transition Metal"),
    73: Element(73, "Ta", "Tantalum", 180.948, "Transition Metal"),
    74: Element(74, "W", "Tungsten", 183.84, "Transition Metal"),
    75: Element(75, "Re", "Rhenium", 186.207, "Transition Metal"),
    76: Element(76, "Os", "Osmium", 190.23, "Transition Metal"),
    77: Element(77, "Ir", "Iridium", 192.217, "Transition Metal"),
    78: Element(78, "Pt", "Platinum", 195.084, "Transition Metal"),
    79: Element(79, "Au", "Gold", 196.967, "Transition Metal"),
    80: Element(80, "Hg", "Mercury", 200.592, "Transition Metal"),
    81: Element(81, "Tl", "Thallium", 204.383, "Metal"),
    82: Element(82, "Pb", "Lead", 207.2, "Metal"),
    83: Element(83, "Bi", "Bismuth", 208.980, "Metal"),
    84: Element(84, "Po", "Polonium", 209.0, "Metalloid"),
    85: Element(85, "At", "Astatine", 210.0, "Halogen"),
    86: Element(86, "Rn", "Radon", 222.0, "Noble Gas"),
    
    87: Element(87, "Fr", "Francium", 223.0, "Alkali Metal"),
    88: Element(88, "Ra", "Radium", 226.0, "Alkaline Earth"),
    89: Element(89, "Ac", "Actinium", 227.0, "Actinide"),
    90: Element(90, "Th", "Thorium", 232.038, "Actinide"),
    91: Element(91, "Pa", "Protactinium", 231.036, "Actinide"),
    92: Element(92, "U", "Uranium", 238.029, "Actinide"),
    93: Element(93, "Np", "Neptunium", 237.0, "Actinide"),
    94: Element(94, "Pu", "Plutonium", 244.0, "Actinide"),
    95: Element(95, "Am", "Americium", 243.0, "Actinide"),
    96: Element(96, "Cm", "Curium", 247.0, "Actinide"),
    97: Element(97, "Bk", "Berkelium", 247.0, "Actinide"),
    98: Element(98, "Cf", "Californium", 251.0, "Actinide"),
    99: Element(99, "Es", "Einsteinium", 252.0, "Actinide"),
    100: Element(100, "Fm", "Fermium", 257.0, "Actinide"),
    101: Element(101, "Md", "Mendelevium", 258.0, "Actinide"),
    102: Element(102, "No", "Nobelium", 259.0, "Actinide"),
    103: Element(103, "Lr", "Lawrencium", 266.0, "Actinide"),
    104: Element(104, "Rf", "Rutherfordium", 267.0, "Transition Metal"),
    105: Element(105, "Db", "Dubnium", 268.0, "Transition Metal"),
    106: Element(106, "Sg", "Seaborgium", 269.0, "Transition Metal"),
    107: Element(107, "Bh", "Bohrium", 270.0, "Transition Metal"),
    108: Element(108, "Hs", "Hassium", 269.0, "Transition Metal"),
    109: Element(109, "Mt", "Meitnerium", 278.0, "Transition Metal"),
    110: Element(110, "Ds", "Darmstadtium", 281.0, "Transition Metal"),
    111: Element(111, "Rg", "Roentgenium", 282.0, "Transition Metal"),
    112: Element(112, "Cn", "Copernicium", 285.0, "Transition Metal"),
    113: Element(113, "Nh", "Nihonium", 286.0, "Metal"),
    114: Element(114, "Fl", "Flerovium", 289.0, "Metal"),
    115: Element(115, "Mc", "Moscovium", 290.0, "Metal"),
    116: Element(116, "Lv", "Livermorium", 293.0, "Metal"),
    117: Element(117, "Ts", "Tennessine", 294.0, "Halogen"),
    118: Element(118, "Og", "Oganesson", 294.0, "Noble Gas"),
}

def get_element(atomic_number: int) -> Element:
    if atomic_number in ELEMENTS:
        return ELEMENTS[atomic_number]
    else:
        return Element(
            atomic_number=atomic_number,
            symbol=f"E{atomic_number}",
            name=f"Element-{atomic_number}",
            atomic_mass=atomic_number * 2.0,
            category="Unknown"
        )

def get_electron_shells(atomic_number: int) -> List[int]:
    max_electrons = [2, 8, 18, 32, 50, 72, 98]
    shells = []
    remaining_electrons = atomic_number
    
    for max_in_shell in max_electrons:
        if remaining_electrons <= 0:
            break
        
        electrons_in_shell = min(remaining_electrons, max_in_shell)
        shells.append(electrons_in_shell)
        remaining_electrons -= electrons_in_shell
    
    if remaining_electrons > 0:
        shells.append(remaining_electrons)
    
    return shells

def get_electron_configuration(atomic_number: int) -> str:
    if atomic_number <= 0:
        return ""
    
    orbital_order = [
        ("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2),
        ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10), ("5p", 6), ("6s", 2),
        ("4f", 14), ("5d", 10), ("6p", 6), ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
    ]
    
    configuration = []
    remaining_electrons = atomic_number
    
    for orbital, max_electrons in orbital_order:
        if remaining_electrons <= 0:
            break
        
        electrons_in_orbital = min(remaining_electrons, max_electrons)
        
        superscript_map = {
            1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹", 10: "¹⁰",
            11: "¹¹", 12: "¹²", 13: "¹³", 14: "¹⁴"
        }
        
        superscript = superscript_map.get(electrons_in_orbital, str(electrons_in_orbital))
        configuration.append(f"{orbital}{superscript}")
        remaining_electrons -= electrons_in_orbital
    
    return " ".join(configuration)

def get_noble_gas_notation(atomic_number: int) -> str:
    if atomic_number <= 2:
        return get_electron_configuration(atomic_number)
    
    noble_gases = {
        2: ("He", 2),
        10: ("Ne", 10),
        18: ("Ar", 18),
        36: ("Kr", 36),
        54: ("Xe", 54),
        86: ("Rn", 86),
    }
    
    core_symbol = ""
    core_electrons = 0
    
    for ng_atomic_num, (symbol, electrons) in noble_gases.items():
        if ng_atomic_num < atomic_number:
            core_symbol = symbol
            core_electrons = electrons
    
    if core_electrons == 0:
        return get_electron_configuration(atomic_number)
    
    remaining_electrons = atomic_number - core_electrons
    if remaining_electrons > 0:
        outer_config = get_electron_configuration(remaining_electrons)
        return f"[{core_symbol}] {outer_config}"
    else:
        return f"[{core_symbol}]"

def get_valence_electrons(atomic_number: int) -> int:
    shells = get_electron_shells(atomic_number)
    return shells[-1] if shells else 0

def get_element_period(atomic_number: int) -> int:
    if atomic_number <= 2:
        return 1
    elif atomic_number <= 10:
        return 2
    elif atomic_number <= 18:
        return 3
    elif atomic_number <= 36:
        return 4
    elif atomic_number <= 54:
        return 5
    elif atomic_number <= 86:
        return 6
    elif atomic_number <= 118:
        return 7
    else:
        return 8

def get_element_group(atomic_number: int) -> int:
    if atomic_number == 1:
        return 1
    elif atomic_number == 2:
        return 18
    elif atomic_number in [3, 11, 19, 37, 55, 87]:
        return 1
    elif atomic_number in [4, 12, 20, 38, 56, 88]:
        return 2
    elif atomic_number in [5, 13, 31, 49, 81, 113]:
        return 13
    elif atomic_number in [6, 14, 32, 50, 82, 114]:
        return 14
    elif atomic_number in [7, 15, 33, 51, 83, 115]:
        return 15
    elif atomic_number in [8, 16, 34, 52, 84, 116]:
        return 16
    elif atomic_number in [9, 17, 35, 53, 85, 117]:
        return 17
    elif atomic_number in [10, 18, 36, 54, 86, 118]:
        return 18
    else:
        return 0

def get_orbital_diagram(atomic_number: int) -> str:
    if atomic_number <= 0:
        return ""
    
    orbitals = {
        "1s": 0, "2s": 0, "2p": 0, "3s": 0, "3p": 0
    }
    
    remaining = atomic_number
    
    if remaining > 0:
        orbitals["1s"] = min(2, remaining)
        remaining -= orbitals["1s"]
    
    if remaining > 0:
        orbitals["2s"] = min(2, remaining)
        remaining -= orbitals["2s"]
    
    if remaining > 0:
        orbitals["2p"] = min(6, remaining)
        remaining -= orbitals["2p"]
    
    if remaining > 0:
        orbitals["3s"] = min(2, remaining)
        remaining -= orbitals["3s"]
    
    if remaining > 0:
        orbitals["3p"] = min(6, remaining)
        remaining -= orbitals["3p"]
    
    diagram_parts = []
    for orbital, electrons in orbitals.items():
        if electrons > 0:
            arrows = "↑" * min(electrons, 1)
            if electrons > 1:
                arrows += "↓" * min(electrons - 1, 1)
            diagram_parts.append(f"{orbital}:{arrows}")
    
    return " ".join(diagram_parts) if diagram_parts else "No electrons"
