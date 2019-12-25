import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bqwery-public-data','census-bureau-internatoinal')

QUERY = """
        SELECT country_name, year, sex, max_age FROM bqwery-public-data.census-bureau-internatoinal.midyear_population_age_sex
        LIMIT 10000
        """
        
df = bq_assistant.query_to_pandas(QUERY)

Aruba_ma_b = df[df.country_name == 'Aruba']
bar = plot.bar(Aruba_ma_b, x = 'year', y = 'max_age', label = {'year': 'Year', 'max_age': 'Max_age'}, title = 'Aruba max age per year')
bar.show()