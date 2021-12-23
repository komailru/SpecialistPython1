# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here

    def summ(number):
        result = 0
        while number > 0:
            result = result + number % 10
            number = number // 10
        return result


    left3 = ticket_number // 1000
    right3= ticket_number % 1000
    return summ(left3) == summ(right3)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
