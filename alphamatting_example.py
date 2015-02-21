import pandas as pd
from bs4 import BeautifulSoup
import requests

columns = ['Method',
           'overall rank',
           'Avg small rank',
           'Avg large rank',
           'Avg user rank',
           'Troll small',
           'Troll large',
           'Troll user',
           'Doll small',
           'Doll large',
           'Doll user',
           'Donkey small',
           'Donkey  large',
           'Donkey user',
           'Elephant small',
           'Elephant large',
           'Elephant user',
           'Plant small',
           'Plant large',
           'Plant user',
           'Pineapple small',
           'Pineapple large',
           'Pineapple user',
           'Plasticbag small',
           'Plasticbag large',
           'Plasticbag user',
           'Net small',
           'Net large',
           'Net user']

# read saved file instead if looking at private results table
url = 'http://alphamatting.com/eval_25.php'
data = requests.get(url).content

# remove blue ranking tags
soup = BeautifulSoup(data, 'html5')
for h in soup.findAll(attrs={'class' : 'rank'}):
    h.extract()

# {'id' : 'errortable'} identifies the table - look at page source if this changes
df = pd.read_html(str(soup), attrs={'id' : 'errortable'}, parse_dates=False)[0]
df.rename(columns=dict(enumerate(columns)), inplace=True)

# save to latex table
with open('alphamatting_sad_table', 'w') as f:
    df.to_latex(f)
