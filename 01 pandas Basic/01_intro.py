import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
# data frame
df = pandas.DataFrame(mydataset)

print(df)
print("version of the pandas is :",pandas.__version__)