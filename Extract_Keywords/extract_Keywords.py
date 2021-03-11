#Project 3 - Extract Keywords

#rake-nltk short for Rapid Automatic Keyword Extraction algorithm
from rake_nltk import Rake

r = Rake()

text = "Ola o meu nome é João e tenho 23 anos. Sou estudante de engenharia e tenho uma paixão enorme pelas matemáticas e pela programação"

r.extract_keywords_from_text(text)

keyword_extract = r.get_ranked_phrases()

print(keyword_extract)
