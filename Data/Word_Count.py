from collections import Counter
import spacy
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2500000

WC = []
SW = []
newsyear = "2017"
speechFile = newsyear + ".txt"
wordCountFile = newsyear + ".csv"
peopleFile = newsyear + "_People.csv"
placesFile = newsyear + "_Places.csv"
orgFile = newsyear + "_Organization.csv"
nounFile = newsyear + "_Nouns.csv"

with open("stopwords.txt", "r") as s:
    line = s.read().lower().split()
    # print(line)
    SW.append(line)
SW = str(SW).split()
print(len(SW))

with open(speechFile, 'r', encoding='UTF-8') as f:
    doc = nlp(f.read())

f.close()

with open(speechFile, 'r', encoding='UTF-8') as f:
    text = f.read().lower().split()
    WC = Counter(text)
print("Total Words = " + str(len(text)))
words = str(WC).split(',')

print("Unique Words = " + str(len(words)))
# print(words)
outfile = open(wordCountFile, 'w', encoding='UTF-8')
for w in words:
    found = 0
    for sw in SW:
        curWord = (w.replace('[Counter({', '').replace("'", '').replace(':', ',').replace('})]', '').replace(
            '.', '').replace('?', '').replace('"', '').replace('\n', '').strip() + '\n').split(',')
        curSword = str(sw).replace("'", '').replace(
            ",", '').replace(']]', '').replace('[[', '')
        if curSword == curWord[0]:
            found = 1
    if found == 0:
        outfile.writelines(w.replace('Counter({', '').replace("'", '').replace(
            ':', ',').replace('})]', '').replace('\n', '').strip() + '\n')

personList = []
for ent in doc.ents:
    if ent.label_ == "PERSON":
        personList.append(ent.text)


PC = (Counter(personList))
people = str(PC).split(',')
# print(people)
outfile = open(peopleFile, 'w', encoding='UTF-8')
for PER in people:
    perSplit = PER.split(':')
    name = perSplit[0].replace("'", '').replace('Counter({', '').replace("'", '').replace(
        ':', ',').replace('})]', '').replace('\n', '').replace('"', '').strip()
    nameCount = perSplit[1].replace('})', '')
    outfile.write(name + "," + str(nameCount) + '\n')

placesList = []
for ent in doc.ents:
    if ent.label_ == "GPE":
        placesList.append(ent.text)


PL = (Counter(placesList))
places = str(PL).split(',')
# print(places)

outfile = open(placesFile, 'w', encoding='UTF-8')
for PLA in places:
    if ":" in PLA:
        plaSplit = PLA.split(':')
        name = plaSplit[0].replace("'", '').replace('Counter({', '').replace("'", '').replace(
            ':', ',').replace('})]', '').replace('\n', '').replace('"', '').strip()
        nameCount = plaSplit[1].replace('})', '')
        outfile.write(name + "," + str(nameCount) + '\n')

nounList = []
for token in doc:
    if token.pos_ == "NOUN":
        nounList.append(token.text)


NL = (Counter(nounList))
nouns = str(NL).split(',')
# print(nouns)

outfile = open(nounFile, 'w', encoding='UTF-8')
for NOUN in nouns:
    if ":" in NOUN:
        nounSplit = NOUN.split(':')
        name = nounSplit[0].replace("'", '').replace('Counter({', '').replace("'", '').replace(
            ':', ',').replace('})]', '').replace('\n', '').replace('"', '').strip()
        nounCount = nounSplit[1].replace('})', '')
        outfile.write(name + "," + str(nounCount) + '\n')

orgList = []
for ent in doc.ents:
    if ent.label_ == "ORG":
        orgList.append(ent.text)


OC = (Counter(orgList))
orgs = str(OC).split(',')
# print(orgs)
outfile = open(orgFile, 'w', encoding='UTF-8')
for ORG in orgs:
    orgSplit = ORG.split(':')
    name = orgSplit[0].replace("'", '').replace('Counter({', '').replace("'", '').replace(
        ':', ',').replace('})]', '').replace('\n', '').replace('"', '').strip()
    nameCount = orgSplit[1].replace('})', '')
    outfile.write(name + "," + str(nameCount) + '\n')
