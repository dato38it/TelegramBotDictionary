# Телеграм Бот Переводчик
<ul>
    <li>
        Для подготовки разработки программы в текстовых файлах записал труднозапоминаемые слова и термины.
    </li>
    <li>
        Разработал программу, которая переводит слова и предложения без ботов.
    </li>
    <li>
        Добавил Бот-переводчик в телеграмме.
    </li>
    <li>
        Разработал базу данных Словарь, в котором хранятся данные слов и предложений.
    </li>
    <li>
        Написал Sql-запрос.
    </li>
    <li>
        Добавил скрипт, который подключается базе и выполняет Sql-запрос.
    </li>
</ul>
<p>
    <strong>Task:</strong><br>
    Переводчик слов и предложений<br>
    <strong>Decision:</strong><br>
    $ vim translator.py<br>
    $ cat translator.py<br>
    from translate import Translator<br>
    translator=Translator(from_lang="russian", to_lang="english")<br>
    translation=translator.translate("Привет. Как дела?")<br>
    print(translation)<br>
    $ vim requirements.txt<br>
    $ cat requirements.txt<br>
    translate==3.6.1<br>
    $ pip install -r requirements.txt<br>
    $ python3 translator.py<br>
    Hi, how are you?<br>
    <strong>Task:</strong><br>
    Бот-переводчик в телеграмме через библиотеку aiogram<br>
    <strong>Decision:</strong><br>
    $ vim requirements.txt<br>
    $ cat requirements.txt<br>
    translate==3.6.1<br>
    aiogram==2.23.1<br>
    $ pip install -r requirements.txt<br>
    $ vim translatorBot.py<br>
    $ cat translatorBot.py<br>
    import logging<br>
    from translate import Translator<br>
    from aiogram import Bot, Dispatcher, executor, types<br>
    API_TOKEN = 'ttoken'<br>
    # Configure logging<br>
    logging.basicConfig(level=logging.INFO)<br>
    # Initialize bot and dispatcher<br>
    bot = Bot(token=API_TOKEN)<br>
    dp = Dispatcher(bot)<br>
    ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"<br>
    en_letters = "abcdefghijklmnopqrstuvwxyz"<br>
    @dp.message_handler(commands=['start', 'help'])<br>
    async def send_welcome(message: types.Message):<br>
    &nbsp;&nbsp;await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")<br>
    @dp.message_handler()<br>
    async def echo(message: types.Message):<br>
    &nbsp;&nbsp;text = message.text<br>
    &nbsp;&nbsp;if text[0].lower() in ru_letters:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;translator = Translator(from_lang="russian", to_lang="english")<br>
    &nbsp;&nbsp;elif text[0].lower() in en_letters:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;translator = Translator(from_lang="english", to_lang="russian")<br>
    &nbsp;&nbsp;else:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;await message.answer('Я тебя не понимаю')<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return<br>
    &nbsp;&nbsp;translation = translator.translate(text)<br>
    &nbsp;&nbsp;await message.answer(translation)<br>
    if __name__ == '__main__':<br>
    &nbsp;&nbsp;executor.start_polling(dp, skip_updates=True)<br>
    $ python translatorBot.py<br>
    <strong>Source:</strong><br>
    Переводчик бот в telegram на python за 5 минут aiogram - https://www.youtube.com/@shcoder001<br>

<p>
    <strong>Task:</strong><br>
    Разработать базу данных Словарь, в котором будут две таблицы<br>
    Словарь<br>
    id | words | translate&nbsp;<br>
    1 | Текст1 | Text1&nbsp;&nbsp;&nbsp;<br>
    2 | Текст2 | Text2&nbsp;&nbsp;&nbsp;&nbsp;<br>
    3 | Текст3 | Text3&nbsp;<br>
    Термины<br>
    id | words_id&nbsp;&nbsp;| description | translate<br>
    1 | 1&nbsp;&nbsp;&nbsp;&nbsp; | Текст4&nbsp;&nbsp; | Text4&nbsp;<br>
    2 | 3&nbsp;&nbsp;&nbsp;&nbsp; | Текст5&nbsp;&nbsp; | Text5&nbsp;<br>
    <strong>Decision:</strong><br>
    =&gt; CREATE DATABASE tdb2;<br>
    =&gt; exit<br>
    $ sudo vim /etc/postgresql/14/main/pg_hba.conf<br>
    $ cat /etc/postgresql/14/main/pg_hba.conf | grep tdb2<br>
    host&nbsp;&nbsp;tdb2&nbsp;&nbsp; tuser&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tip/24&nbsp;&nbsp; md5<br>
    $ sudo vim /etc/postgresql/14/main/postgresql.conf<br>
    $ cat /etc/postgresql/14/main/postgresql.conf | grep listen_addres<br>
    listen_addresses = 'tip, 192.168.0.105'<br>
    $ sudo systemctl restart postgresql<br>
    $ sudo ufw allow 5432<br>
    $ psql -U tuser -d tdb2 -h tip<br>
    =&gt; CREATE TABLE tdb2 (<br>
    &nbsp;&nbsp;id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,<br>
    &nbsp;&nbsp;words VARCHAR(1000),<br>
    &nbsp;&nbsp;translate VARCHAR(1000)<br>
    );<br>
    =&gt; CREATE TABLE Terms (<br>
    &nbsp;&nbsp;id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,<br>
    &nbsp;&nbsp;words_id INT,<br>
    &nbsp;&nbsp;description VARCHAR(1000),<br>
    &nbsp;&nbsp;translate VARCHAR(1000),<br>
    &nbsp;&nbsp;CONSTRAINT fk_tdb2<br>
    &nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(words_id)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;REFERENCES tdb2(id)<br>
    );<br>
    =&gt; INSERT INTO tdb2 (words, translate)<br>
    VALUES ('Текст1', 'Text1'), ('Текст2', 'Text2'), ('Текст3', 'Text3');<br>
    =&gt; INSERT INTO Terms (words_id, description, translate)<br>
    VALUES (1, 'Текст4', 'Text4'), (3, 'Текст5','Text5');<br>
    <strong>Task:</strong><br>
    Выборка таблицы&nbsp;<br>
    words | translate | description&nbsp;&nbsp; | translate<br>
    Текст1 | Text1&nbsp;&nbsp; | Текст4&nbsp;&nbsp;&nbsp;&nbsp; | Text4<br>
    Текст3 | Text3&nbsp;&nbsp; | Текст5&nbsp;&nbsp;&nbsp;&nbsp; | Text5<br>
    <strong>Decision:</strong><br>
    =&gt; select words, tdb2.translate, description, Terms.translate&nbsp;<br>
    from tdb2<br>
    inner join Terms&nbsp;<br>
    on tdb2.id = Terms.words_id;<br>
    words | translate | description | translate&nbsp;<br>
    --------+-----------+-------------+-----------<br>
    Текст1 | Text1&nbsp;&nbsp; | Текст4&nbsp;&nbsp; | Text4<br>
    Текст3 | Text3&nbsp;&nbsp; | Текст5&nbsp;&nbsp; | Text5<br>
    (2 rows)<br>
    <strong>Source:</strong><br>
    Создание базы данных - https://postgrespro.ru/docs/postgresql/9.5/manage-ag-createdb<br>
    Руководство по SQL для начинающих. Часть 1: создание базы данных, таблиц и установка связей между таблицами - https://proglib.io/p/rukovodstvo-po-sql-dlya-nachinayushchih-chast-1-sozdanie-bazy-dannyh-tablic-i-ustanovka-svyazey-mezhdu-tablicami-2022-02-07<br>
    Внутреннее соединение INNER JOIN - https://sql-academy.org/ru/guide/inner-join<br>
    <strong>Task:</strong><br>
    Подключение к базе данных и выолнение запроса через скрипт на Python<br>
    <strong>Decision:</strong><br>
    $ vim requirements.txt&nbsp;<br>
    $ cat requirements.txt&nbsp;<br>
    translate==3.6.1<br>
    aiogram==2.23.1<br>
    psycopg2-binary==2.9.9<br>
    $ pip install -r requirements.txt<br>
    $ vim psqlpy.py<br>
    $ cat psqlpy.py<br>
    import psycopg2<br>
    try:<br>
    &nbsp;&nbsp;# пытаемся подключиться к базе данных<br>
    &nbsp;&nbsp;conn = psycopg2.connect(dbname='tdb2', user='tuser', password='tpassword', host='tip')<br>
    except:<br>
    &nbsp;&nbsp;# в случае сбоя подключения будет выведено сообщение в STDOUT<br>
    &nbsp;&nbsp;print('Can`t establish connection to database')<br>
    $ python psqlpy.py<br>
    $ vim psqlpy.py<br>
    $ cat psqlpy.py<br>
    import psycopg2<br>
    try:<br>
    &nbsp;&nbsp;# пытаемся подключиться к базе данных<br>
    &nbsp;&nbsp;conn = psycopg2.connect(dbname='tdb2', user='tuser', password='tpassword', host='tip')<br>
    &nbsp;&nbsp;cursor = conn.cursor()<br>
    &nbsp;&nbsp;cursor.execute('select words, tdb2.translate, description, Terms.translate from tdb2 inner join Terms on tdb2.id = Terms.words_id')<br>
    &nbsp;&nbsp;#records = cursor.fetchall()<br>
    &nbsp;&nbsp;#print(records)<br>
    &nbsp;&nbsp;for row in cursor:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(row)<br>
    &nbsp;&nbsp;cursor.close()<br>
    &nbsp;&nbsp;conn.close()<br>
    except:<br>
    &nbsp;&nbsp;# в случае сбоя подключения будет выведено сообщение в STDOUT<br>
    &nbsp;&nbsp;print('Can`t establish connection to database')<br>
    $ python psqlpy.py<br>
    ('Внутреннее соединение', 'Inner join', 'Возвращаются только те строки, где ключевые значения совпадают в обеих таблицах', 'Only those rows are returned where the key values match in both tables')<br>
    ('Полное соединение', 'Cross Join', 'Позволяет получить декартово произведение нескольких таблиц. особенно полезен, когда между таблицами нет определенной связи, и вам нужно создать полную комбинацию записей из каждой таблицы', '-')<br>
    ('Декартово произведение', 'Cartesian product', 'Результат соединения строки из первой таблицы с каждой строкой из второй таблицы', '-')<br>
    $ vim psqlpy.py<br>
    $ cat psqlpy.py<br>
    import psycopg2<br>
    from contextlib import closing<br>
    with closing(psycopg2.connect(dbname='tdb2', user='tuser', password='tpassword', host='tip')) as conn:<br>
    &nbsp;&nbsp;with conn.cursor() as cursor:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;cursor.execute('select words, tdb2.translate, description, Terms.translate from tdb2 inner join Terms on tdb2.id = Terms.words_id')<br>
    &nbsp;&nbsp;&nbsp;&nbsp;for row in cursor:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(row)<br>
    $ python psqlpy.py<br>
    ('Внутреннее соединение', 'Inner join', 'Возвращаются только те строки, где ключевые значения совпадают в обеих таблицах', 'Only those rows are returned where the key values match in both tables')<br>
    ('Полное соединение', 'Cross Join', 'Позволяет получить декартово произведение нескольких таблиц. особенно полезен, когда между таблицами нет определенной связи, и вам нужно создать полную комбинацию записей из каждой таблицы', '-')<br>
    ('Декартово произведение', 'Cartesian product', 'Результат соединения строки из первой таблицы с каждой строкой из второй таблицы', '-')<br>
    <strong>Source:</strong><br>
    Использование Psycopg2 - https://ru.hexlet.io/blog/posts/python-postgresql<br>
    Начало работы - https://khashtamov.com/ru/postgresql-python-psycopg2/<br>
    &nbsp;
</p>