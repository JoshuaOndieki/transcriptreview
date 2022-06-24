import imp
import re, difflib
from savereviewtodoc import savereview


file_id = input("Enter file ID: ")

initial_transcript = open("files/txt/" + file_id + ".txt", "r").readlines()
final_transcript = open("files/txt/" + file_id + "-final.txt", "r").readlines()

for i in range(len(initial_transcript)):
    initial_transcript[i] = initial_transcript[i].replace("\n", " ")
for i in range(len(final_transcript)):
    final_transcript[i] = final_transcript[i].replace("\n", " ")


initial_transcript = "".join(initial_transcript).split(" ")
final_transcript = "".join(final_transcript).split(" ")


for d in difflib.ndiff(initial_transcript, final_transcript):
    print(d)


# Save review as DOC
savereview(file_id, difflib.ndiff(initial_transcript, final_transcript))