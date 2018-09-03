from datetime import datetime
from random import choice

from tutorial.todoapp.models import Todo
from tutorial.master.models import BaseUser


def main():
    users = [
        {
            'username': 'megu',
            'password': 'test',
        },
        {
            'username': 'taro',
            'password': 'test',
        },
        {
            'username': 'mika',
            'password': 'test',
        },
        {
            'username': 'kouichi',
            'password': 'test',
        },
        {
            'username': 'saku',
            'password': 'test',
        },
        {
            'username': 'shiro',
            'password': 'test',
        }
    ]

    for user in users:
        if BaseUser.objects.filter(username=user['username']).exists():
            continue
        else:
            BaseUser.objects.create_user(**user)

    users = BaseUser.objects.all()

    todos = [
        {
            'title': 'python勉強会資料作成',
            'content': '勉強会の資料を作成する',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': 'バイト',
            'content': '生協のバイト',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': '資料整理',
            'content': '学校の課題の資料整理',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': '問い合わせ',
            'content': '旅行会社に問い合わせ',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': 'アプリ開発',
            'content': 'アプリ開発の計画を立てる',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': '自転車の修理',
            'content': '自転車が壊れたから修理に行く',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': '服を買いに',
            'content': '服がないので買いに行く',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
        {
            'title': '銀行振込',
            'content': 'ローンの返済',
            'completed': datetime(2018, 8, 25, 12, 15, 30),
            'due': datetime(2018, 9, 1, 0, 0, 0),
        },
    ]

    for i in range(100):
        todo = todos[i % 8]
        todo.update({
            'user': choice(users)
        })
        Todo(**todo).save()
