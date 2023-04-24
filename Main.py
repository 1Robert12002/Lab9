import pandas as pd

dataframe = pd.read_excel(open('Test.xlsx', 'rb'), sheet_name='Sheet1')
print(dataframe.to_markdown())
dataframe['lungime'] = dataframe['nume'].str.len()
dataframe.to_csv('Lungime.csv', index=False)