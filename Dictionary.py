sales = [{'country': "India", 'sale': 150.5}, {'country': "China", 'sale': 200.2}, {'country': "US", 'sale': 300.3}, {'country': "UK", 'sale':210.4}]

country_key = map(lambda x: x['country'], sales)
print(list(country_key))

country_values = map(lambda x: x['sale'], sales)
print(list(country_values))
