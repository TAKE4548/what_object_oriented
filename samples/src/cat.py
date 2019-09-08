# -*- coding: utf-8 -*-


class Cat:
    """
    ネコのクラス
    """
    def __init__(
        self,
        name, age, sex, type_name, favorite_food,
        fur_color, eye_color, fur_type
    ):
        # ネコのプロパティ
        self.name = name
        self.age = age
        self.sex = sex
        self.type_name = type_name
        self.favorite_food = favorite_food
        self.fur_color = fur_color
        self.eye_color = eye_color
        self.fur_type = fur_type
