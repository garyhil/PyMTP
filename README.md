# PyMTP - A MTP based Python State Machine

This repository contains a Python script that generates a state machine using the transitions package. The state machine is similar to the one used in the Modular Type Package.

## CAUTION
At present, this is a very rudimentary abstraction of the MTP Service State-Machine and is intended solely for experimental purposes. It is not recommended for use in a production environment at this time. The author(s) do not provide any assurance that this code will function as described in the MTP norm.

## Prerequisites
To run this script, you need to have Python 3 and the transitions package installed on your computer. You can install transitions using pip:

```
  python3 -m pip install transitions
```


## How to use
To run the script, simply execute the following command in your terminal:

```
  /<path to the file/python3 python state_machine.py
```

This will generate a state machine using the transitions package and print the states and transitions to the console.

However, you can also execute the 'opcua_mtp.py' file, which will start an OPC UA Server with a 'State Machine' Object, consisting of two Nodes, one recieving the current Command and one displaying the current State.

## Modular Type Package State Machine
The Modular Type Package (MTP) used in the Process Industry, is a modular, flexible, and reusable software architecture for developing control applications. MTP provides a standardized and structured approach to developing control systems and can be applied to a range of industries, including chemical, oil and gas, and food and beverage. It is designed to improve the efficiency, reliability, and safety of control systems, and to reduce the time and cost of development and maintenance. 

For further Details on the MTP refer to the VDI/VDE/NAMUR 2658 or the scientific literature on the toic.

While the Modular Type Package (MTP) encompasses much more than just the Service-State-Machine, our focus is on this specific component. By utilizing the state machine implemented in Python, one can integrate additional modules into a production facility without being limited to PLC-based modules. This allows any software functionality to be integrated as a service, enabling greater flexibility in the production process.




## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

- [@garyhil](https://www.github.com/garyhil)

