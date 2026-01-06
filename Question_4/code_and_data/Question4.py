# What is the relationship between sick leave and Job Title (PersonType)?

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Q4_sick_leave.csv')

df = pd.read_csv(file_path)

# print(df.head(5))
# print(df.info())
# print(len(df))
# print(df.JobTitle.value_counts())
# print(len(df.JobTitle.value_counts()))
# print(df.SickLeaveHours.value_counts())
# print(df.Department.value_counts())
# print(df.GroupName.value_counts())

# -------- SickLeave_PersonType_boxplot --------
plt.figure()
sns.boxplot(data=df, x='PersonType', y='SickLeaveHours')
plt.title('Sick Leave by Person Type')
plt.ylabel("Sick Leave (hours)")

ax = plt.gca()
labels_x = ["Employee", "Sales Person"]
ax.set_xticks(range(len(labels_x)))
ax.set_xticklabels(labels_x)

# Annotate min, median, max per group
stats_df = df.groupby('PersonType')['SickLeaveHours'].agg(['min', 'median', 'max']).reset_index()

for i in range(len(stats_df)):
    min = stats_df.loc[i,'min']
    median = stats_df.loc[i,'median']
    max = stats_df.loc[i,'max']
    plt.text(i, min, f'min: {min}', ha='center', va='top')
    plt.text(i, median, f'median: {int(median)}', ha='center', va='bottom')
    plt.text(i, max, f'max: {max}', ha='center', va='bottom')

# -------- SickLeave_JobTitle --------

mean_sl = df.groupby("JobTitle")["SickLeaveHours"].mean()
top10 = mean_sl.nlargest(10)
bot10 = mean_sl.nsmallest(10)

# Function to annotate bars
def annotate_bars(ax, values):
    for i, v in enumerate(values):
        ax.text(v + 0.5, i, f"{v:.1f} h", va='center', fontsize=8)

fig, axes = plt.subplots(1, 2, figsize=(16, 14))
fig.suptitle("Average Sick Leave Across Job Titles", fontsize=18, fontweight='bold')

axes[0].barh(top10.index, top10.values, height = 0.8)
axes[0].set_title("Top 10 Job Titles by Average Sick Leave(hours)", fontweight='bold')
axes[0].invert_yaxis() 
axes[0].set_xlim(0, top10.max() * 1.1)
annotate_bars(axes[0], top10.values)

axes[1].barh(bot10.index, bot10.values, height = 0.8)
axes[1].set_title("Bottom 10 Job Titles by Average Sick Leave(hours)", fontweight='bold')
axes[1].invert_yaxis()
axes[1].set_xlim(0, bot10.max() * 1.15)
annotate_bars(axes[1], bot10.values)

plt.tight_layout(rect=[0.03, 0, 1, 0.97]) 

# -------- SickLeave_per department and per group --------
#  didn't find anything intresting, didn't include in the final report

avg_sick_leave_d = mean_d = df.groupby("Department")["SickLeaveHours"].mean().sort_values(ascending=False)
avg_sick_leave_g = mean_g = df.groupby("GroupName")["SickLeaveHours"].mean().sort_values(ascending=False)


plt.figure()
plt.barh(avg_sick_leave_d.index, avg_sick_leave_d.values)
plt.title("Average Sick Leave per Department", fontsize=18, fontweight='bold')
ax = plt.gca()
annotate_bars(ax, avg_sick_leave_d.values)
plt.tight_layout(rect=[0.01, 0, 1, 1]) 

plt.figure()
plt.barh(avg_sick_leave_g.index, avg_sick_leave_g.values)
plt.title("Average Sick Leave per Group", fontsize=18, fontweight='bold')
ax = plt.gca()
annotate_bars(ax, avg_sick_leave_g.values)
plt.tight_layout(rect=[0.01, 0, 1, 1]) 

plt.show()





