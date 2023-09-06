'''
Assignment no 1:
Name:Pawar Kalyani Kacharu
Batch:B4
Roll no: 73
Title: "Text Pre-processing using NLP operations : Perform Sentence detection ,
        Tokenization, Lemmatization , Part of speech tagging"
'''
#import library
import spacy

#load dictionary
nlp = spacy.load("en_core_web_sm")

#sample input
conference_help_text = (
    "Backgammon is one of the oldest known board games." 
    "Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East."  
    "t is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice."

)

#sentence Detection
about_doc = nlp(conference_help_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")


#Tokenization
about_doc = nlp(conference_help_text)

for token in about_doc:
    print (token, token.idx)



#lemmatization
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")




#part of speech tagging
about_doc = nlp(conference_help_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

#output:
'''

------Sentence Detection-----

Backgammon is one of the...
Its history can be traced...

------Tokenization------

Backgammon 0
is 11
one 14
of 18
the 21
oldest 25
known 32
board 38
games 44
. 49
Its 50
history 54
can 62
be 66
traced 69
back 76
nearly 81
5,000 88
years 94
to 100
archeological 103
discoveries 117
in 129
the 132
Middle 136
East.t 143
is 150
a 153
two 155
player 159
game 166
where 171
each 177
player 182
has 189
fifteen 193
checkers 201
which 210
move 216
between 221
twenty 229
- 235
four 236
points 241
according 248
to 258
the 261
roll 265
of 270
two 273
dice 277
. 281

------Lemmatization-----

                  is : be
               known : know
               games : game
                 Its : its
              traced : trace
               years : year
         discoveries : discovery
              Middle : middle
              East.t : east.t
                  is : be
                 has : have
            checkers : checker
              points : point
           according : accord

 ------Part of speech-----          

TOKEN: Backgammon
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: one
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: oldest
=====
TAG: RBS        POS: ADV
EXPLANATION: adverb, superlative

TOKEN: known
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: board
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: games
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Its
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: history
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: be
=====
TAG: VB         POS: AUX
EXPLANATION: verb, base form

TOKEN: traced
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: back
=====
TAG: RP         POS: ADP
EXPLANATION: adverb, particle

TOKEN: nearly
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: 5,000
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: years
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: to
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: archeological
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: discoveries
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: in
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Middle
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: East.t
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: two
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: player
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: game
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: where
=====
TAG: WRB        POS: SCONJ
EXPLANATION: wh-adverb

TOKEN: each
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: player
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: has
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: fifteen
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: checkers
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: which
=====
TAG: WDT        POS: PRON
EXPLANATION: wh-determiner

TOKEN: move
=====
TAG: VBP        POS: VERB
EXPLANATION: verb, non-3rd person singular present

TOKEN: between
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: twenty
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: -
=====
TAG: HYPH       POS: PUNCT
EXPLANATION: punctuation mark, hyphen

TOKEN: four
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: points
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: according
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: to
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: roll
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: two
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: dice
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: .
=====
TAG: .          POS: PUNCT'''