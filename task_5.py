class TestCase:
    def __init__(self, steps=None, result=None):
        # Инициализируем поле steps пустым словарем, если оно не передано
        self.steps = steps if steps is not None else {}
        # Инициализируем поле result, если результат не передан - устанавливаем None
        self.result = result

    def set_step(self, step_number, step_text):
        # Добавляем шаг в словарь steps
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        # Удаляем шаг из steps по ключу step_number
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):
        # Устанавливаем ожидаемый результат
        self.result = result

    def get_test_case(self):
        # Формируем и выводим информацию о тест-кейсе
        test_case_info = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(test_case_info)

# Пример использования класса
test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()