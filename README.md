Задача: Автоматизировать UI- и API-тесты из вашей финальной работы по ручному тестированию.

Как запускать
- Установка зависимостей:
  - python -m venv .venv
  - source .venv/bin/activate (Windows: .venv\Scripts\activate)
  - pip install -r requirements.txt
- UI тесты:
  - pytest tests/test_ui.py -s --alluredir=allure_results_ui
- API тесты:
  - pytest tests/test_api.py -s --alluredir=allure_results_api
- Все тесты:
  - pytest -s --alluredir=allure_results
- Просмотр allure:
  - allure serve allure_results_ui

Ссылка на финальный проект: 
https://mark21.yonote.ru/doc/kursovaya-rabota-po-sajtu-chitaj-gorod-1L7IBJfNV4
