import os
import re
import operator

class logParser():
    def __init__(self, filepath):
        self.filepath = filepath

    def getPlayerChampMap(self, summonerName):
        champMap = {}
        for filename in os.listdir(self.filepath):
            file = open(self.filepath +"\\"+ filename, 'r', encoding="cp852")
            data = file.readline()
            counter = 0
            while data != '':
                if "created for " + summonerName in data:
                    champPlayed = re.split("(.*Hero )(.*)(\(.*created for )(.*)", data)[2]
                    if champPlayed not in champMap:
                        champMap[champPlayed] = 1
                    else:
                        champMap[champPlayed]+=1
                    if "Total" not in champMap:
                        champMap["Total"] = 1
                    else:
                        champMap["Total"] += 1
                    counter +=1
                if counter >= 10:
                    break
                data = file.readline()
        return champMap

    def getSortedPlayerChampPairVector(self, summonerName):
        champMap = self.getPlayerChampMap(summonerName)
        sortedchampMap = sorted(champMap.items(), key=operator.itemgetter(1), reverse=True)
        return sortedchampMap

    def getPlayersMap(self):
        playersMap = {}
        for filename in os.listdir(self.filepath):
            file = open(self.filepath +"\\"+ filename, 'r', encoding="cp852")
            data = file.readline()
            counter = 0
            while data != '':
                if "created for " in data:
                    summonerName = re.split("(.*Hero )(.*)(\(.*created for )(.*)", data)[4]
                    if summonerName not in playersMap:
                        playersMap[summonerName] = { "total": 1}
                    else:
                        playersMap[summonerName]["total"] += 1
                    champPlayed = re.split("(.*Hero )(.*)(\(.*created for )(.*)", data)[2]
                    if champPlayed not in playersMap[summonerName]:
                        playersMap[summonerName][champPlayed] = 1
                    else:
                        playersMap[summonerName][champPlayed]+=1
                    counter +=1
                if counter >= 10:
                    break
                data = file.readline()
        return playersMap
