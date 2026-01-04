import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
bonus_vacation=pd.read_csv(r"C:\Users\natal\OneDrive\Documents\python\Visualization task\Question2\bonus_vs_vacation.csv")
print(bonus_vacation)
bonus=bonus_vacation.iloc[:,1]
vacation=bonus_vacation.iloc[:,2]
correlation = bonus_vacation['Bonus'].corr(bonus_vacation['VacationHours'])
print(correlation)
plt.scatter(bonus,vacation)
plt.xlabel('Amount of bonus earned')
plt.ylabel('Number of vacation days')
plt.title('The correlation between annual vacation and bonus')
plt.text(3000, 15, 'Corr=0.38')
plt.show()


