# What is the relationship between sick leave and Job Title (PersonType)?

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("q_4_whole.csv")

#print(df.head(5))
#print(df.info())

# print(len(df))
# print(df.JobTitle.value_counts())
# print(len(df.JobTitle.value_counts()))
# print(df.SickLeaveHours.value_counts())
#print(df.Department.value_counts())
#print(df.GroupName.value_counts())

sns.boxplot(data=df, x='PersonType', y='SickLeaveHours')
plt.title('Sick Leave by Person Type')
plt.ylabel("Sick Leave (hours)")

ax = plt.gca()
labels_x = ["Employee", "Sales Person"]
ax.set_xticklabels(labels_x)


groups = df.groupby('PersonType')['SickLeaveHours']
for i, (rev, g) in enumerate(groups):
    stats = g.describe() 
    ax.text(i, stats['min'], f"min: {int(stats['min'])}", ha='center', va='top', fontsize=9)
    ax.text(i, stats['50%'], f"median: {int(stats['50%'])}", ha='center', va='top', fontsize=9)
    ax.text(i, stats['max'], f"max: {int(stats['max'])}", ha='center', va='bottom', fontsize=9)


mean_sl = df.groupby("JobTitle")["SickLeaveHours"].mean()

top10 = mean_sl.sort_values(ascending=False).head(10)
bot10 = mean_sl.sort_values().head(10)

fig, axes = plt.subplots(1, 2, figsize=(16, 14))
fig.suptitle("Average Sick Leave Across Job Titles", fontsize=18, fontweight='bold')

axes[0].barh(top10.index, top10.values, height = 0.8)
axes[0].set_title("Top 10 Job Titles by Average Sick Leave(hours)", fontweight='bold')
axes[0].invert_yaxis() 
axes[0].set_xlim(0, top10.max() * 1.1)
for i, v in enumerate(top10.values):
    axes[0].text(v + 0.5, i, f"{v:.1f} h", va='center', fontsize = 8)

axes[1].barh(bot10.index, bot10.values, height = 0.8)
axes[1].set_title("Bottom 10 Job Titles by Average Sick Leave(hours)", fontweight='bold')
axes[1].invert_yaxis()
axes[1].set_xlim(0, bot10.max() * 1.15)
for i, v in enumerate(bot10.values):
    axes[1].text(v + 0.5, i, f"{v:.1f} h", va='center', fontsize = 8)

plt.subplots_adjust(left=0.25, right=0.95, wspace=0.8)

plt.tight_layout(rect=[0.03, 0, 1, 0.97]) 


avg_sick_leave_d = mean_d = df.groupby("Department")["SickLeaveHours"].mean().sort_values(ascending=False)
avg_sick_leave_g = mean_g = df.groupby("GroupName")["SickLeaveHours"].mean().sort_values(ascending=False)


plt.figure()
plt.barh(avg_sick_leave_d.index, avg_sick_leave_d.values)
plt.title("Average Sick Leave per Department", fontsize=18, fontweight='bold')
ax = plt.gca()
for i, v in enumerate(avg_sick_leave_d.values):
    ax.text(v + 0.5, i, f"{v:.1f}", va='center', fontsize = 8)
plt.tight_layout(rect=[0.01, 0, 1, 1]) 

plt.figure()
plt.barh(avg_sick_leave_g.index, avg_sick_leave_g.values)
plt.title("Average Sick Leave per Group", fontsize=18, fontweight='bold')
ax = plt.gca()
for i, v in enumerate(avg_sick_leave_g.values):
    ax.text(v + 0.5, i, f"{v:.1f}", va='center', fontsize = 8)
plt.tight_layout(rect=[0.01, 0, 1, 1]) 


plt.show()





