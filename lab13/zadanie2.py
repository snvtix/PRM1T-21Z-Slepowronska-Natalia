import pandas as pd

s=pd.read_excel("sample_pivot.xlsx")
print(s)

print("wiersze dla ktorych Units=18 ")
print(s[s["Units"]==18])
print("zawartosc wiersza 999: ")
print(s.iloc[999])
# Dane sierpniowe:
print(s[s.Date.dt.month==8])
