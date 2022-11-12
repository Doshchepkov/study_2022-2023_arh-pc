---
## Front matter
title: "Отчёт по лабораторной работе №6"
subtitle: "Дисциплина: Архитектура компьютера"
author: "Ощепков Дмитрий Владимирович"

## Generic otions
lang: ru-RU
## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl
## Pdf output format
toc: true # Table of contents
toc-depth: 2
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---
# Цель работы

Приобретение практических навыков работы в Midnight Commander. Освоение
инструкций языка ассемблера mov и int.

# Выполнение лабораторной работы

![Перешел в mc в соответствующий каталог, создал файл lab6-1.asm](image/1.png){ #fig:001 width=70% }

![Ввел текст программы из листинга 6.1](image/2.png){ #fig:002 width=70% }

![Запустил программу, убедился в корректности совершенных действий](image/3.png){ #fig:003 width=70% }

#Подключение внешнего файла in_out.asm

![Скачал с ТУИСа внешний файл и положил в один каталог с файлом программы](image/4.png){ #fig:004 width=70% }

![Скопировал файл lab6-1.asm и переименовал в lab6-2.asm](image/5.png){ #fig:005 width=70% }

Сверху не видно строчку с подключением файла с помощью include
![Исправил текст программы в файле lab6-2.asm с использование подпрограмм из внешнего файла in_out.asm](image/6.png){ #fig:006 width=70% }

![Запустил программу](image/7.png){ #fig:007 width=70% }

![В файле lab6-2.asm заменил подпрограмму sprintLF на sprint. Теперь нет перехода на новую строчку](image/8.png){ #fig:008 width=70% }

#Самостоятельная работа 

![Скопировал файл lab6-1.asm и добавил туда корректировки, чтобы программа выводила введенную строку](image/9.png){ #fig:009 width=70% }

![Создал объектный и исполняемый файлы, запустил программу](image/10.png){ #fig:010 width=70% }

# Выводы

Приобрел практические навыки работы в Midnight Commander. Освоенил
инструкции языка ассемблера mov и int, начал вникать в синтаксис NASM.

