# -*- coding: utf-8 -*-


from datetime import date

class Cat:
    """
    ネコのクラス
    """
    def __init__(
        self,
        name, birth_day, sex, type_name, favorite_food,
        fur_color, eye_color, fur_type
    ):
        # ネコのプロパティ
        self.name = name
        self.birth_day = birth_day # 誕生日のプロパティを追加
        self.age = None
        self.calculation_age()     # 誕生日から自動算出
        self.sex = sex
        self.type_name = type_name
        self.favorite_food = favorite_food
        self.fur_color = fur_color
        self.eye_color = eye_color
        self.fur_type = fur_type

    def calculation_age(self):
        """
        誕生日から年齢を算出する
        """
        # 今日の日付を取得
        today = date.today()
        # 去年の年齢を取得
        age = today.year - self.birth_day.year - 1
        # 今年の誕生日を迎えていれば+1歳
        if today.month > self.birth_day.month:
            age += 1
        elif today.month == self.birth_day.month:
            if today.day >= self.birth_day.day:
                age += 1
        # プロパティに反映
        self.age = age
