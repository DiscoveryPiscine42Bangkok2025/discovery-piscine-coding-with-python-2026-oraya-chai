#!/usr/bin/env python3
def array_of_names(persons):
    list_name = []
    for firstname, lastname in persons.items():
        name = firstname.capitalize() + " " + lastname.capitalize()
        list_name.append(name)
    return list_name

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

     