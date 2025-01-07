import pandas as pd
# countries = pd.Series(
#     data = ['Англия', 'Канада', 'США'],
#     index = ['UK', 'CA', 'US'],
#     name = 'countries'
# )
# print(countries)
# print(countries.loc['UK'])
# print(countries.loc[['UK', 'US']])
# print(countries.iloc[1])
# print(countries.iloc[1:])

# В аптеку поступают партии лекарств. Их названия находятся в списке names, количество единиц товара находится в списке counts.
# Например:
# names = ['chlorhexidine', 'cyntomycin', 'afobazol']
# counts = [15, 18, 7]
# Напишите функцию create_medications(names, counts), которая создает Series medications, 
# индексами которой являются названия лекарств names, а значениями - их количество в поставке counts.
# А также напишите функцию get_percent(medications, name), которая возвращает долю количества товара 
# с именем name от общего количества товаров в поставке в процентах.
# def create_medications(names, counts):
#     medications = pd.Series(
#         data = counts,
#         index = names,
#         name = 'medications'
#     )
#     print(medications)
#     def get_percent(medications, name):
#         count = medications.loc[name]/sum(medications.iloc[:])*100
#         print(name, count)
#     get_percent(medications, 'afobazol')
# create_medications(names, counts)

# countries_df = pd.DataFrame({
#     'country': ['Англия', 'Канада', 'США'],
#     'population': [56, 38, 322],
#     'area': [133, 998, 982]
# })
# print(countries_df)
# print(countries_df.mean(axis=0, numeric_only=True))
# print(countries_df['population'])
# print(countries_df.loc[0, 'area'])
# print(countries_df.loc[2, ['population', 'area']])
# print(countries_df.iloc[:2, 2:])

# weather = pd.DataFrame(
#     data = [
#         ['Москва', -4, -9],
#         ['Петербург', 2, -8],
#         ['Улан-Удэ', -23, -36]
#     ],
#     columns = ['city', 'present', 'last'],
#     index = ['Msk', 'Spb', 'UU']
# )
# print(weather)

# Вы работаете аналитиком в компании ScienceYou. Ваша задача — проанализировать чистую прибыль.
# Доходы (income), расходы (expenses) и годы (years), соответствующие им, предоставлены вам в виде списков.
# Например:
# income = [478, 512, 196]
# expenses = [156, 130, 270]
# years = [2018, 2019, 2020]
# Создайте функцию create_companyDF(income, expenses, years), которая возвращает DataFrame, 
# составленный из входных данных со столбцами Income и Expenses и индексами, соответствующими годам рассматриваемого периода.
# Пример такого DataFrame представлен ниже.
#     Income  Expenses
# 2018    478     156
# 2019    512     130
# 2020    196     270
# Также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, 
# записанными в таблице df, за год year.
# Примечание. Если информация за запрашиваемый год не указана в вашей таблице, вам необходимо вернуть None.
# def create_companyDF(income, expenses, years):
#     table = pd.DataFrame({
#         'income': income,
#         'expenses': expenses
#     })
#     table.index = years
#     print(table)
#     def get_profit(table, year):
#         if year in table.index:
#             profit = table.loc[year, 'income'] - table.loc[year, 'expenses']
#             print(profit)
#         else:
#             print(None)
#     get_profit(table, 2019)
# create_companyDF(income, expenses, years)
import numpy as np
oleg = np.random.randint(1, 51)
dima = np.random.randint(1, 51)
print(f'Олег - {oleg}, Дима - {dima}')