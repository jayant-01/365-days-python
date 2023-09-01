#violin plot using python


import seaborn as sb
import matplotlib.pyplot as plt

data = sb.load_dataset("tips")
plt.figure(figsize=(10,4))
sb.violinplot(x=data["total_bill"])
plt.show()