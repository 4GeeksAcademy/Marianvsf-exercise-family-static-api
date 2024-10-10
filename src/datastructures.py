
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id=0
        # example list of members
        self._members = [{
            "first_name": "John",
            "age": "33",
            "lucky_numbers": [7,13,22],
            "id": 1
        },
        {
            "first_name": "Jane",
            "age": "35",
            "lucky_numbers": [10,14,3],
            "id": 2
        },
        {
            "first_name": "Jimmy",
            "age": "5",
            "lucky_numbers": [1],
            "id": 3
        },
        ]

    

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id +=1
        return generated_id

    def add_member(self, member):
        if member["age"]<=0:
            print ("La edad debe ser mayor a 0")
            return False
        if not "id" in member:
            member["id"]=self._generateId()
            member["id"]=self._next_id
        member["last_name"]=self.last_name
        self._members.append(member)
        return True

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}
        return {"done": False}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return False
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
