import MeCab
import re

from typing import List, Tuple


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
            if node == 'EOS':
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


class Vectorizer:
    def __init__(self):
        self.parser = Parser()
        self.BOS = '<s>'
        self.EOS = '</s>'

    def make_word_ngram(self, text: str, n: int = 2, bos: str = None, eos: str = None) -> List[List[Tuple[str]]]:
        """
        Make word ngrams.

        :param text: input text
        :param n: an integer
        :param bos: a string for the beginning of sentence
        :param eos: a string for the end of sentence
        :return: List[List[Tuple]]

        example
        -------

        input: '今日はいい天気ですね。どちらへ行くのです？'
        output (2gram):
        [
            [('今日', 'は'), ('は', 'いい'), ('いい', '天気'), ('天気', 'です'), ('です', 'ね'), ('ね', '。')],
            [('どちら', 'へ'), ('へ', '行く'), ('行く', 'の'), ('の', 'です'), ('です', '？')]
        ]
        """

        assert n > 0, f'n={n} must larger than 0.'
        assert type(n) == int, f'n={n} must be an integer value.'

        sents_surfaces = [ self.parser.get_surfaces(sent) for sent in self.parser.split_to_lines(text) ]
        # sents_surfaces = [ ['w1', 'w2'], ['w3', 'w4'] ]
        if bos:
            # sents_surfaces = [ ['<bos>', 'w1', 'w2'], ['<bos>', 'w3', 'w4'] ]
            sents_surfaces = [ [bos] + surfs for surfs in sents_surfaces ]
        if eos:
            # sents_surfaces = [ ['w1', 'w2', '<eos>'], ['w3', 'w4', '<eos>'] ]
            sents_surfaces = [ surfs + [eos] for surfs in sents_surfaces ]

        if n == 1:
            sents_ngrams = [ [ tuple(surf) for surf in surfs ] for surfs in sents_surfaces ]
            # sents_ngrams = [ tuple(surfs) for surfs in sents_surfaces ]
        else:
            sents_ngrams = []
            for surfs in sents_surfaces:
                sent_length = len(surfs)

                assert n <= sent_length, f'n={n} must smaller than sentence length.'

                sents_ngrams.append([ tuple([ surfs[i+j] for j in range(n) ])
                                      for i in range(sent_length - n + 1) ])

        return sents_ngrams

    def make_char_ngram(self, text: str, n: int = 2) -> List[List[Tuple[str]]]:
        """
        Make char ngrams.

        :param text: input text
        :param n: an integer
        :return: List[List[Tuple]]

        example
        -------

        input: '今日はいい天気ですね。どちらへ行くのです？'
        output (2gram):
        [
            [('今', '日'), ('日', 'は'), ('は', 'い'), ('い', 'い'), ('い', '天'),
             ('天', '気'), ('気', 'で'), ('で', 'す'), ('す', 'ね'), ('ね', '。')],
            [('ど', 'ち'), ('ち', 'ら'), ('ら', 'へ'), ('へ', '行'), ('行', 'く'),
             ('く', 'の'), ('の', 'で'), ('で', 'す'), ('す', '？')]
        ]
        """

        assert n > 0, f'n={n} must larger than 0.'
        assert type(n) == int, f'n={n} must be an integer value.'

        sentences = self.parser.split_to_lines(text)

        if n == 1:
            sents_ngrams = [ [ char for char in sent ] for sent in sentences ]
        else:
            sents_ngrams = []
            for sent in sentences:
                sent_length = len(sent)

                assert n <= sent_length, f'n={n} must smaller than sentence length.'

                sents_ngrams.append([ tuple([ sent[i+j] for j in range(n) ])
                                      for i in range(sent_length - n + 1) ])

        return sents_ngrams
