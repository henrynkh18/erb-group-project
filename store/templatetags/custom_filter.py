from django import template

register = template.Library()

# @register.filter(name='currency')
# def currency(number):
#     return "HKD$ "+str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter(name='add')
def add(number, number1):
    if not number:
        number = 0
    return number + number1

@register.filter(name='minus')
def minus(number, number1):
    return number - number1

@register.filter(name='is_divisible')
def is_divisible(num, num1):
    if num % num1 == 0:
        return True
    else:
        return False
    
@register.filter(name='list_item')
def list_item(list, i):
    return list[i]

