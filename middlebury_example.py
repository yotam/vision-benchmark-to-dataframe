import pandas as pd
from bs4 import BeautifulSoup
import requests

columns = [
    'Method',
    'avg. rank',
    'Army all',
    'Army disc',
    'Army untext',
    'Mequon all',
    'Mequon disc',
    'Mequon untext',
    'Schefflera all',
    'Schefflera disc',
    'Schefflera untext',
    'Wooden all',
    'Wooden disc',
    'Wooden untext',
    'Grove all',
    'Grove disc',
    'Grove untext',
    'Urban all',
    'Urban disc',
    'Urban untext',
    'Yosemite all',
    'Yosemite disc',
    'Yosemite untext',
    'Teddy all',
    'Teddy disc',
    'Teddy untext']

# read saved file instead if looking at private results table
url = 'http://vision.middlebury.edu/flow/eval/results/results-e1.php'
data = requests.get(url).content

# remove blue ranking tags
soup = BeautifulSoup(data, 'html5')
for h in soup.findAll(attrs={'class' : 'rank'}):
    h.extract()

# {'class' : 'gr'} identifies the table - look at page source if this changes
df = pd.read_html(str(soup), attrs={'class' : 'gr'}, parse_dates=False)[0]
df.rename(columns={i : c for i, c in enumerate(columns)}, inplace=True)

# save to latex table
with open('middlebury_epe_table', 'w') as f:
    df.to_latex(f)
