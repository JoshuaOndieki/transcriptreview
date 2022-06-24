import json, time


ajson = input("Enter file ID: ")


with open("jsoncache/" + ajson + ".json", "r") as f:
    data = json.load(f)

segments = []

for t in data[0]["transcriptions"]:
    segments.append([t["speaker"], t["startTime"], t["endTime"], t["transcript"]])


with open("files/txt/" + ajson + "-final.txt", 'w') as f:
    for segment in segments:

        start_timestamp = time.strftime("%H:%M:%S", time.gmtime(segment[1]))
        end_timestamp = time.strftime("%H:%M:%S", time.gmtime(segment[2]))

        segment_timestamp = "[" + start_timestamp + "--" + end_timestamp + "] "

        f.write(segment[0] + ": " + segment_timestamp + segment[3])
        f.write('\n')

