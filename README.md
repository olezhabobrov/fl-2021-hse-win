# HW04

## 0

Дублирование описания языка из HW01:

Слова нашего языка: 

```
setAlphabet
setStates
setStart
makeTerminate
addEdge
```

Представляем автомат в виде графа, который задаем следующим образом:

* После setAlphabet: записываем используемый алфавит через запятую
* После setStatesAmount: записываем возможные состояния
* После setStart: записываем начальное положение
* После makeTerminate: записываем состояние, которое является терминальным
* После addEdge: записываем "текущее состояние, состояние перехода, буква из алфавита"

После двоеточия все параметры находятся в ковычках `"`

Если пользователь использует следующие символы, как часть алфавита: `':', ',', '"', '\'`, то он должен экранировать их с помощью `\`

**Пример 1.** Автомат, принимающий только пустое слово

Описание автомата на моем языке:

```
setAlphabet: "0, 1"
setStates: "q0, q1"
setStart: "q0"
makeTerminate: "q0"
addEdge: "q0, q1, 0"
addEdge: "q0, q1, 1"
addEdge: "q1, q1, 0"
addEdge: "q1, q1, 1"
```

## 1

### Федотова

Описание автомата на данном языке:

Автомат, принимающий только пустое слово:

```
Alphabet: 2 -- ("0", "1")
Q: 2
start: 1
T: 1 -- 1
edges: (1; 2; "0", "1"), (2; 2; "0", "1")
```

Нигде не нашел актуального описания языка (но возможно не там искал, если так, то извиняюсь), потому что в HW01 представлены некорректные примеры, в частности, не сказано, что
слова языка необходимо заключать в ковычки + нумерация состояний оказывается начинается с 1, а не с 0, как написано в HW01

Мне кажется, что не очень удобно, когда пользователь сам должен считать какому номеру состояния какое состояние соответствует, легко запутаться (хотя я сам только вчера исправил это у себя, так что не мне судить)

Нигде не сказано, что если есть несколько терминальных состояний, то их перечисление не надо заключать в скобки. И мне кажется это противоестественным, так как при перечислении 
алфавита и ребер, надо ставить скобки

В целом я считаю, что язык достаточно удобным, но очень сильно не хватило его описания, пришлось разбираться с ним, основываясь на примерах (да и то в HW01 они некорректны)

**Синтаксический анализатор**

В целом очень хорошие и понятные ошибки выдает, например:

* Автомат не детерминированный автомат: [ввод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/input.txt), [вывод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/input.txt.out)
* В автомате перепутано состояние: [ввод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/wrong_state.txt), [вывод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/wrong_state.txt.out)
* Автомат неполный [ввод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/missed_edge.txt), [вывод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/missed_edge.txt.out)

Однако есть и некоторые ошибки, которые анализатор не распознает:

* Количество символов в алфавите может быть абсолютно любым, оно как-то ни на что не влияет: [ввод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/incorrect_number.txt), [вывод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/incorrect_number.txt.out)
* Количество одинаковых символов, по которому можно перейти в другое состояние, может быть в принципе любое: [ввод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/several_edges.txt), [вывод](https://github.com/olezhabobrov/fl-2021-hse-win/blob/HW04/Fedotova/several_edges.txt.out)

Я не считаю данные неточности существенными, так что лично от меня жирный **LIKE** данному анализатору. Особенно понравилось, что, если ДКА неполный, то выводится ребро, которого не хватает

### Бондаренко

Описание автомата на данном языке:

Автомат, принимающий только пустое слово:

```
Alf: {0,1}
Start: 0
Vertices: 0(), 1(T)
Edges: (0, 1){0, 1}, (1,1){0,1}
```

Мне нравится этот язык, особенно, что при перечислении состояний можно сразу же указать, терминальная она или нет

К сожалению, парсер еще не доделан. Мне кажется такой язык действительно сложно парсить, так что понимаю...


## 2

Реализован в `parser/main.py`

Написаны несколько тестов: с корректным автоматом, с неполным и с повторяющимися словами из языка

## 3

Done
