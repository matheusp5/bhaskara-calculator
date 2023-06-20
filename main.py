import math

try:
    a = int(input("Qual é o valor do A: "))
    b = int(input("Qual é o valor do B: "))
    c = int(input("Qual é o valor do C: "))

    delta = b ** 2 - 4 * a * c
    if delta < 0: delta = delta * -1
    print(delta)

    negative_b = b
    if b > 0:
        negative_b = b - (b * 2)

    variation_1 = (negative_b + (math.floor(math.sqrt(delta)))) / (2 * a)
    variation_2 = (negative_b - (math.floor(math.sqrt(delta)))) / (2 * a)

    result = f"{variation_1}; {variation_2}"
    if variation_1 > variation_2: result = f"{variation_2}; {variation_1}"

    print("S = {"+result+"}")
    print(f"x1 = {variation_1}")
    print(f"x2 = {variation_2}")
except Exception:
    print("Ocorreu um erro! Certifique-se de que todos os valores foram inseridos corretamente e se o erro persistir, contate um administrado ou abra uma issue em https://github.com/ofmxtheuuz/bhaskara-calculator")