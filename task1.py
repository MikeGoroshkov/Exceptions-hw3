# Напишите программу-калькулятор, которая запрашивает у пользователя два числа и выполняет операцию возведения первого числа в степень второго числа. Если введены некорректные числа или происходит деление на ноль, необходимо обработать соответствующие исключения и вывести информативное сообщение об ошибке.
# Важно! С использованием принципа одного уровня абстракции
# **В этой задаче мы создаем класс PowerCalculator, который содержит метод calculatePower(), выполняющий операцию возведения числа в степень. Если введено некорректное основание (ноль) и отрицательная степень, выбрасывается исключение InvalidInputException.
# В методе main() мы запрашиваем у пользователя основание и показатель степени, вызываем метод calculatePower() и выводим результат. Если введены некорректные числа или происходит ошибка ввода, соответствующие исключения перехватываются и выводится информативное сообщение об ошибке.
# Обратите внимание, что в этой задаче мы использовали собственное исключение InvalidInputException, чтобы явно указать на некорректный ввод. Это помогает разделить обработку ошибок на соответствующие уровни абстракции

class InvalidInputException(Exception):
    pass

class PowerCalculator:
    @staticmethod
    def calculatePower(base, exponent):
        if base == 0 or exponent < 0:
            raise InvalidInputException("Invalid input: base cannot be zero and exponent cannot be negative")
        return pow(base, exponent)

def main():
    try:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        result = PowerCalculator.calculatePower(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    except ValueError as e:
        print("Invalid input:", e)
    except InvalidInputException as e:
        print(e)
        

if __name__ == '__main__':
    main()
