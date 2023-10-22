import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitajte CSV datoteku sa eksplicitno definisanim tipovima podataka
data = pd.read_csv("samogamma-/metropoliten.csv", encoding='utf-8', low_memory=False, dtype={
    'actor.id': str,
    'Course': str,
    'result.score.scaled': float,
    'result.success': str,
    'result.completion': str,
    'timestamp': str  # zadržavamo string za datum i vreme
})

data['result.score.scaled'].fillna(np.nan, inplace=True)

# Dodajte indeksiranje na kolone 'actor.id' i 'Course'
data.set_index(['actor.id', 'Course'], inplace=True)

# Filtrirajte podatke gde je verb.display = 'completed' ili 'scored'
filtered_data = data[(data['verb.display'] == 'completed') | (data['verb.display'] == 'scored')]

# Grupišite podatke po indeksiranim kolonama i izračunajte COUNT i SUM
result = filtered_data.groupby(['actor.id', 'Course']).agg(
    total_activities_completed=pd.NamedAgg(column='verb.display', aggfunc='count'),
    total_points_scored=pd.NamedAgg(column='result.score.scaled', aggfunc='sum')
).reset_index()

# Prikaz rezultata
print(result)

# Izrada grafa
plt.figure(figsize=(10, 6))
plt.scatter(result['total_activities_completed'], result['total_points_scored'])
plt.xlabel('Broj završenih aktivnosti')
plt.ylabel('Ukupni broj bodova')
plt.title('Napredak studenata')
plt.grid(True)
plt.show()