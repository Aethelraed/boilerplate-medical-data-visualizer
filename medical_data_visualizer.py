import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv")

# 2
bmi = df.weight/ ((df.height/100)**2)
df['overweight'] = [1 if b > 25 else 0  for b in bmi]

# 3
df.gluc = [0 if g == 1 else 1 for g in df.gluc]
df.cholesterol = [0 if c == 1 else 1 for c in df.cholesterol]
df["id"] = df.index



# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
        id_vars = ["cardio"],
        value_vars=["active","alco","cholesterol","gluc","overweight","smoke","cardio"])


    # 6
    #df_cat = None
    

    # 7
    pdf = df_cat
    pdf.groupby("value").head()
    pdf.head()


    # 8
    fig = sns.catplot(data=df_cat, 
    x="variable", hue="value", col="cardio",
    kind="bar",errorbar=None)


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
