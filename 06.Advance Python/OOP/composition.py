class Leg:
    pass


class Back:
    pass


class Chair:
    def __init__(self, num_legs):
        self.legs = [Leg() for leg in range(num_legs)]
        self.back = Back()

    def __repr__(self):
        return f'I have {len(self.legs)} legs and one back.'


chair = Chair(5)
print(chair)
print(chair.legs)
print(chair.back)
