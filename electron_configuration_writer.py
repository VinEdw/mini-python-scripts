# Electron configuration writer

subshell_letters = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'k', 'l']
subshell_capacities = {letter:4*i+2 for i, letter in enumerate(subshell_letters)}

aufbau_principle = []
for i in range(8):
    aufbau_principle.append(subshell_letters[:i])
aufbau_principle = aufbau_principle[1:]

def electron_configuration_str(e_count):
    total = 0
    return_str = ''
    r = 0
    c = 0
    r_ref = 0
    c_ref = 0
    shell_count = 0
    subshell = 's'
    capacity = subshell_capacities[subshell]

    while total < e_count:
        if shell_count == capacity:
            return_str += f"{r+1}{subshell}^{capacity} "
            shell_count = 0
            if c == 0:
                if c_ref+1 == len(aufbau_principle[r_ref]):
                    r_ref += 1
                else:
                    c_ref += 1
                r = r_ref
                c = c_ref
            else:
                r += 1
                c -= 1
        total += 1
        shell_count += 1
        subshell = aufbau_principle[r][c]
        capacity = subshell_capacities[subshell]
    return_str += f"{r+1}{subshell}^{shell_count}"

    return return_str

def abbreviated_electron_configuration_str(e_count):
    noble_gases = {
        2: 'He',
        10: 'Ne',
        18: 'Ar',
        36: 'Kr',
        54: 'Xe',
        86: 'Rn',
    }
    noble_gas_numbers = [i for i in noble_gases]
    e_config = electron_configuration_str(e_count)
    if e_count < 3:
        return e_config

    num = 0
    for i in noble_gas_numbers:
        if i < e_count:
            num = i
        else:
            break
    noble_gas_config = electron_configuration_str(num)
    return f"[{noble_gases[num]}]{e_config[len(noble_gas_config):]}"
    
if __name__ == "__main__":
    while True:
        electrons = input("Please input the number of electrons: ")
        
        try:
            electrons = int(electrons)
        except:
            print('That is not a number silly. Please try again.')
            continue
        if electrons < 1 or electrons > 118:
            print('Number out of range. Please input an integer between 1 and 118 inclusive.') 
            continue
        
        e_config = electron_configuration_str(electrons)
        abbreviated_e_config = abbreviated_electron_configuration_str(electrons)
        print(e_config)
        print(abbreviated_e_config)
        print('-'*30)