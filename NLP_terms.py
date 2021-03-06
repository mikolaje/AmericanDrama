# coding=u8

term_dict = {
    "interjection ": "感叹词. oh,wow,ah",
    "lemmatization": "词形还原.  walking->walk, better->good",
    "stemming": "抽取词的词干或词根形式（不一定能够表达完整语义）. played->play",
    "tokenization": "分词",
    "pronoun": "I, you, we, they, he, she, it, me, us, them, him, her, this",
    "part-of-speech": "单词在句子中的作用。The part of speech explains how a word is used in a sentence. There are eight main parts of speech - nouns, pronouns, adjectives, verbs, adverbs, prepositions, conjunctions and interjections.",
    "chunking": "use phrases such as “South Africa” as a single word instead of ‘South’ and ‘Africa’ separate words."
}




tags_explain = [
    ('CC', 'conjunction, coordinating',	'and, or, but'),
    ('CD',	'cardinal number',	'five, three, 13%'),
    ('DT',	'determiner',	'the, a, these'),
    ('EX',	'existential', 'there	there were six boys'),
    ('FW',	'foreign word',	'mais'),
    ('IN',	'conjunction, subordinating or preposition', 'of, on, before, unless'),
    ('JJ',	'adjective',	'nice, easy'),
    ('JJR',	'adjective, comparative',	'nicer, easier'),
    ('JJS',	'adjective, superlative	', 'nicest, easiest'),
    ('LS',	'list item marker', ''),
    ('MD',	'verb, modal auxillary',	'may, should'),
    ('NN',	'noun, singular or mass',	'tiger, chair, laughter'),
    ('NNS',	'noun, plural',	'tigers, chairs, insects'),
    ('NNP',	'noun, proper singular',	'Germany, God, Alice'),
    ('NNPS',	'noun, proper plural',	'we met two Christmases ago'),
    ('PDT',	'predeterminer',	'both his children'),
    ('POS',	'possessive ending',	"'s"),
    ('PRP',	'pronoun, personal',	'me, you, it'),
    ('PRP$',	'pronoun, possessive',	'my, your, our'),
    ('RB',	'adverb',	'extremely, loudly, hard'),
    ('RBR',	'adverb, comparative',	'better'),
    ('RBS',	'adverb, superlative',	'best'),
    ('RP',	'adverb, particle',	 'about, off, up'),
    ('SYM',	'symbol',	'%'),
    ('TO',	'infinitival to',	'what to do?'),
    ('UH',	'interjection',	 'oh, oops, gosh'),
    ('VB',	'verb, base form',	'think'),
    ('VBZ',	'verb, 3rd person singular present',	'she thinks'),
    ('VBP',	'verb, non-3rd person singular present',	'I think'),
    ('VBD',	'verb, past tense',	 'they thought'),
    ('VBN',	'verb, past participle',	'a sunken ship'),
    ('VBG',	'verb, gerund or present participle	', 'thinking is fun'),
    ('WDT',	'wh-determiner',	'which, whatever, whichever'),
    ('WP',	'wh-pronoun, personal',	 'what, who, whom'),
    ('WP$',	'wh-pronoun, possessive	','whose, whosever'),
    ('WRB',	'wh-adverb',	'where, when'),
    ('.',	'punctuation mark, sentence closer', '.;?*'),
    (',',	'punctuation mark, comma',	','),
    (':',	'punctuation mark, colon',	':'),
    ('(',	'contextual separator, left paren', '('),
    (')',	'contextual separator, right paren', ')')

]

"""
Reference: 
https://www.clips.uantwerpen.be/pages/mbsp-tags
https://medium.com/greyatom/learning-pos-tagging-chunking-in-nlp-85f7f811a8cb

"""


