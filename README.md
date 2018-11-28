# A util package for myself

Mostly about NLP.

## Install

```bash
$ pip install -e git+https://github.com/peinan/peinan-utils-py
```

## Usage

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
