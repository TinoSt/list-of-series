import random
import math

list_of_series = []
event = 1


def create_serie_of_numbers(start_value, stop_value, elements):
    intervall = range(start_value, stop_value+1)
    serie = random.sample(intervall, k=elements)
    return serie


print("Stell dir eine Liste aus x Elementen vor. Jedes Element der Liste ist eine Zahl, die zwischen einem \n "
      "Minimalwert und einem Maximalwert liegt. Innerhalb der Liste darf jede Zahl nur einmal vorkommen. Wenn x \n"
      "z.B. den Wert 7 hat, der Minimalwert 1 beträgt und der Maximalwert 7 ist, dann könnte die Liste so \n"
      "ausschauen: [1, 2, 3, 4, 5, 6, 7]. Mithilfe dieses Programms wird eine Liste mit allen möglichen \n"
      "Kombinationen generiert.")

k = int(input("Bitte gib die Anzahl x der Elemente der Liste ein: "))
start = int(input("Bitte gib den Minimalwert der Zahlen innerhalb der Liste an: "))
stop = int(input("Bitte gib den Maximalwert der Zahlen innerhalb der Liste an: "))
n = stop - start + 1
maximum_number_of_events = math.factorial(n) / math.factorial(n - k)


while event <= maximum_number_of_events:
    pair = create_serie_of_numbers(start, stop, k)
    if pair not in list_of_series:
        list_of_series.append(pair)
        event += 1
    else:
        event = event


print(list_of_series)
