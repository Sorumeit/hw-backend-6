from attrs import define


@define
class Flower:
    name: str
    count: int
    cost: int
    id: int = 0


class FlowersRepository:
    flowers: list[Flower]

    def __init__(self):
        self.flowers = []
    
    def add( self , flower ):
        new_flower = Flower
        new_flower.cost = flower["price"]
        new_flower.name = flower["name"]
        new_flower.count = flower["count"]
        new_flower.id = len( self.flowers ) + 1
        self.flowers.append( new_flower )
