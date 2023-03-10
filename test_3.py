from Web_scraping_function import get_article_date, get_article_header, get_actual_link, make_soup, check_article_body, \
    _get_response

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Wasteland', 'ViRush', 'нейросеть', 'робот']


def test_3():  # тест по старой ДЗ
    url = 'https://habr.com/ru'  # базовый url
    response = _get_response(some_url=url)  # переменная сделана для проверки работы логгера.
    soup = make_soup(some_url=url)  # делаем из полученной строки суп

    articles = soup.findAll('article')  # ищем все заданные тэги
    for article in articles:  # обрабатываем каждый тэг
        full_article_url = get_actual_link(article=article)  # ссылка на полную статью
        article_soup = make_soup(full_article_url)  # получаем суп из полной статьи.
        article_word_set = check_article_body(full_article_soup=article_soup)  # множество из слов из тела статьи

        for word in KEYWORDS:  # проверка вхождения требуемых слов в тело полной статьи
            if word.lower() in article_word_set:
                article_date = get_article_date(article=article_soup)
                header = get_article_header(article=article_soup)
                print(f'Дата: {article_date}. Название статьи - {header}, '
                      f'ссылка - {full_article_url}')