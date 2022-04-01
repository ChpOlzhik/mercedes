from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(API_TOKEN)


def main():
    print(bot._token)


if __name__ == '__main__':
    main()
