import dataclasses

@dataclasses.dataclass
class Scorecard:
    nine: int
    ten: int
    jack: int
    queen: int
    king: int
    ass: int
    street: int
    full_house: int
    poker: int
    grande: int
    
    def sum(self):
        return self.nine + self.ten + self.jack + self.queen + self.king + self.ass + self.street + self.full_house + self.poker + self.grande
    
    def add_points(self, card_symbol: str, count: int, first_try: bool):
        if first_try:
            bonus = 5
        else:
            bonus = 0
            
        if card_symbol == '9': self.nine = count + bonus
        elif card_symbol == '10': self.ten = count * 2 + bonus
        elif card_symbol == 'J': self.jack = count * 3 + bonus
        elif card_symbol == 'Q': self.queen = count * 4 + bonus
        elif card_symbol == 'K': self.king = count * 5 + bonus
        elif card_symbol == 'A': self.ass = count * 6 + bonus
        elif card_symbol == 'S': self.street = 20 + bonus
        elif card_symbol == 'F': self.street = 30 + bonus
        elif card_symbol == 'P': self.street = 40 + bonus
        elif card_symbol == 'G': self.street = 50 + bonus