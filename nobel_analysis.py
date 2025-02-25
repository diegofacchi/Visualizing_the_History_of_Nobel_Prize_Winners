import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

nobel = pd.read_csv("D:/diego/Documents/MyProjects/Visualizing_the_History_of_Nobel_Prize_Winners/nobel.csv")

top_gender = nobel["sex"].value_counts().index[0]
top_country = nobel["birth_country"].value_counts().index[0]

print(f"\nThe gender with the most laureates is: {top_gender}.\n")
print(f"The most common birth country of Nobel laureates is: {top_country}.\n")

nobel["us_born_winners"] = nobel["birth_country"] == "United States of America"
nobel["decade"] = (np.floor(nobel["year"] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby("decade", as_index=False)["us_born_winners"].mean()

max_decade_usa = prop_usa_winners[prop_usa_winners["us_born_winners"] == prop_usa_winners["us_born_winners"].max()]["decade"].values[0]

ax1 = sns.relplot(x="decade", y="us_born_winners", data=prop_usa_winners, kind="line")

nobel["female_winners"] = nobel["sex"] == "Female"
prop_female_winners = nobel.groupby(["decade", "category"], as_index=False)["female_winners"].mean()

max_female_decade_category = prop_female_winners[prop_female_winners["female_winners"] == prop_female_winners["female_winners"].max()][["decade", "category"]]

max_female_dict = {max_female_decade_category["decade"].values[0]: max_female_decade_category["category"].values[0]}

ax2 = sns.relplot(x="decade", y="female_winners", data=prop_female_winners, kind="line", hue="category")

plt.show()

nobel_women = nobel[nobel["female_winners"]]
min_row = nobel_women[nobel_women["year"] == nobel_women["year"].min()]

first_woman_name = min_row["full_name"].values[0]
first_woman_category = min_row["category"].values[0]

print(f"The first woman to win a Nobel prize was {first_woman_name} in the category of {first_woman_category}.\n")

counts = nobel["full_name"].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)

print(f"The repeats winners are: {repeat_list}.\n")