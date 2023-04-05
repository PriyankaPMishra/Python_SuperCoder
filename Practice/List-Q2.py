"""Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words.
The task is to find the unknown words (other than the words they already know) from the given text.
Write a python function which accepts the text and the known list of words and returns the set of unknown words found.
Return -1 if there are no unknown words.
Estimated Time: 20 minutes

Sample Input
Text: "the sun rises in the east"
Vocabulary: ["sun", "in", "east", "doctor", "day"]

Expected Output: {'rises', 'the'}"""

text = "the sun rises in the east"
voc = ["sun", "in", "east", "doctor", "day"]

def known_unknown(text, voc):
    unknown = set()
    for i in text.split():
        if i not in voc:
            unknown.add(i)
    return unknown if len(unknown)>0 else -1

print((known_unknown(text, voc)))