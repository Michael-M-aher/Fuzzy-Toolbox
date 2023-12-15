class FuzzyVariable:
    """
    This class represents a Fuzzy Variable in a Fuzzy System.

    Parameters:
    -----------
    name: str
        The name of the fuzzy variable.
    v_type: str
        The type of the fuzzy variable.
    v_range: tuple
        The range of the fuzzy variable.

    Attributes:
    -----------
    name: str
        The name of the fuzzy variable.
    type: str
        The type of the fuzzy variable.
    range: tuple
        The range of the fuzzy variable.
    fuzzy_sets: dict
        A dictionary to store fuzzy sets associated with the variable.

    Methods:
    --------
    add_fuzzy_set(name, f_type, values)
        Adds a fuzzy set to the fuzzy variable.

    get_fuzzy_set(name)
        Retrieves a fuzzy set by name.
    """
    def __init__(self, name, v_type, v_range):
        self.name = name
        self.type = v_type
        self.range = v_range
        self.fuzzy_sets = {}

    def add_fuzzy_set(self, name, f_type, values):
        """
        Adds a fuzzy set to the fuzzy variable.

        Parameters:
        -----------
        name: str
            The name of the fuzzy set.
        f_type: str
            The type of the fuzzy set.
        values: tuple
            The values defining the fuzzy set.
        """
        fuzzy_set = FuzzySet(name, f_type, values)
        self.fuzzy_sets[name] = fuzzy_set

    def get_fuzzy_set(self, name):
        """
        Retrieves a fuzzy set by name.

        Parameters:
        -----------
        name: str
            The name of the fuzzy set.

        Returns:
        --------
        fuzzy_set: FuzzySet or None
            The fuzzy set if found, None otherwise.
        """
        return self.fuzzy_sets.get(name)


class FuzzySet:
    """
    This class represents a Fuzzy Set associated with a Fuzzy Variable.

    Parameters:
    -----------
    name: str
        The name of the fuzzy set.
    f_type: str
        The type of the fuzzy set.
    values: tuple
        The values defining the fuzzy set.

    Attributes:
    -----------
    name: str
        The name of the fuzzy set.
    type: str
        The type of the fuzzy set.
    values: tuple
        The values defining the fuzzy set.
    """
    def __init__(self, name, f_type, values):
        self.name = name
        self.type = f_type
        self.values = values


class FuzzyRule:
    """
    This class represents a Fuzzy Rule in a Fuzzy System.

    Parameters:
    -----------
    antecedent: list
        The antecedent of the fuzzy rule.
    consequent: tuple
        The consequent of the fuzzy rule.

    Attributes:
    -----------
    antecedent: list
        The antecedent of the fuzzy rule.
    consequent: tuple
        The consequent of the fuzzy rule.
    """
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent