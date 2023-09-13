import random
from enum import Enum
from typing import Dict, List, Union

from faker import Faker

fake = Faker()


class WeightClass(Enum):
    STRAWWEIGHT = 0
    FLYWEIGHT = 1
    BANTAMWEIGHT = 2
    FEATHERWEIGHT = 3
    LIGHTWEIGHT = 4
    WELTERWEIGHT = 5
    MIDDLEWEIGHT = 6
    LIGHTHEAVYWEIGHT = 7
    HEAVYWEIGHT = 8


class GenderType(Enum):
    MALE = "M"
    FEMALE = "F"


class Age(Enum):
    MIN = 18
    MAX = 40


class Height:
    MIN = [155, 165, 168, 168, 170, 175, 175, 180, 180]
    MAX = [170, 175, 180, 183, 190, 190, 193, 198, 201]


class Reach:
    MEAN = [165, 170, 171, 179, 184, 186, 190, 198, 200]
    SIGMA = [5] * 9


class Weight:
    MIN = [155, 115, 125, 135, 145, 155, 170, 185, 205]
    MAX = [115, 125, 135, 145, 155, 170, 185, 205, 265]


class Fighter:
    def __init__(self, weight_class: WeightClass, gender: GenderType) -> None:
        self.weight_class = weight_class.value
        self.gender = gender.value
        self.record = [0, 0, 0]

    @property
    def name(self) -> str:
        return (
            fake.name_male()
            if self.gender == GenderType.MALE.value
            else fake.name_female()
        )

    @property
    def age(self) -> int:
        return random.randint(Age.MIN.value, Age.MAX.value)

    @property
    def height(self) -> int:
        return random.randint(
            Height.MIN[self.weight_class], Height.MAX[self.weight_class]
        )

    @property
    def reach(self) -> int:
        return round(
            random.normalvariate(
                Reach.MEAN[self.weight_class], Reach.SIGMA[self.weight_class]
            ),
            0,
        )

    @property
    def weight(self) -> float:
        return round(
            random.uniform(
                Weight.MIN[self.weight_class], Weight.MAX[self.weight_class]
            ),
            1,
        )

    def add_win(self) -> List[int]:
        self.record[0] += 1
        return self.record

    def add_loss(self) -> List[int]:
        self.record[1] += 1
        return self.record

    def add_draw(self) -> List[int]:
        self.record[2] += 1
        return self.record

    def get_data(self) -> Dict[str, Union[int, float, str]]:
        map_weight_class = {
            0: "Strawweight",
            1: "Flyweight",
            2: "Bantamweight",
            3: "Featherweight",
            4: "Lightweight",
            5: "Welterweight",
            6: "Middleweight",
            7: "Light heavyweight",
            8: "Heavyweight",
        }

        data = {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "height": self.height,
            "reach": self.reach,
            "weight": self.weight,
            "record": self.record,
            "weight_class": map_weight_class[self.weight_class],
        }

        return data


if __name__ == "__main__":
    fighter = Fighter(WeightClass.BANTAMWEIGHT, GenderType.FEMALE)
    print(fighter.get_data())
