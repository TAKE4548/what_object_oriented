# coding: utf-8
from datetime import date

class Cat:
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
        # ネコのプロパティ
        self.name = name
        self.birth_day = birth_day
        self.age = None
        self.calculation_age()
        self.sex = sex
        self.type_name = type_name
        self.favorite_food = favorite_food
        self.fur_color = fur_color
        self.eye_color = eye_color
        self.fur_type = fur_type

    def __str__(self):
        delimiter = '\t'
        linefeed = '\n'
        ret_str = "名前" + delimiter
        ret_str += self.name + linefeed
        ret_str += "性別" + delimiter
        ret_str += self.sex + linefeed
        ret_str += "誕生日" + delimiter
        ret_str += self.birth_day.strftime("%Y/%m/%d") + linefeed
        ret_str += "年齢" + delimiter
        ret_str += str(self.age) + linefeed
        ret_str += "種類" + delimiter
        ret_str += self.type_name + linefeed
        ret_str += "毛色" + delimiter
        ret_str += self.fur_color + linefeed
        ret_str += "目の色" + delimiter
        ret_str += self.eye_color + linefeed
        ret_str += "毛種" + delimiter
        ret_str += self.fur_type + linefeed
        ret_str += "好物" + delimiter
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
            "毛色": self.fur_color,
            "目の色": self.eye_color,
            "毛種": self.fur_type,
            "好物": self.favorite_food
        }
        return ret_dict


class CatInquirer:
    """
    ネコの情報を紹介する

    param
        cats: (list)Catオブジェクトのリスト
    """
    def __init__(self, cats=[]):
        # 名前をキーにした辞書に変換
        self.cats = {x.name: x for x in cats}

    def increase(
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
        # 既存の確認
        if name in self.cats.keys():
            if not force:
                print(
                    "既に同名のネコがいます。\n" +
                    "情報を上書きする場合は\"force\"オプションを" +
                    "Trueにして再試行して下さい。"
                )
                return None
        # 追加するCatインスタンスを作成
        tmp_cat =  Cat(
            name, birth_day, sex, type_name, favorite_food,
            fur_color, eye_color, fur_type
        )
        # 追加
        self.cats[tmp_cat.name] = tmp_cat
        return tmp_cat

    def find_cat(self, name):
        """
        指定した名前のCatインスタンスを取得して返す

        param
            name: (str)探索するネコの名前
        return
            (Cat)見つかったCatのインスタンス
        """
        if name not in self.cats.keys():
            raise KeyError("そんなネコはいないよ")
        return self.cats[name]

    def get_names(self):
        """
        登録済みのネコたちの名前一覧を返す

        param
            None
        return
            (list)ネコの名前リスト
        """
        return list(self.cats.keys())

    def to_dict(self, name):
        """
        指定した名前のCatインスタンスに対応する辞書を返す

        param
            name: (str)探索するネコの名前
        return
            (dict)見つかったCatのインスタンスの辞書(key:属性名, val:属性値)
        """
        return self.find_cat(name).to_dict()
