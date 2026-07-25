import pandas as pd
df = pd.read_csv("data/ucb_admissions.csv")
df["Total"] = df.Admitted + df.Rejected
df["Rate"] = df.Admitted / df.Total

# Aggregate by gender
agg = df.groupby("Gender").agg(Admitted=("Admitted","sum"), Total=("Total","sum"))
agg["Rate"] = agg.Admitted/agg.Total
print("=== OVERALL (aggregate) ===")
print((agg["Rate"]*100).round(1).to_string())

# By department
print("\n=== BY DEPARTMENT ===")
piv = df.pivot_table(index="Dept", columns="Gender", values="Rate")
piv = (piv*100).round(1)
piv["F>M"] = piv["Female"] > piv["Male"]
print(piv.to_string())
print("\nDepts where Female rate > Male rate:", int(piv["F>M"].sum()), "of", len(piv))

# Dept applicant volume by gender
print("\n=== APPLICANT VOLUME (Total apps per dept by gender) ===")
vol = df.pivot_table(index="Dept", columns="Gender", values="Total", aggfunc="sum")
print(vol.to_string())
# Overall admit rate per dept and where women applied
dept_rate = df.groupby("Dept").apply(lambda g: g.Admitted.sum()/g.Total.sum(), include_groups=False)
print("\n=== DEPT OVERALL ADMIT RATE ===")
print((dept_rate*100).round(1).to_string())
