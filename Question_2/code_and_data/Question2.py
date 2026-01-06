import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q2_bonus_vs_vacation.csv')

df = pd.read_csv(file_path)

corr = df['Bonus'].corr(df['VacationHours'])

plt.figure()
sns.regplot(data=df, x='Bonus', y='VacationHours', line_kws={'color': 'red'})
plt.xlabel('Amount of bonus earned')
plt.ylabel('Number of vacation days')
plt.title('The correlation between annual vacation and bonus', fontsize=16)

plt.text(3000, 15, f'Corr = {corr:.2f}')
plt.show()


