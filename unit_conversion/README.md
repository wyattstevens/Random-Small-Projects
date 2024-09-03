A unit conversion tool that I made.

First we have a list of conversions that is some starting unit and target unit with the multiplier to get from the starting to the target unit. For example to get from 'ft' to 'in' we see that the multiplier is 12 so given a measurement in feet we multiply it by 12 to get the measurement in inches.

(multiplier, starting_unit, target_unit)
conversions = [
        (0.3048, 'ft', 'm'),
        (3.28084, 'm', 'ft'),
        (12, 'ft', 'in'),
        (0.08333333, 'in', 'ft'),
        (2.54, 'in', 'cm'),
        (0.3937008, 'cm', 'in'),
]

We parse the conversion list and create a node for every starting unit and create edges to the target units with the multiplier being the weight of the edge to that unit.
{
    'ft': [('m', 0.3048), ('in', 12)], 
    'm': [('ft', 3.28084)], 
    'in': [('ft', 0.08333333), ('cm', 2.54)], 
    'cm': [('in', 0.3937008)]
}

Next we do a depth first search starting from our starting unit in the graph keeping track of the proper unit conversions as we traverse it and returning that value when we find ourselves at the target unit.