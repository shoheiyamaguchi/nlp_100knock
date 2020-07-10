import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
print(ukText)
