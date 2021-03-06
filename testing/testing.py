QUESTIONS = {
    'Ухаживать за животными': '1a',
    'Обслуживать машины, приборы (следить, регулировать)': '1б',
    'Помогать больным людям, лечить их': '2а',
    'Составлять таблицы, схемы, программы вычислительных машин.': '2б',
    'Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластино': '3а',
    'Следить за состоянием, развитием растений': '3б',
    'Обрабатывать материалы (дерево, ткань, пластмассу и т.д.)': '4а',
    'Доводить товары до потребителя (рекламировать, продавать)': '4б',
    'Обсуждать научно-популярные книги, статьи': '5а',
    'Обсуждать художественные книги': '5б',
    'Выращивать молодняк животных какой-либо породы': '6а',
    'Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных)': '6б',
    'Копировать рисунки, изображения, настраивать музыкальные инструменты': '7а',
    'Управлять каким-либо грузовым, подъёмным, транс портным средством (подъёмным краном, машиной и т.п.)': '7б',
    'Сообщать, разъяснять людям нужные для них сведения в справочном бюро, во время экскурсии и т.д.': '8а',
    'Художественно оформлять выставки, витрины, участвовать в подготовке концертов, пьес и т.п.': '8б',
    'Ремонтировать изделия, вещи (одежду, технику), жилище.': '9а',
    'Искать и исправлять ошибки в текстах, таблицах, рисунках.': '9б',
    'Лечить животных.': '10а',
    'Выполнять расчёты, вычисления.': '10б',
    'Выводить новые сорта растений.': '11а',
    'Конструировать новые виды промышленных изделий (машины, одежду, дома и т.д.).': '11б',
    'Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать.': '12а',
    'Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).': '12б',
    'Наблюдать, изучать работу кружков художественной самодеятельности': '13а',
    'Наблюдать, изучать жизнь микробов.': '13б',
    'Обслуживать, налаживать медицинские приборы и аппараты.': '14а',
    'Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.': '14б',
    'Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др.': '15а',
    'Художественно описывать, изображать события наблюдаемые или представляемые.': '15б',
    'Делать лабораторные анализы в больнице.': '16а',
    'Принимать, осматривать больных, беседовать с ними, назначать лечение.': '16б',
    'Красить или расписывать стены помещений, поверхность изделий.': '17а',
    'Осуществлять монтаж здания или сборку машин, приборов.': '17б',
    'Организовывать культ походы людей в театры, музеи, на экскурсии, в туристические путешествия и т.п.': '18а',
    'Играть на сцене, принимать участие в концертах.': '18б',
    'Изготовлять по чертежам детали, изделия (машины, одежду), строить здания.': '19а',
    'Заниматься черчением, копировать карты, чертежи.': '19б',
    'Вести борьбу с болезнями растений, с вредителями леса, сада.': '20а',
    'Работать на машинах (пишущая машина, компьютер, телетайп, телефакс).': '20б',
}


def get_test_results(result):
    results = {
        'Человек природа': '1a3б6а10а11а13б16а20а',
        'Человек техника': '1б4а7б9а11б14а17б19а',
        'Человек человек': '2а4б6б8а12а14б16б18а',
        'Человек знаковая система': '2б5а9б10б12б15а19б20б',
        'Человек художественный образ': '3а5б7а8б13а15б17а18б',
    }
    for result_title, value in results.items():
        if result == value:
            return result_title
    return result_title


def test(string):
    for question, value in QUESTIONS.items():
        if string == question:
            return value


if __name__ == '__main__':

    # print(get_doc_file())
    document = Document()
    print(test())
