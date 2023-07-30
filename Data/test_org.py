import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def show_ents(doc):
  if doc.ents:
    for ent in doc.ents:
      print(ent.text + ' - ' + str(ent.start_char) + ' - ' +  str(ent.end_char) + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_ )))
  else:
    print("No named entities found.")

speechFile="2021.txt"
peopleFile="2021_Organization.csv"

with open(speechFile, 'r', encoding='UTF-8') as f:
    doc = nlp(f.read())

f.close()

personList = []
for ent in doc.ents:
    if ent.label_ == "ORG":
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


