# FastAPI_project
This is my first **FastAPI** project. And this is test task for recommendation AI platform **Bewise**

## Stack:

![FastAPI](https://img.shields.io/badge/FastAPI-0.95.1-cyan?style=flat&logo=FastAPI&logoColor=cyan)
![Python](https://img.shields.io/badge/Python-3.10-brightgreen?style=flat&logo=Python&logoColor=brightgreen)
![SqlAlchemy](https://img.shields.io/badge/SqlAlchemy-2.0.13-brightgreen?style=flat&logo=python&logoColor=brightgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.2-blue?style=flat&logo=postgresql&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker_compose-grey?style=flat&logo=docker&logoColor=blue)

## Задача 1
Реализовать на Python3 веб сервис (с помощью ***FastAPI*** или ***Flask***, например), выполняющий следующие функции:

1. В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
2. После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) [https://jservice.io/api/random?count=1](https://jservice.io/api/random?count=1) указанное в полученном запросе количество вопросов.
3. Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки):
      - ID вопроса,
      - Текст вопроса,
      - Текст ответа,
      - Дата создания вопроса.
      
      В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
4. Ответом на запрос из п.1 должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

### Запуск
1. Перейти в директорию с проектом и запустить команду:
	```zsh
	docker-compose up
	```
2. После установки и запуска контейнера, перейти по ссылке: http://127.0.0.1:8000/docs

### Пример запроса и ответа
**POST** запрос на *endpoint* `/questions/3` сохранит в базе 3-и сущности викторины

```
{"questions_num": 3}
```
И вернет предыдущей сохранённый вопрос для викторины

```json
{
  "id_question": 43046,
  "question": "After Abel's murder, Cain settled in this land east of Eden",
  "answer": "Nod",
  "created_at": "2022-12-30T18:55:35.605000"
}
```
