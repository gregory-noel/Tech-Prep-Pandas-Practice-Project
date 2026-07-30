import pandas as pd

#Open the csv file
df = pd.read_csv('Grades_Short.csv')

#print the top few rows

#df.head()
#print the info of the columns
#df.info()
#df.describe()
#add a column called average with the average of each graded column

df['Average'] = df[['Assignment_1',	'Assignment_2','Quiz_1','Quiz_2','Mid_Term_Exam','Final_Exam']].mean(axis=1)

#add a column with the grade assigned using a defined function

def letter_grades(average):
    if average >= 90:
        return 'A+'
    if average < 90 and average >= 80:
        return 'A'
    if average < 80 and average >= 70:
        return 'B'
    if average < 70 and  average >= 60:
        return 'C'
    if average < 60 and average >= 55:
        return 'D'
    if average < 55:
        return 'F'





df['Letter Grade'] = df['Average'].apply(letter_grades)


#Save to a new CSV (false index is to prepvent a new column with the index numbers)
df.to_csv('Graded_Short_with_Averages_Letters.csv', index=False)

df.head()