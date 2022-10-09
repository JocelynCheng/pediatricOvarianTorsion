# Python program to read an excel file
import pandas as pd
import openpyxl
import re

# Give the location of the file
pathMRI = "MRI_Pelvis_Pedi.F.10yr.xlsx"
pathUS = "US_Pelvis_Pedi.F.10yr.xlsx"

df1_i = pd.read_excel(pathMRI)
df2_i = pd.read_excel(pathUS)
df1_i = df1_i.reset_index()
df2_i = df2_i.reset_index()

#eliminating data from patients without matching MRNs. This ensures that all patients have had both an MRI and US.
ultrasoundMatches = df2_i[(df2_i['Patient MRN'].isin(df1_i['Patient MRN']))]
mriMatches = df1_i[(df1_i['Patient MRN'].isin(df2_i['Patient MRN']))]


# determining the name of the file
file_name1 = 'ultrasoundMatches2.xlsx'
file_name2 = 'mriMatches2.xlsx'

# saving the excel
ultrasoundMatches.to_excel(file_name1)
mriMatches.to_excel(file_name2)
#print('DataFrame is written to Excel File successfully.')



####PARSING FOR TORSION
df_us = ultrasoundMatches
df_mri = mriMatches


#str.contains documentation for future customization: https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html
df1 = df_us[df_us['Report Text'].str.contains('torsion', na = False)]
df2 = df_mri[df_mri['Report Text'].str.contains('torsion', na = False)]

df2
df1

df1.to_excel('ultrasoundParsed.xlsx')
df2.to_excel('mriParsed2.xlsx')



txt = "lalala this is a IMPRESSION:::: ovarian torsion"
x = re.search("IMPRESSION.*torsion", txt)

x
#view DataFrame
