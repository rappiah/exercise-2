import inputdata
import numpy
data = inputdata.raw_scores
def prep_data(raw_scores):
people = all_scores.keys()
  people.sort()
print people
people.sort()
print people
papers = set()
for person in people:
    for title in raw_scores[person].keys():
      papers.add(title)
        papers = list(papers)
             papers.sort()
                ratings = numpy.zeros((len(people), len(papers)))
for (person_id, person) in enumerate(people):
    for (title_id, title) in enumerate(papers):
      r = scores[person].get(title, 0)
      ratings[person_id, title_id] = float(r)
print ratings
papers.sort()
print papers


