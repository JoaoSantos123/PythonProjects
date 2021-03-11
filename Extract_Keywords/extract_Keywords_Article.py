#Project 3.1 - Extract Keywords Article

#rake-nltk short for Rapid Automatic Keyword Extraction algorithm
from rake_nltk import Rake

r = Rake()

text = " The Platform of the Future? \
\
The survival of any organization depends on its ability to outperform competitors and marketplaces in attracting and rewarding talent, ideas and capital. As communication and transaction costs have drastically declined because of the internet, new platforms have emerged, delivering goods and services at a speed and efficiency previously unimaginable. These new digital players took advantage of the changes in the underlying technology to challenge established business models and rethink pre-existing value chains. The ones that succeeded did so because they achieved a level of efficiency that their brick and mortar counterparts had trouble replicating. Through online reputation and feedback systems, digital players were able to create global marketplaces where individuals, products and services could be matched more effectively than ever before. By providing curation and ensuring the safety of transactions, these new types of intermediaries were able to reap the returns of this first wave of digitization. \
\
A similar transformation is about to happen as blockchain technology and cryptocurrencies mature and mainstream applications emerge. Under this new wave of technological change, intermediaries will still be able to add value to transactions, but the nature of intermediation will fundamentally change. Whereas some established players will be able to use this opportunity to further scale their operations, others will be challenged by new entrants proposing entirely new approaches to value creation and value capture.\
\
Complementing Artificial Intelligence with Human Intelligence "

#Extraction given a text
r.extract_keywords_from_text(text)

#Extraction given the list of strings where is a sentence
myList = ["ability to outperform", "blockchain", "suvival organization", "cryptocurrencies emerge", "artifical intelligence blockchain"]
r.extract_keywords_from_sentences(myList)

#To get Keyword phrases ranked highest to lowest
r.get_ranked_phrases()

#To get Keyword phrases ranked highest to lowest with scores
print(r.get_ranked_phrases_with_scores())


