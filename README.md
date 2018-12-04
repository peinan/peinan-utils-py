# An util package for myself

![](https://img.shields.io/badge/version-0.0.2-green.svg?style=flat-square) ![](https://img.shields.io/badge/python-3.6+-green.svg?style=flat-square) ![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

Mostly about NLP.

## Install

```bash
$ pip install -e git+https://github.com/peinan/peinan-utils-py#egg=peinan-utils
```

## Usages & Features

### Parser

```python
# sample text
>>> text = 'こんにちは！今日はいい天気ですね。これからどちらへ？'

>>> from peinan_utils import Parser
>>> p = Parser()

# just parse input texts and get information about surfaces and features
>>> p.parse(text)
[{'surface': 'こんにちは',
  'features': ['感動詞', '*', '*', '*', '*', '*', 'こんにちは', 'コンニチハ', 'コンニチワ']},
 {'surface': '！', 'features': ['記号', '一般', '*', '*', '*', '*', '！', '！', '！']},
 {'surface': '今日',
  'features': ['名詞', '副詞可能', '*', '*', '*', '*', '今日', 'キョウ', 'キョー']},
 {'surface': 'は',
  'features': ['助詞', '係助詞', '*', '*', '*', '*', 'は', 'ハ', 'ワ']},
 {'surface': 'いい',
  'features': ['形容詞', '自立', '*', '*', '形容詞・イイ', '基本形', 'いい', 'イイ', 'イイ']},
 {'surface': '天気',
  'features': ['名詞', '一般', '*', '*', '*', '*', '天気', 'テンキ', 'テンキ']},
 {'surface': 'です',
  'features': ['助動詞', '*', '*', '*', '特殊・デス', '基本形', 'です', 'デス', 'デス']},
 {'surface': 'ね',
  'features': ['助詞', '終助詞', '*', '*', '*', '*', 'ね', 'ネ', 'ネ']},
 {'surface': '。', 'features': ['記号', '句点', '*', '*', '*', '*', '。', '。', '。']},
 {'surface': 'これから',
  'features': ['副詞', '助詞類接続', '*', '*', '*', '*', 'これから', 'コレカラ', 'コレカラ']},
 {'surface': 'どちら',
  'features': ['名詞', '代名詞', '一般', '*', '*', '*', 'どちら', 'ドチラ', 'ドチラ']},
 {'surface': 'へ',
  'features': ['助詞', '格助詞', '一般', '*', '*', '*', 'へ', 'ヘ', 'エ']},
 {'surface': '？', 'features': ['記号', '一般', '*', '*', '*', '*', '？', '？', '？']}]

# get surfaces of input text
>>> p.get_surfaces(text)
['こんにちは', '！', '今日', 'は', 'いい', '天気', 'です', 'ね', '。', 'これから', 'どちら', 'へ', '？']

# get only content words of input text
>>> p.get_surfaces(text, only_content_words=True)
['今日', 'いい', '天気', 'これから', 'どちら']

# split input text into lines
>>> p.split_to_lines(text)
['こんにちは！', '今日はいい天気ですね。', 'これからどちらへ？']

# change dictonary path
>>> sumomo = 'すもももももももものうち'
>>> p.get_surfaces(sumomo)
['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち']

>>> p.set_dict('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
>>> p.get_surfaces(sumomo)
['すもももももももものうち']
```

### Vectorizer

```python
# sample text
>>> text = '今日はいい天気ですね。これからどちらへ？'

>>> from peinan_utils import Vectorizer
>>> v = Vectorizer()

# make word ngram (the default n is 2)
>>> v.make_word_ngram(text)
[[('今日', 'は'), ('は', 'いい'), ('いい', '天気'), ('天気', 'です'), ('です', 'ね'), ('ね', '。')], [('これから', 'どちら'), ('どちら', 'へ'), ('へ', '？')]]

# specify n
>>> v.make_word_ngram(text, n=3)
[[('今日', 'は', 'いい'), ('は', 'いい', '天気'), ('いい', '天気', 'です'), ('天気', 'です', 'ね'), ('です', 'ね', '。')], [('これから', 'どちら', 'へ'), ('どちら', 'へ', '？')]]

# use BOS and EOS (the default BOS and EOS are '<s>' and </s>, respectively)
>>> v.make_word_ngram(text, n=3, bos=v.BOS, eos=v.EOS)
[[('<s>', '今日', 'は'), ('今日', 'は', 'いい'), ('は', 'いい', '天気'), ('いい', '天気', 'です'), ('天気', 'です', 'ね'), ('です', 'ね', '。'), ('ね', '。', '</s>')], [('<s>', 'これから', 'どちら'), ('これから', 'どちら', 'へ'), ('どちら', 'へ', '？'), ('へ', '？', '</s>')]]

# make character ngram (the default n is 2)
>>> v.make_char_ngram(text, n=2)
[[('今', '日'), ('日', 'は'), ('は', 'い'), ('い', 'い'), ('い', '天'), ('天', '気'), ('気', 'で'), ('で', 'す'), ('す', 'ね'), ('ね', '。')], [('こ', 'れ'), ('れ', 'か'), ('か', 'ら'), ('ら', 'ど'), ('ど', 'ち'), ('ち', 'ら'), ('ら', 'へ'), ('へ', '？')]]
```

### Matplotlib Utils

```python
# just import this package and then you can plot with Japanese font
>>> import matplotlib.pyplot as plt
>>> import peinan_utils

# set background face color
>>> fig = plt.figure()
>>> fig.patch.set_facecolor('white')

# plot with Japanese labels
>>> plt.plot([1,2,3], [1,2,3])
>>> plt.xlabel('x軸')
>>> plt.ylabel('y軸')
>>> plt.show()
```

![](https://raw.githubusercontent.com/peinan/peinan-utils-py/master/images/plot_result.png)
