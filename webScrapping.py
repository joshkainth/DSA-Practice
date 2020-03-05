# Web Scrapping with open hashing
import requests as rqt
from bs4 import BeautifulSoup
import hashlib

class TeamRecords:
    def __init__(self, team_name, total, won, lost,
                 tied, abandoned, points, net_run_rate, score_for, score_against):
        self.team_name = team_name
        self.total = total
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.net_run_rate = net_run_rate
        self.score_for = score_for
        self.score_against = score_against

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(
            self.team_name, self.total, self.won, self.lost,
            self.tied, self.abandoned, self.points, self.net_run_rate, self.score_for, self.score_against)

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(capacity):
            objects = []
            self.table.append(objects)

    def hash_function(self, key):
        hash_code = int(hashlib.sha256(key.encode("utf-8")).hexdigest(), 16) % 8
        return hash_code

    def put(self, team):
        key = team.team_name
        index = self.hash_function(key)

        self.size +=1
        self.table[index].append(team)
        print("{} Team Added at index {}".format(team.team_name,index))

    def iterate(self):
        for i in range(0, len(self.table)):
            if len(self.table[i]) != 0:
                print("--Index at {}---".format(i))
                for data in self.table[i]:
                    print(data)
                # print("----------------")

web_url = "https://www.espncricinfo.com/table/series/8048/season/2019/indian-premier-league"
response = rqt.get(web_url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
span_tags = soup.find_all("span", class_="team-names")
td_tags = soup.find_all("td", class_="")

team_score = []
for tags in td_tags:
    team_score.append(tags.text)

i=0
team_data = []
hTable = HashTable(len(span_tags))

for names in span_tags:
    team_object = TeamRecords(names.text, team_score[i], team_score[i+1], team_score[i+2], team_score[i+3], team_score[i+4], team_score[i+5],
                       team_score[i+6], team_score[i+7], team_score[i+8])
    team_data.append(team_object.__str__())

    hTable.put(team_object)

    i += 9


print()
hTable.iterate()
print()
print(hTable.table)
