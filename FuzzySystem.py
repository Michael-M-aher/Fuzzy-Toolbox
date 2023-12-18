from FuzzyClasses import FuzzyVariable, FuzzyRule

class FuzzySystem:
    """
    This class represents a Fuzzy System.

    Parameters:
    -----------
    name: str
        The name of the fuzzy system.
    description: str
        A description of the fuzzy system.

    Attributes:
    -----------
    name: str
        The name of the fuzzy system.
    description: str
        A description of the fuzzy system.
    variables: dict
        A dictionary to store fuzzy variables.
    rules: list
        A list to store fuzzy rules.

    Methods:
    --------
    add_variable(name, v_type, v_range)
        Adds a fuzzy variable to the system.

    add_fuzzy_set(variable_name, name, f_type, values)
        Adds a fuzzy set to a fuzzy variable.

    add_rule(antecedent, consequent)
        Adds a fuzzy rule to the system.

    run_simulation(crisp_values)
        Runs the simulation using crisp input values.

    fuzzification(crisp_values)
        Performs fuzzification of crisp input values.

    inference(fuzzy_values)
        Performs the inference step of the fuzzy system.

    defuzzification(rule_strengths)
        Performs defuzzification to obtain a crisp output.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.variables = {}
        self.rules = []

    def add_variable(self, name, v_type, v_range):
        """
        Adds a fuzzy variable to the system.

        Parameters:
        -----------
        name: str
            The name of the fuzzy variable.
        v_type: str
            The type of the fuzzy variable.
        v_range: tuple
            The range of the fuzzy variable.
        """
        variable = FuzzyVariable(name, v_type, v_range)
        self.variables[name] = variable

    def add_fuzzy_set(self, variable_name, name, f_type, values):
        """
        Adds a fuzzy set to a fuzzy variable.

        Parameters:
        -----------
        variable_name: str
            The name of the fuzzy variable.
        name: str
            The name of the fuzzy set.
        f_type: str
            The type of the fuzzy set.
        values: tuple
            The values defining the fuzzy set.
        """
        variable = self.variables.get(variable_name)
        if variable:
            variable.add_fuzzy_set(name, f_type, values)
        else:
            print(f"Error: Variable '{variable_name}' not found.")

    def add_rule(self, antecedent, consequent):
        """
        Adds a fuzzy rule to the system.

        Parameters:
        -----------
        antecedent: list
            The antecedent of the fuzzy rule.
        consequent: tuple
            The consequent of the fuzzy rule.
        """
        rule = FuzzyRule(antecedent, consequent)
        self.rules.append(rule)

    def run_simulation(self, crisp_values):
        """
        Runs the simulation using crisp input values.

        Parameters:
        -----------
        crisp_values: dict
            A dictionary of crisp input values.
        """
        print("\nRunning the simulation...")

        # Fuzzification
        fuzzy_values = self.fuzzification(crisp_values)
        print("Fuzzification => done")

        # Inference
        rule_strengths = self.inference(fuzzy_values)
        print("Inference => done")

        # Defuzzification
        var_name, result, num = self.defuzzification(rule_strengths)
        print("Defuzzification => done")

        print(f"\nThe predicted {var_name} is {result} ({num})")

    def fuzzification(self, crisp_values):
        """
        Performs fuzzification of crisp input values.

        Parameters:
        -----------
        crisp_values: dict
            A dictionary of crisp input values.

        Returns:
        --------
        fuzzy_values: dict
            A dictionary of fuzzy values for each variable and fuzzy set.
        """
        fuzzy_values = {}
        for variable_name, value in crisp_values.items():
            variable = self.variables.get(variable_name)
            if variable:
                fuzzy_values[variable_name] = {}
                for set_name, fuzzy_set in variable.fuzzy_sets.items():
                    fuzzy_values[variable_name][set_name] = self._membership(value, fuzzy_set)
        return fuzzy_values

    def _membership(self, x, fuzzy_set):
        """
        Computes the membership value for a given value and fuzzy set.

        Parameters:
        -----------
        x: float
            The input value.
        fuzzy_set: FuzzySet
            The fuzzy set.

        Returns:
        --------
        membership_value: float
            The computed membership value.
        """
        if fuzzy_set.type == 'TRI':
            return self._triangular_membership(x, fuzzy_set.values)
        elif fuzzy_set.type == 'TRAP':
            return self._trapezoidal_membership(x, fuzzy_set.values)

    def _triangular_membership(self, x, values):
        """
        Computes the membership value for a triangular fuzzy set.

        Parameters:
        -----------
        x: float
            The input value.
        values: tuple
            The values defining the triangular fuzzy set.

        Returns:
        --------
        membership_value: float
            The computed membership value.
        """
        a, b, c = values
        if x <= a or x >= c:
            return 0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x < c:
            return (c - x) / (c - b)

    def _trapezoidal_membership(self, x, values):
        """
        Computes the membership value for a trapezoidal fuzzy set.

        Parameters:
        -----------
        x: float
            The input value.
        values: tuple
            The values defining the trapezoidal fuzzy set.

        Returns:
        --------
        membership_value: float
            The computed membership value.
        """
        a, b, c, d = values
        if x <= a or x >= d:
            return 0
        elif b <= x <= c:
            return 1
        elif a < x < b:
            return (x - a) / (b - a)
        elif c < x < d:
            return (d - x) / (d - c)

    def inference(self, fuzzy_values):
        """
        Performs the inference step of the fuzzy system.

        Parameters:
        -----------
        fuzzy_values: dict
            A dictionary of fuzzy values for each variable and fuzzy set.

        Returns:
        --------
        rule_strengths: list
            A list of rule strengths and their consequents.
        """
        rule_strengths = []
        for rule in self.rules:
            antec = rule.antecedent.copy()

            # replace fuzzy set names with their strengths
            for i in range(0, len(antec)):
                if isinstance(antec[i], tuple):
                    v_name, v_set = antec[i]
                    antecedent_strength = fuzzy_values[v_name][v_set]
                    antec[i] = antecedent_strength

            # evaluate the antecedent
            antec = self._not(antec)
            antec = self._and(antec)
            antec = self._or(antec)

            # add the rule strength and the consequent
            rule_strengths.append((antec[0], rule.consequent))
        return rule_strengths

    def defuzzification(self, rule_strengths):
        """
        Performs defuzzification to obtain a crisp output.

        Parameters:
        -----------
        rule_strengths: list
            A list of rule strengths and their consequents.

        Returns:
        --------
        var_name: str
            The name of the variable.
        result: float
            The defuzzified result.
        num: float
            The total strength of the rules.
        """
        aggregated_values = {}
        centeroids = {}
        var_name = ''
        total_strength = 0
        for strength, consequent in rule_strengths:
            if consequent not in aggregated_values:
                aggregated_values[consequent] = strength
            else:
                aggregated_values[consequent] = max(aggregated_values[consequent], strength)
            total_strength += strength
        result = 0
        for value, strength in aggregated_values.items():
            v, s = value
            var_name = v
            points = self.variables[v].get_fuzzy_set(s).values
            centeroids[s] = sum(points) / len(points)
            result += centeroids[s] * strength
        result /= total_strength

        return var_name, self._output(centeroids, result), result

    def _output(self, centeroids, result):
        """
        Computes the output of the fuzzy system.

        Parameters:
        -----------
        centeroids: dict
            A dictionary of fuzzy set centeroids.
        result: float
            The defuzzified result.

        Returns:
        --------
        output: str
            The output fuzzy set.
        """
        output = []
        for key, value in centeroids.items():
            output.append((abs(value - result), key))
        return min(output)[1]

    def _not(self, antec):
        """
        Performs the "not" operation on the antecedent.

        Parameters:
        -----------
        antec: list
            The antecedent list.

        Returns:
        --------
        antec: list
            The modified antecedent list.
        """
        ind = []
        for i in range(0, len(antec)):
            if isinstance(antec[i], str) and antec[i] == 'not':
                antec[i] = 1 - antec[i + 1]
                ind.append(i + 1)

        # remove the evaluated values
        for i in sorted(ind, reverse=True):
            del antec[i]
        return antec

    def _and(self, antec):
        """
        Performs the "and" operation on the antecedent.

        Parameters:
        -----------
        antec: list
            The antecedent list.

        Returns:
        --------
        antec: list
            The modified antecedent list.
        """
        ind = []
        for i in range(0, len(antec)):
            if isinstance(antec[i], str) and antec[i] == 'and':
                antec[i] = min(antec[i - 1], antec[i + 1])
                ind.extend((i - 1, i + 1))

        # remove the evaluated values
        for i in sorted(ind, reverse=True):
            del antec[i]
        return antec

    def _or(self, antec):
        """
        Performs the "or" operation on the antecedent.

        Parameters:
        -----------
        antec: list
            The antecedent list.

        Returns:
        --------
        antec: list
            The modified antecedent list.
        """
        ind = []
        for i in range(0, len(antec)):
            if isinstance(antec[i], str) and antec[i] == 'or':
                antec[i] = max(antec[i - 1], antec[i + 1])
                ind.extend((i - 1, i + 1))

        # remove the evaluated values
        for i in sorted(ind, reverse=True):
            del antec[i]
        return antec
