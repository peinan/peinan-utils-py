import re
from typing import List

import MeCab


class Parser:
    def __init__(self):
        self.feature_columns = [
            '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3',
            '活用型', '活用形', '基本形', '読み', '発音',
        ]
        self.stopwords = []
        self.content_pos = ['名詞', '動詞', '形容詞', '副詞', '連体詞']
        self.eos = ['。', '？', '！', '．', '\?', '\!']
        self.ptn_eos = re.compile(f'({"|".join(self.eos)})')
        self.tagger = MeCab.Tagger()
        self.tagger.parse('')

    def set_dict(self, dict_path: str):
        self.dict_path = dict_path
        self.tagger = MeCab.Tagger(f'-d {self.dict_path}')

    def set_stopwords(self, stopwords: list):
        self.stopwords = stopwords

    def set_content_pos(self, content_pos: list):
        self.content_pos = content_pos

    def set_eos(self, eos: list):
        self.eos = eos

    def parse(self, text: str, only_content_words: bool = False, fit_stopwords: bool = False) -> List[dict]:
        results = []
        for node in self.tagger.parse(text).rstrip('\n').splitlines():
            if node == 'EOS' or node == '':
                continue

            surface, feature = node.split('\t')
            features = feature.split(',')

            if only_content_words:
                if features[0] in self.content_pos:
                    results.append({'surface': surface, 'features': features})
            elif fit_stopwords:
                if surface not in self.stopwords:
                    results.append({'surface': surface, 'features': features})
            else:
                results.append({'surface': surface, 'features': features})

        return results

    def get_surfaces(self, text: str, only_content_words: bool = False, fit_stopwords: bool = False) -> List[str]:
        return [ res['surface'] for res in self.parse(text,
                                                      only_content_words=only_content_words,
                                                      fit_stopwords=fit_stopwords) ]

    def split_to_lines(self, text: str) -> List[str]:
        return re.sub(self.ptn_eos, '\g<1>\n', text.replace('\n', '').rstrip()).splitlines()

