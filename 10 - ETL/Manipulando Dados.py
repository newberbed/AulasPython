#importando uma tabela utilizando panda
import pandas as pd
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
df1 = pd.read_csv(url)
df1.head()

#importando a biblioteca pandas e um dataset
import pandas as pd
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
sf.head()
