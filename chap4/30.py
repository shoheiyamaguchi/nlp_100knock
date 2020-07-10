import MeCab

file_path = './neko2.txt'
file_path_parsed = './neko.txt.mecab'


def make_morphemes_dict(text):
    morphemes = []
    for line in text.split("\n"):
        cols = line.split('\t')
        if len(cols) < 2:
            continue
        res_cols = cols[1].split(',')
        morpheme = {
            'surface': cols[0],
            'base': res_cols[6],
            'pos': res_cols[0],
            'pos1': res_cols[1]
        }

        morphemes.append(morpheme)
    return morphemes


tokenizer = MeCab.Tagger()
with open(file_path) as data_file:
    for line in data_file:
        parsed_text = tokenizer.parse(line)
        morpheme = make_morphemes_dict(parsed_text)
        print(morpheme)
        print('\n')
