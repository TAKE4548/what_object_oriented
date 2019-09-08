# coding: utf-8
import tkinter
from tkinter import ttk
from datetime import date

from cat import Cat
from cat import CatInquirer


class OperationWindow(tkinter.Frame):
    """
    GUIの操作画面クラス
    """
    def __init__(self, master=None, values=[], command=None):
        # フレームを作成
        super().__init__(master=master)
        self.pack()

        # コールバック関数の設定
        if command is None:
            command = self.dmy_command
        self.command = command

        # 指定リストのコンボボックスを作成
        self.value = tkinter.StringVar()
        self.name_box = ttk.Combobox(
            master=self, state="readonly", values=values
        )
        self.name_box.current(0)
        self.name_box.pack(padx=5, pady=5)

        # 選択を確定するボタンを作成
        self.select_btn = ttk.Button(
            master=self, text="Select", command=self.decition_name
        )
        self.select_btn.pack(padx=5, pady=5)

    def dmy_command(self, *args):
        """
        コールバック未指定時のダミー関数
        """
        return {}

    def decition_name(self):
        """
        選択確定ボタンを押した時の処理
        """
        # コンボボックスの現在表示値を取得
        self.value.set(self.name_box.get())
        # 対応する表示情報の辞書を取得
        infos = self.command(self.value.get())
        self.show_information(infos)

    def show_information(self, infos):
        """
        情報表示のサブウィンドウを開く

        param
            infos: (dict)表示する情報の辞書(key: 項目名, val: 情報の内容)
        return
            None
        """
        # 情報表示用テーブル作成
        sub_win = tkinter.Toplevel()
        information = ttk.Treeview(
            master=sub_win, columns=("値"), show="tree",
            height=len(infos.items())
        )
        for key, val in infos.items():
            information.insert("", "end", text=key, values=(val))
        information.pack()
        # 閉じるボタン作成
        close_btn = tkinter.Button(
            master=sub_win, text="閉じる", command=sub_win.destroy
        )
        close_btn.pack(pady=10)


def main():
    # サンプルとするネコのインスタンス生成
    cats = CatInquirer()
    cats.increase(
        "ジジ", date(2017, 5, 10), "オス", "",
        "ニシンパイ", "黒", "白", "短毛種"
    )
    cats.increase(
        "タマ", date(2015, 11, 23), "オス", "",
        "サンマ", "白", "白", "短毛種"
    )
    cats.increase(
        "ニャース", date(2017, 1, 31), "オス", "ポケモン",
        "がんもどき", "アイボリー", "白", "短毛種"
    )

    # GUIの準備・設定
    root = tkinter.Tk()
    root.title("Cat's Infomations")
    app = OperationWindow(root, cats.get_names(), cats.to_dict)
    # 操作画面の表示
    app.mainloop()


if __name__ == "__main__":
    main()
