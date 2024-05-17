#!/usr/bin/env python3
"""Define a function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Compute the evarage score and sorte students"""
    average = []
    result = []
    for s in mongo_collection.find():
        total, n = 0, 0
        for m in s.get("topics"):
            n += 1
            total += m.get('score')
        s["averageScore"] = total/n
        average.append(total/n)
    average.sort(reverse=True)
    for a in average:
        print(mongo_collection.find_one({"averageScore": a}))
        print("average print")
    return result
