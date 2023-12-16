from FuzzySystem import FuzzySystem

def main():
    fuzzy_system = None
    crisp_values = {}

    while True:
        print("\nFuzzy Logic Toolbox\n===================")
        print("1- Create a new fuzzy system")
        print("2- Quit")

        choice = input()

        if choice == '1':
            print("Enter the system’s name and a brief description:")
            name = input()
            description = input()
            # name = "Fuzzy Logic Toolbox"
            # description = "A simple fuzzy logic toolbox"
            fuzzy_system = FuzzySystem(name, description)

            while True:
                print("\nMain Menu:\n==========")
                print("1- Add variables.")
                print("2- Add fuzzy sets to an existing variable.")
                print("3- Add rules.")
                print("4- Run the simulation on crisp values.")

                choice = input()

                if choice == '1':
                    print("Enter the variable’s name, type (IN/OUT) and range ([lower, upper]):")
                    print("(Press x to finish)")
                    print("----------------------------------------------------------------------")
                    while True:
                        line_input = input()
                        if line_input.lower() == 'x':
                                break
                        try:
                            len_i = len(line_input.split(' ',2))
                            if(len_i != 3):
                                raise ValueError(f"Expected 3 arguments but got {len_i}.")
                            v_name, v_type, v_range = map(str.strip, line_input.split(' ',2))
                            v_range = tuple(eval(v_range))
                            if v_type not in ['IN', 'OUT']:
                                raise ValueError("Invalid variable type (IN/OUT).")
                            fuzzy_system.add_variable(v_name, v_type, v_range)
                        except ValueError as e:
                            print(f"Invalid input. {str(e)} Please try again.")

                elif choice == '2':
                    print("Enter the variable’s name:")
                    print("---------------------------")
                    v_name = input()
                    print("Enter the fuzzy set name, type (TRI/TRAP) and values: (Press x to finish)")
                    print("------------------------------------------------------")
                    while True:
                        line_input = input()
                        if line_input.lower() == 'x':
                            break
                        try:
                            len_i = len(line_input.split(' ',2))
                            if(len_i != 3):
                                raise ValueError(f"Expected 3 arguments but got {len_i}.")
                            set_name, f_type, values = map(str.strip, line_input.split(' ',2))
                            if f_type not in ['TRI', 'TRAP']:
                                raise ValueError("Invalid fuzzy set type (TRI/TRAP).")
                            values = tuple(map(float, values.split(' ')))
                            fuzzy_system.add_fuzzy_set(v_name, set_name, f_type, values)
                        except ValueError as e:
                            print(f"Invalid input. {str(e)} Please try again.")

                elif choice == '3':
                    print("Enter the rule in this format: (Press x to finish)")
                    print("IN_variable set operator IN_variable set => OUT_variable set")
                    print("-------------------------------------------------------------")
                    while True:
                        line_input = input()
                        if line_input.lower() == 'x':
                            break
                        try:
                            antecedent, consequent = map(str.strip, line_input.split('=>',1))
                            antecedent = antecedent.split(' ')
                            consequent = consequent.split(' ')
                            if len(consequent) != 2 or len(antecedent) < 3:
                                raise ValueError("Invalid consequent format.")
                            operators = ['and', 'or', 'and_not', 'or_not']
                            antecedent_operations = []
                            if(antecedent[1] == 'not'):
                                if(len(antecedent) < 4):
                                    raise ValueError("Invalid antecedent format.")
                                antecedent_operations.append(antecedent[1])
                                antecedent_operations.append((antecedent[0], antecedent[2]))
                                i = 3
                            else:
                                if(len(antecedent) < 3):
                                    raise ValueError("Invalid antecedent format.")
                                antecedent_operations.append((antecedent[0], antecedent[1]))
                                i = 2
                            while i < len(antecedent):
                                if antecedent[i] in operators and len(antecedent) > i+2:
                                    antecedent_operations.append(antecedent[i])
                                    if antecedent[i+2] == 'not':
                                        if(len(antecedent) < i+4):
                                            raise ValueError("Invalid antecedent format.")
                                        antecedent_operations.append(antecedent[i+2])
                                        antecedent_operations.append((antecedent[i+1], antecedent[i+3]))
                                        i+=4
                                    else:
                                        antecedent_operations.append((antecedent[i+1], antecedent[i+2]))
                                        i+=3
                                else:
                                    raise ValueError("Invalid antecedent format.")
                            fuzzy_system.add_rule(antecedent_operations, (consequent[0], consequent[1]))
                        except ValueError as e:
                            print(f"Invalid input. {str(e)} Please try again.")

                elif choice == '4':
                    if fuzzy_system and fuzzy_system.variables and fuzzy_system.rules :
                        print("Enter the crisp values:")
                        print("-----------------------")
                        for variable in fuzzy_system.variables.values():
                            if variable.type == 'IN':
                                print(f"{variable.name} = ", end='')
                                crisp_values[variable.name] = float(input())
                        fuzzy_system.run_simulation(crisp_values)

                    else:
                        print("CAN’T START THE SIMULATION! Please add the fuzzy sets and rules first.")

                elif choice.lower() == 'close':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()