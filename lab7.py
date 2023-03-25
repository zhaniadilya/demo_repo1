"""dict1 = {'city1': 'Almaty', 'city2': 'Oral', 'city3': 'Nur-Sultan', 'city4': 'Atyrau', 'city5': 'Semey'}
del dict1['city5']
print('First dictionary: ', dict1)
print('------------------------------------------------------------')
dict1.update({'city6': 'Aktau'})
print('After updating: ', dict1)
print('------------------------------------------------------------')
print('Result of the get method: ', dict1.get('city5', 'Key error!'))
print('------------------------------------------------------------')
print('Dictionary keys: ', dict1.keys())
print('------------------------------------------------------------')
print('Dictionary keys and values: ', dict1.items())
"""
#1-tapsyrma
rivers = {'Yenisei River': 'China', 'Mississippi': 'USA', 'Amazon': 'South America', 'Ile': 'Kazakhstan', 'Murray-Darling': 'Australia'}
print('River            Country')
for i in rivers:
    print(i, '  ---  ', rivers[i])
print('------------------------------------------------------------')
river = input('Enter river name: ')
print('Result of the get method: ', rivers.get(river, 'This river not found!'))
print('------------------------------------------------------------')
river_key = input('Enter river name: ')
river_city = input('Enter this river''s country: ' )
rivers[river_key] = river_city
print(rivers)