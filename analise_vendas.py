import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/vendas.csv", parse_dates=["data"])

print("RECEITA TOTAL:", round(df["receita"].sum(), 2))
print("LUCRO TOTAL:", round(df["lucro"].sum(), 2))
print("MARGEM MÉDIA:", round(df["margem"].mean(), 2), "%")

print("\nReceita por produto:")
print(df.groupby("produto")["receita"].sum().sort_values(ascending=False))

print("\nReceita por região:")
print(df.groupby("regiao")["receita"].sum().sort_values(ascending=False))

print("\nMargem média por categoria:")
print(df.groupby("categoria")["margem"].mean().sort_values(ascending=False))
