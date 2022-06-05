# Empirical formula approximator
import periodictable as pt

def confirm_valid_element(formula: str) -> bool:
    element_list = [str(element) for element in pt.elements]
    return formula in element_list

def get_element_input():
    print('Please input element and mass data in the form, "{element symbol} {mass in grams (g)}":')
    output_list = []
    n = 1

    while (True):
        response = input(f"{n}  ").strip()
        response_split = response.split()

        if len(response) == 0:
            break

        if len(response_split) != 2:
            print('Invalid input format')
            continue

        element = response_split[0]
        if not confirm_valid_element(element):
            print('Invalid element symbol')
            continue

        try:
            mass = float(response_split[1])
        except:
            print('Invalid mass value')
            continue

        n += 1
        molar_mass = pt.formula(element).mass
        output_list.append({'element': element, 'mass': mass, 'molar_mass': molar_mass, 'moles': mass / molar_mass})

    return output_list

if __name__ == "__main__":
    print('Welcome')
    elements_in_formula = get_element_input()
    print('\n', elements_in_formula, '\n')

    print('Ratios:')
    min_moles = min([element['moles'] for element in elements_in_formula])
    for element in elements_in_formula:
        symbol = element['element']
        ratio = element['moles'] / min_moles
        element['ratio'] = ratio
        print(symbol, ratio)
    formula_mass = sum([element['molar_mass'] * element['ratio'] for element in elements_in_formula])
    print('Formula Mass:', formula_mass)
    
    while True:
        scale = input('\nInput a number to scale the original ratios by:  ').strip()

        if len(scale) == 0:
            break

        try:
            scale = float(scale)
        except:
            print('NaN')
            continue

        for element in elements_in_formula:
            print(element['element'], element['ratio']*scale)
        print('Formula Mass:', formula_mass * scale)