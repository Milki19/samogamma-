import pandas as pd
import matplotlib.pyplot as plt
import functools
from functools import lru_cache

# Učitajte CSV datoteku i indeksirajte kolonu 'verb.display'
data = pd.read_csv("metropoliten.csv", encoding='iso-8859-1')
data = data.set_index('verb.display')

# Kreirajte funkciju za računanje broja 'submited' vrednosti sa memoizacijom
@lru_cache(maxsize=None)
def calculate_submited_count(filter_value):
    submited_count = data[data.index == filter_value].groupby('object.definition.name').size()
    return submited_count

# Pozovite funkciju za brojanje 'submited' vrednosti
submited_count = calculate_submited_count('completed')
print(data['object.definition.name'])



# Prikazivanje grafikona
plt.figure(figsize=(16, 10))
plt.bar(submited_count.index, submited_count)
plt.xlabel('Zadatak')
plt.ylabel('Broj kompletiranih')
plt.title('Broj kompletiranih po zadatku')
plt.xticks(rotation=90)
plt.show()