# Fuzzy Logic Toolbox

<img src="https://brighterion.com/wp-content/uploads/2016/07/shutterstock_172740005.jpg" width="800" height="400" width="200">

## Brief

The Fuzzy Logic Toolbox is a user-friendly set of functions and applications designed for creating and simulating fuzzy logic systems. Inspired by MATLAB's Fuzzy Logic ToolboxTM, this toolbox allows users to define fuzzy systems, input and output variables, membership functions, rules, and defuzzification methods. The toolbox is aimed at providing a simple yet powerful platform for designing and testing fuzzy logic systems on well-known problems.


## Getting Started
To begin using the Fuzzy Logic Toolbox, follow these steps:

1. **Create a New Fuzzy System**
    - Choose option 1 to create a new fuzzy logic system.
    - Enter the system's name and provide a brief description.

2. **Define System Variables**
    - Add input (IN) and output (OUT) variables.
    - Specify the range of each variable.

3. **Add Fuzzy Sets to Variables**
    - Define fuzzy sets for each variable using triangular (TRI) or trapezoidal (TRAP) shapes.
    - Assign appropriate values to the fuzzy sets.

4. **Define Rules**
    - Enter rules to establish the relationships between input and output variables.
    - Use the format: `IN_variable set operator IN_variable set => OUT_variable set`.

5. **Run Simulation on Crisp Values**
    - Choose option 4 to run the simulation on crisp input values.
    - Enter crisp values for input variables.

6. **View Results**
    - Observe the fuzzification, inference, and defuzzification stages.
    - The predicted output value and corresponding fuzzy set are displayed.

7. **Close or Quit**
    - Return to the main menu to continue refining the fuzzy system or exit the toolbox.

## Example Usage
Here's an example session using the Fuzzy Logic Toolbox:

```bash
Fuzzy Logic Toolbox
===================
1- Create a new fuzzy system
2- Quit
1
Enter the system’s name and a brief description:
Project Risk Estimation

Main Menu:
==========
1- Add variables.
2- Add fuzzy sets to an existing variable.
3- Add rules.
4- Run the simulation on crisp values.
1
Enter the variable’s name, type (IN/OUT) and range ([lower, upper]):
(Press x to finish)
proj_funding IN [0, 100]
exp_level IN [0, 60]
risk OUT [0, 100]
x
Main Menu:
==========
1- Add variables.
2- Add fuzzy sets to an existing variable.
3- Add rules.
4- Run the simulation on crisp values.
2
Enter the variable’s name:
exp_level
Enter the fuzzy set name, type (TRI/TRAP) and values: (Press x to finish)
beginner TRI 0 15 30
intermediate TRI 15 30 45
expert TRI 30 60 60
x
Main Menu:
==========
1- Add variables.
2- Add fuzzy sets to an existing variable.
3- Add rules.
4- Run the simulation on crisp values.
# ... (Continue adding fuzzy sets for other variables)
4
Enter the crisp values:
proj_funding: 50
exp_level: 40

Running the simulation...
Fuzzification => done
Inference => done
Defuzzification => done
The predicted risk is normal (37.5)

Main Menu:
==========
1- Create a new fuzzy system
2- Quit
2
```



## Installation

To use the Fuzzy Logic Toolbox, make sure you have Python 3 installed on your system. If not, you can download Python 3 from the official website: [Python Downloads](https://www.python.org/downloads/)

Once Python 3 is installed, you can interact with the toolbox using the provided command-line interface.

## Contributing
Pull requests are welcome. For major changes, please open an [issue](https://github.com/Michael-M-aher/Fuzzy-Toolbox/issues) first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Author

👤 **Michael Maher**

- Twitter: [@Michael___Maher](https://twitter.com/Michael___Maher)
- Github: [@Michael-M-aher](https://github.com/Michael-M-aher)

## Show your support

Please ⭐️ this repository if this project helped you!

<a href="https://www.buymeacoffee.com/michael.maher" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60px" width="200" ></a>

## 📝 License

Copyright © 2023 [Michael Maher](https://github.com/Michael-M-aher).<br />
This project is [MIT](https://github.com/Michael-M-aher/Fuzzy-Toolbox/blob/main/LICENSE) licensed.