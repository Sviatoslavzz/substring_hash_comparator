## Реализация алгоритма определения равенства подстрок

Дана строка S, состоящая из строчных латинских букв.
Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.

### Формат ввода

В первой строке записана S (1 ≤ |S| ≤ 2 ⋅ $10^5$), состоящая из строчных латинских букв.
Во второй строке записано число Q (1 ≤ Q ≤ 2 ⋅ $10^6$) — количество запросов.
В следющих Q строках записаны запросы: целые числа L, A и B (1 ≤ L ≤ |S|, 0 ≤ A, B ≤ (|S| - L)) — длина подстрок и позиции, с которых они начинаются.
### Формат вывода

Если строки совпадают — выведите "yes", иначе — "no".

#### Пример ввода
acabaca  
3  
4 3 2  
3 4 0  
2 0 1  

#### Пример вывода
no  
yes  
no  
