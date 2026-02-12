#!/usr/bin/env python3
def find_the_redheads(family):
    filtered_people = (filter(lambda p: p[1] == "red", family.items()))
    map_people = list(map(lambda person: person[0], filtered_people))
    return map_people

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))