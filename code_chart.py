import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {
    'Company': ['Target','UnitedHealth','Medtronic','U.S. Bank','Arctic Wolf','CrowdStrike','Rapid7','Mayo Clinic','Best Buy','Optum'],
    'Salary': [90000, 95000, 92000, 91000, 97000, 100000, 98000, 93000, 89000, 96000],
    'WLB': [4.0, 4.2, 4.1, 3.9, 4.0, 4.1, 4.0, 4.3, 4.0, 4.2]
}

df = pd.DataFrame(data)

# Bar chart: Salary vs WLB
fig, ax1 = plt.subplots(figsize=(12,6))

ax2 = ax1.twinx()

width = 0.4
x = range(len(df['Company']))

ax1.bar(x, df['Salary'], width, color='skyblue', label='Salary ($)')
ax2.bar([i + width for i in x], df['WLB'], width, color='lightgreen', label='WLB (1-5)')

ax1.set_xticks([i + width/2 for i in x])
ax1.set_xticklabels(df['Company'], rotation=45, ha='right')
ax1.set_ylabel('Salary ($)')
ax2.set_ylabel('Work-Life Balance (1-5)')

fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.title('Salary vs Work-Life Balance by Company')
plt.tight_layout()
plt.savefig('charts/salary_vs_wlb.png')
plt.show()
