# Q1. List any five functions of the pandas library with execution.
# Ans.
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df.head()
#     head() and tail() - Used to view the top and bottom rows of the DataFrame, respectively.
df.sort_values("Pclass")
#     sort_values() - Used to sort the DataFrame by one or more columns.
df.describe()
#     describe() - Used to get summary statistics of the DataFrame, including the 
#     count, mean, standard deviation, minimum, and maximum values.
df.groupby("Survived").sum()
#     groupby() - Used to group the DataFrame by one or more columns and perform 
#     aggregate operations on the groups.
df.info()
#     info() - Used to get information about the DataFrame, including the data types, 
#     number of non-null values, and memory usage.

# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the 
#     DataFrame with a new index that starts from 1 and increments by 2 for each row.
# Ans.
import pandas as pd
data1 = {"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]}
df = pd.DataFrame(data1)
df.set_index(pd.Index(range(1,len(df)*2+1,2)))

# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python 
#     function that iterates over the DataFrame and calculates the sum of the first 
#     three values in the 'Values' column. The function should print the sum to the console.

#     For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50]
#     , your function should calculate and print the sum of the first three values, which is 60.
# Ans.
import pandas as pd
data2 = {"Values":[10,20,30,40,50], "B":[4,5,6,3,124], "C":[7,8,9,12,21]}
df = pd.DataFrame(data2)
df.loc[0:2, "Values"].sum()

# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column 
#     'Word_Count' that contains the number of words in each row of the 'Text' column.
# Ans.
import pandas as pd
data3 = {"Text":["Abc","pwskills","krish","nair","sudh"], 
         "Values":[10,20,30,40,50], "B":[4,5,6,3,124], "C":[7,8,9,12,21]}
df = pd.DataFrame(data3)
df["word_count"] = df["Text"].apply(lambda x: len(str(x)))
df

# Q5. How are DataFrame.size() and DataFrame.shape() different?
# Ans.
#     DataFrame.size and DataFrame.shape are both methods of a Pandas DataFrame that 
#     return information about the size of the DataFrame, but they return different 
#     types of information.

#     DataFrame.size returns the total number of elements in the DataFrame, which is 
#     equal to the number of rows times the number of columns. It returns a single 
#     integer value.

#     DataFrame.shape returns a tuple containing the number of rows and columns in 
#     the DataFrame, respectively. So, it returns two values - the number of rows and 
#     the number of columns - as a tuple.
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df.size)  # Output: 9
print(df.shape)  # Output: (3, 3)

# Q6. Which function of pandas do we use to read an excel file?
# Ans.
#     We use read_excel() function
import pandas as pd
df = pd.read_excel('example.xlsx', sheet_name='Sheet1')

# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that 
#     contains email addresses in the format 'username@domain.com'. Write a Python 
#     function that creates a new column 'Username' in df that contains only the 
#     username part of each email address.

#     The username is the part of the email address that appears before the '@' 
#     symbol. For example, if the email address is 'john.doe@example.com', the 
#     'Username' column should contain 'john.doe'. Your function should extract the 
#     username from each email address and store it in the new 'Username' column.
# Ans.
import pandas as pd
data4 = {"Email":("Abc@pwskills.com", "pwskills@pwskills.com", "krish@pwskills.com", 
                  "naik@pwskills.com", "sudh@pwskills.com"),
         "Text":["Abc","pwskills","krish","nair","sudh"], 
         "Values":[10,20,30,40,50], "B":[4,5,6,3,124], "C":[7,8,9,12,21]}
data4
df = pd.DataFrame(data4)
df["Username"] = df["Email"].apply(lambda x: x.split("@")[0])
df

# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a 
#     Python function that selects all rows where the value in column 'A' is greater 
#     than 5 and the value in column 'B' is less than 10. The function should return 
#     a new DataFrame that contains only the selected rows.

#     For example, if df contains the following values:
#    A   B   C
# 0  3   5   1
# 1  8   2   7
# 2  6   9   4
# 3  2   3   5
# 4  9   1   2
#     Your function should select the following rows:   
#    A   B   C
# 1  8   2   7
# 4  9   1   2
#     The function should return a new DataFrame that contains only the selected rows.
# Ans.
import pandas as pd
data5 = {"A":[3,8,6,2,9], "B":[5,2,9,3,1], "C":[1,7,4,5,2]}
df =pd.DataFrame(data5)
df[(df["A"]>5) & (df["B"]<10)]

# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function
#     to calculate the mean, median, and standard deviation of the values in the 'Values' column.
# Ans.
import pandas as pd
df = pd.DataFrame({"Values":(1,2,3,4,5,6,33)})
df.describe()
#This function will return all the summary statistics of the "Values" column.

# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', 
#      write a Python function to create a new column 'MovingAverage' that contains 
#      the moving average of the sales for the past 7 days for each row in the 
#      DataFrame. The moving average should be calculated using a window of size 7 and 
#      should include the current day.
# Ans.

import pandas as pd

def add_moving_average(x):
    x["MovingAverage"] = x["Sales"].rolling(window =7, min_periods=1).mean()
    return x

df = pd.DataFrame({'Sales': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                   'Date': pd.date_range('2022-01-01', periods=10, freq='D')})
df = add_moving_average(df)
df

# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python 
#      function that creates a new column 'Weekday' in the DataFrame. The 'Weekday' 
#      column should contain the weekday name (e.g. Monday, Tuesday) corresponding 
#      to each date in the 'Date' column.

#      For example, if df contains the following values:
#    Date
# 0  2023-01-01
# 1  2023-01-02
# 2  2023-01-03
# 3  2023-01-04
# 4  2023-01-05

#      Your function should create the following DataFrame:
#    Date           Weekday
# 0  2023-01-01     Sunday
# 1  2023-01-02     Monday
# 2  2023-01-03    Tuesday
# 3  2023-01-04    Wednesday
# 4  2023-01-05    Thursday
#      The function should return the modified DataFrame.
# Ans.
import pandas as pd
df = pd.DataFrame({"Date":pd.date_range(start="2023-01-01", periods=5)})       
df["Weekday"] = df["Date"].dt.strftime("%A")                                    
df

# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, 
#      write a Python function to select all rows where the date is between 
#      '2023-01-01' and '2023-01-31'.
# Ans.
import pandas as pd
df = pd.DataFrame({"Date":pd.date_range(start="2023-01-01", end="2023-02-28")})
df[df["Date"].between(left="2023-01-01", right="2023-01-31", inclusive="both")]     

# Q13. To use the basic functions of pandas, what is the first and foremost 
#      necessary library that needs to be imported?
# Ans.
#      The first and foremost necessary library that needs to be imported to use 
#      the basic functions of pandas is pandas itself.
import pandas as pd #alias












