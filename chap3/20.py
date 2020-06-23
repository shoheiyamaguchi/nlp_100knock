import json
file_path = './jawiki-country.json'
with open(file_path) as data_file:
    for line in data_file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            print(data['text'])
            break
