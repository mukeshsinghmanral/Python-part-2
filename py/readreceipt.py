import pandas as pd
covid_data=pd.read_csv(r'C:\Users\dell\Documents\hh.csv',nrows=3,names=['sr no.','names','maths','english','physics','chemistry'])
covid_data.to_csv(r'new.csv',index=None)
