# DareFitBot

Телеграм-бот, предоставляющий бесплатные тренировки и программы с сайта Darebee.

## Установка

Требуется Python 3.11 или новее.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создайте файл `.env` и укажите в нём `BOT_TOKEN=<токен вашего бота>`.

## Запуск

```bash
python -m darefitbot.bot
```

Бот использует `aiogram` 3 версии и хранит данные в SQLite.
