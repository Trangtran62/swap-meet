import uuid


class Item(object):

    def __init__(self, condition=0, id=None):
        if not id or not isinstance(id, int):
            self.id = uuid.uuid1().int
        else:
            self.id = id
        if condition > 5:
            raise ValueError("Condition must be in the range of 0-5.")
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        description = {
            0: "oh oops",
            1: "I mean if you have no other choices.",
            2: "It's tolerable.",
            3: "It's decent.",
            4: "Probably a good deal.",
            5: "Get it. Good conditions."
        }
        return description[self.condition]
