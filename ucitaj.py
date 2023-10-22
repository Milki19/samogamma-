import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Učitajte CSV datoteku i indeksirajte kolonu 'verb.display'
data = pd.read_csv("samogamma-/metropoliten.csv", encoding='iso-8859-1')
data = data.set_index('verb.display')

# Kreirajte funkciju za računanje broja 'submited' vrednosti
def calculate_submited_count(filter_value):
    submited_count = data[data.index == filter_value].groupby('object.definition.name').size()
    return submited_count

# Endpoint za Chart 1 podatke
@app.route('/api/chart1-data')
def chart1_data():
    submited_count = calculate_submited_count('completed')
    chart_data = [{"Course": index, "total_points_scored": value} for index, value in submited_count.items()]
    return jsonify(chart_data)

# Endpoint za Chart 2 podatke
@app.route('/api/chart2-data')
def chart2_data():
    submited_count = calculate_submited_count('in_progress')
    chart_data = [{"Course": index, "total_points_scored": value} for index, value in submited_count.items()]
    return jsonify(chart_data)

# Endpoint za Chart 3 podatke
@app.route('/api/chart3-data')
def chart3_data():
    submited_count = calculate_submited_count('not_started')
    chart_data = [{"Course": index, "total_points_scored": value} for index, value in submited_count.items()]
    return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)
