#Name: Kalyani Pawar
#Roll_No: 73
#Batch No: B4


about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")


#Tokenization
for token in about_doc:
    print (token, token.idx)

#Lemmatization
conference_help_doc = nlp(about_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

#Part-of-Speech Tagging
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

