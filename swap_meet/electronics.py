from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0,age = None):
        # self.category = category
        # self.condition = condition
        super().__init__(category="Electronics", condition=condition,age =age)


    def __str__(self):
        return "A gadget full of buttons and secrets."

        
