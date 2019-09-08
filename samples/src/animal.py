# coding: utf-8
from datetime import date

class Animal:
    """
    動物のクラス

    params
        name: (str)名前
        birth_day: (datetime.date)誕生日
        sex: (str)性別
        type_name: (str)種類
        favorite_food: (str)好物
    """
    def __init__(self, name, birth_day, sex, type_name, favorite_food):
        # 動物のプロパティ
        self.name = name
        self.birth_day = birth_day
        self.age = None
        self.calculation_age()
        self.sex = sex
        self.type_name = type_name
        self.favorite_food = favorite_food

    def __str__(self):
        self.delimiter = '\t'
        self.linefeed = '\n'
        ret_str = "名前" + self.delimiter
        ret_str += self.name + self.linefeed
        ret_str += "性別" + self.delimiter
        ret_str += self.sex + self.linefeed
        ret_str += "誕生日" + self.delimiter
        ret_str += self.birth_day.strftime("%Y/%m/%d") + self.linefeed
        ret_str += "年齢" + self.delimiter
        ret_str += str(self.age) + self.linefeed
        ret_str += "種類" + self.delimiter
        ret_str += self.type_name + self.linefeed
        ret_str += "好物" + self.delimiter
        ret_str += self.favorite_food
        return ret_str

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

    def to_dict(self):
        """
        各プロパティを辞書化する

        param
            None
        return
            (dict)作成した辞書(key:属性名, val:属性値)
        """
        ret_dict = {
            "名前": self.name,
            "性別": self.sex,
            "誕生日": self.birth_day,
            "年齢": self.age,
            "種類": self.type_name,
            "好物": self.favorite_food
        }
        return ret_dict

class Cat(Animal):
    """
    ネコのクラス

    params
        name: (str)名前
        birth_day: (datetime.date)誕生日
        sex: (str)性別
        type_name: (str)種類
        favorite_food: (str)好物
        fur_color: (str)毛色
        eye_color: (str)目の色
        fur_type: (str)毛種
    """
    def __init__(
        self,
        name, birth_day, sex, type_name, favorite_food,
        fur_color, eye_color, fur_type
    ):
        # 動物のプロパティ
        super().__init__(name, birth_day, sex, type_name, favorite_food)
        # ネコのプロパティ
        self.fur_color = fur_color
        self.eye_color = eye_color
        self.fur_type = fur_type

    def __str__(self):
        ret_str = super().__str__()
        ret_str += "毛色" + self.delimiter
        ret_str += self.fur_color + self.linefeed
        ret_str += "目の色" + self.delimiter
        ret_str += self.eye_color + self.linefeed
        ret_str += "毛種" + self.delimiter
        ret_str += self.fur_type + self.linefeed
        return ret_str

    def to_dict(self):
        """
        各プロパティを辞書化する

        param
            None
        return
            (dict)作成した辞書(key:属性名, val:属性値)
        """
        ret_dict = super().to_dict()
        ret_dict["毛色"] = self.fur_color
        ret_dict["目の色"] = self.eye_color
        ret_dict["毛種"] = self.fur_type
        return ret_dict


class Elephant(Animal):
    """
    ぞうのクラス

    params
        name: (str)名前
        birth_day: (datetime.date)誕生日
        sex: (str)性別
        type_name: (str)種類
        favorite_food: (str)好物
        tusk_length: (float)牙の長さ
        ear_form: (str)耳の形
        nose_length: (float)鼻の長さ
    """
    def __init__(
        self,
        name, birth_day, sex, type_name, favorite_food,
        tusk_length, ear_form, nose_length
    ):
        # 動物のプロパティ
        super().__init__(name, birth_day, sex, type_name, favorite_food)
        # ぞうのプロパティ
        self.tusk_length = tusk_length
        self.ear_form = ear_form
        self.nose_length = nose_length

    def __str__(self):
        ret_str = super().__str__()
        ret_str += "牙の長さ" + self.delimiter
        ret_str += self.tusk_length + self.linefeed
        ret_str += "耳の形" + self.delimiter
        ret_str += self.ear_form + self.linefeed
        ret_str += "鼻の長さ" + self.delimiter
        ret_str += self.nose_length + self.linefeed
        return ret_str

    def to_dict(self):
        """
        各プロパティを辞書化する

        param
            None
        return
            (dict)作成した辞書(key:属性名, val:属性値)
        """
        ret_dict = super().to_dict()
        ret_dict["牙の長さ"] = self.tusk_length
        ret_dict["耳の形"] = self.ear_form
        ret_dict["鼻の長さ"] = self.nose_length
        return ret_dict

class AnimalInquirer:
    """
    動物の情報を紹介する

    param
        animals: (list)AnimalまたはAnimalのサブクラスのオブジェクトのリスト
    """
    def __init__(self, animals=[]):
        # 名前をキーにした辞書に変換
        self.animals = {x.name: x for x in animals}

    def is_registered(self, name):
        """
        指定した名前が登録済みかを確認する

        param
            name: (str)確認する名前
        return
            登録済み/True, 未登録/False
        """
        return name in self.animals.keys()

    def can_registered(self, name, force=False):
        """
        指定した名前が登録可能かを確認する

        param
            name: (str)確認する名前
            force: (bool)同名の動物がいる場合、強制的に可能とするか
        return
            登録可/True, 登録不可/False
        """
        if not force and self.is_registered(name):
            print(
                "既に同名の動物がいます。\n" +
                "情報を上書きする場合は\"force\"オプションを" +
                "Trueにして再試行して下さい。"
            )
            return False
        else:
            return True

    def add(self, ani_obj):
        """
        新しいAnimal系オブジェクトを登録する

        param
            ani_obj: (Animal or Animalのサブクラス)登録するインスタンス
        return
            None
        """
        self.animals[ani_obj.name] = ani_obj

    def increase_cat(
        self,
        name, birth_day, sex, type_name, favorite_food,
        fur_color, eye_color, fur_type, force=False
    ):
        """
        Catオブジェクトを直接生成して追加する

        param
            force: (bool)同名のネコがいる場合、強制的に情報の上書きをするか
        return
            (Cat)追加したCatインスタンス
        """
        tmp_cat = None
        # 登録可のみ登録
        if self.can_registered(name, force):
            # 追加するCatインスタンスを作成
            tmp_cat =  Cat(
                name, birth_day, sex, type_name, favorite_food,
                fur_color, eye_color, fur_type
            )
            # 追加
            self.add(tmp_cat)
        return tmp_cat

    def increase_elephant(
        self,
        name, birth_day, sex, type_name, favorite_food,
        tusk_length, ear_form, nose_length, force=False
    ):
        """
        Elephantオブジェクトを直接生成して追加する

        param
            force: (bool)同名の動物がいる場合、強制的に情報の上書きをするか
        return
            (Elephant)追加したElephantインスタンス
        """
        tmp_elephant = None
        # 登録可なら登録
        if self.can_registered(name, force):
            # 追加するElephantインスタンスを作成
            tmp_elephant =  Elephant(
                name, birth_day, sex, type_name, favorite_food,
                tusk_length, ear_form, nose_length
            )
            # 追加
            self.add(tmp_elephant)
        return tmp_elephant

    def find_animal(self, name):
        """
        指定した名前のAnimal系インスタンスを取得して返す

        param
            name: (str)探索する動物の名前
        return
            (Cat)見つかったAnimal系のインスタンス
        """
        if not self.is_registered(name):
            raise KeyError("そんな動物はいないよ")
        return self.animals[name]

    def get_names(self):
        """
        登録済みの動物たちの名前一覧を返す

        param
            None
        return
            (list)動物の名前リスト
        """
        return list(self.animals.keys())

    def to_dict(self, name):
        """
        指定した名前のAnimal系インスタンスに対応する辞書を返す

        param
            name: (str)探索する動物の名前
        return
            (dict)見つかったAnimal系のインスタンスの辞書(key:属性名, val:属性値)
        """
        return self.find_animal(name).to_dict()
