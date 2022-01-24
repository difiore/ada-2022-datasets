# a python script
import pandas
import seaborn
f = "https://raw.githubusercontent.com/difiore/ADA-2019/master/zombies.csv"
z = pandas.read_csv(f)
print(z.head())
seaborn.boxplot(x="gender", y="weight", data=z)
seaborn.swarmplot(x="gender", y="weight", data=z, size=2, color=".3", linewidth=0)
