import re
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
sectionList = re.findall(r'(=+)([^=]+)(=+)\n', ukText)
for section in sectionList:
    ans = f'{section[1]}\t{len(section[0]) - 1}'
    print(ans)
