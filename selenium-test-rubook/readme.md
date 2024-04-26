# Отчет Allure

Этот репозиторий содержит пример теста Selenium с использованием библиотеки Allure для генерации отчетов о выполнении тестов.

## Установка зависимостей

Для запуска теста вам потребуются следующие зависимости:

- Python
- pytest
- selenium
- allure-pytest

Вы можете установить их с помощью следующей команды:

```bash
pip install pytest selenium allure-pytest
```
```bash
pip install selenium
```
```bash
pip install pytest
```

Запуск

```bash
pytest -s --alluredir allure-results main.py
```
```bash
allure serve allure-results
```

![image](https://github.com/VsevolodYatsuk/RuBook/assets/130091517/d09ac8e0-56e9-481e-b0ff-62328c11c49b)
