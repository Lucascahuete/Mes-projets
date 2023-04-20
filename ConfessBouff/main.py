from tinydb import TinyDB, Query, where
import random
from pathlib import Path
dir_data = Path.cwd() / "data"
dir_data.mkdir(exist_ok=True)
db = TinyDB(dir_data / 'data.json', indent=4)
q = Query()

class User:
    def __init__(self, name: str):
        self.name = name.capitalize()
        if self.name not in get_users() and self.name != "":
            self.add_user()
        else:
            pass

    def _get_facts(self):
        get_facts = db.search(q.name == self.name)
        try:
            facts = get_facts[0]["fact"]
            return facts
        except:
            print("list vide")
    def add_user(self):
        db.upsert({"name": self.name, "fact": []}, where("name") == self.name)
    def remove_user(self, user: str):
        db.remove(q.name == user)
    def write_fact(self, fact):
        f = self._get_facts()
        f.append(fact)
        db.update({"fact": f}, where("name") == self.name)
    def remove_fact(self, fact):
        f = self._get_facts()
        f.remove(fact)
        db.update({"fact": f}, where("name") == self.name)
def get_users():
    users = []
    for i in db.all():
        users.append(i["name"])
    return users


class Quiz:
    def random_user(self):
        return random.choice(get_users())
    def random_fact(self, user):
        facts = db.search(q.name == user)
        dict_facts = facts[0]
        try:
            return random.choice(tuple(dict_facts["fact"]))
        except:
            print("liste vide")


if __name__ == "__main__":
    qustion1 = Quiz()
    perso = qustion1.random_user()
    confess = qustion1.random_fact(perso)
    print(perso)
    print(confess)