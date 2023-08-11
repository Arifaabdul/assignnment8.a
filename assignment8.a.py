

# Task: Explore in Google and Make a document :

# 1. What is pandas library in python? 
'''Pandas is a Python library used for working with data sets. 
It has functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data",
 and "Python Data Analysis" and was created by Wes McKinney in 2008.'''

# 2. How to install library in python?
'''In this short guide, you'll see how to install a package in Python using PIP. You'll also learn how to uninstall a package that is no longer needed.
If you're using Windows, you'll be able to install a Python package by opening the Windows Command Prompt, and then typing this command:
    pip install package_name'''

# 3. what is package in pandas library?
'''pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with
 “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical,
   real-world data analysis in Python.'''

# 4. what are delimiter files?
'''A delimiter is the character that separates fields in your file. 
It is what the computer reads as a "separator" of sorts, giving structure to your file. 
Without it, your file would be one, verrrry long read with no organizational structure at all.'''

# 5. Write some delimiter files?

# Task: Create files and import in spyder and print data.

# 1. Create a friend_names.csv file delimiter is comma(,)  (atleast 10 names, columns are FriendName,Quality)
df_friend_names=pd.read_csv(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\friends_names.csv")
print(df_friend_names)

import pandas as pd
# 2. Create a family_members.txt file delimiter is star (*), (atleast 10 names, columns are FamilyMemberName*Relation)
df_family_members=pd.read_csv(r"C:\\Users\Abdul\\Downloads\\assignment8.a\\family_memberst.txt")
print(df_family_members)

# 3. Create a Vegfood_items.txt file delimiter is pipe (|), (atleast 10 names, columns are VegFoodName*Taste)
df_Vegfood_items=pd.read_csv(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Vegfood_items_pipe.txt")
print(df_Vegfood_items)

# 4. Create a NonVegfood_items.txt file delimiter is pipe (|), (atleast 10 names, columns are NonVegFoodName*Taste)
df_NonVegfood_items=pd.read_csv(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Non_Vegfood_items_pipe.txt")
print(df_NonVegfood_items)


# 5. Create a month_names.txt file delimiter is and (&), (atleast 12 names, columns are MonthName*Season)
df_month_names=pd.read_csv(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\month_names&.txt")
print(df_month_names)


# 6. Create a colours_names.txt file delimiter is cap (^), (atleast 12 names, columns are colourName_in_English^colourName_in_Hindi^colourName_in_Telugu)
df_colour_names=pd.read_csv(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\colours_names^.txt")
print(df_colour_names)

