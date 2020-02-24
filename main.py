from Utils import *
import pandas as pd
import matplotlib.pyplot as plt

df= loadAndCleanData("creditData.csv")
#df2= computePDF("age",df)
# df3=viewDistribution("age",df)
#df4=viewLogDistribution("age",df)
#df5=computeDefaultRisk("creditData.csv")
#column,bin,feature,
#print(computeProbability("age",[0,40],df))
print(computeDefaultRisk("SeriousDlqin2yrs","age",[0,40],df))
