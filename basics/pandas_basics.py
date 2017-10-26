# previously we looked into numpy and its ndarrayobject in particular. Here 
# we build on that knowledge by looking at the data structures provided by the Pandas Library.
# Pandas is a newer package built on top of NumPz and proveides an efficient 
# implementation of a DataFrame. 

# Here we will focus on the mechanics of using Series, DataFrame and related structures effectively. 
# We will use examples drawn from real datasets where appropriate, but these examples are not 
# necessarily the focus.

import numpy as np
import pandas as pd 

# Series
# a pandas series is a one dimensional array of indeed data
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data
# as attributes it has values and index attributes
data.values
data.index

# can be sliced 
data[1:3]

# The big difference is that it has a specific index value in the series
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])
data

# The series data object can also be likened and used as a python dictionary.
# but for typed types only. So its a bit faster but a lot less general
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population

# Typical dictionary actions can be taken as well
population['California']

# However you can also slice a dictionary which is a bit weird
population['California':'Illinois']

# Turn a dictionary into a pd series
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area

# lets take population and area and turn it into a dataframe
states = pd.DataFrame({'population': population,
                       'area': area})
states

# DataFrame as specialized dictionary
# Similarly, we can also think of a DataFrame as a specialization of a dictionary. 
# Where a dictionary maps a key to a value, a DataFrame maps a column name to a Series 
# of column data. For example, asking for the 'area' attribute returns the Series object 
# containing the areas we saw earlier:
