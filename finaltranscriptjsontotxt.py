import json


ajson = input("Enter file ID: ")


with open("jsoncache/" + ajson + ".json", "r") as f:
    data = json.load(f)

segments = []

for t in data[0]["transcriptions"]:
    segments.append([t["speaker"], t["transcript"]])


with open("files/" + ajson + "-final.txt", 'w') as f:
    for segment in segments:
        f.write(segment[0] + ": " + segment[1])
        f.write('\n')

