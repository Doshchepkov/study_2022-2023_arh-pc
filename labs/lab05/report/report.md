---
## Front matter
title: "Отчёт по лабораторной работе №5"
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

Освоение процедуры компиляции и сборки программ, написанных на ассемблере NASM.

# Программа Hello world!

![Уже перешел в созданный ранее каталог, в нем создал файл hello.asm, открыл файйл с помощью текстового редактора, и переписал текст из лабораторной работы](image/1.png){ #fig:001 width=80% }

# Транслятор NASM

![Превратил текст в объектный код с помощью соответсвующей команды](image/2.png){ #fig:002 width=80%}

# Расширенный синтаксис командной строки NASM

![Скомпилировал исходный файл в obj.o](image/3.png){ #fig:003 width=80% }

![Проверил содержимое каталога](image/31.png){ #fig:004 width=80% }

# Компоновщик LD

![Передал объектный файл на обработку компоновщику, проверил содержимое каталога, создал еще один исполняемый файл с именем main](image/4.png){ #fig:005 width=80%}

# Запуск исполняемого файла

![Запустил исполняемый файл](image/5.png){ #fig:006 width=80%}

#Задание для самостоятельной работы

![Скопировал файл hello.asm и назвал его lab5.asm, открыл новый файл через текстовый редактор, поменял фразу на свои имя и фамилию](image/6.png){ #fig:007 width=80% }


Текст программы: 

; hello.asm
SECTION .data ; Начало секции данных
    hello: DB 'Ощепков Дмитрий!',10 ; 'Ощепков Дмитрий!' плюс
; символ перевода строки
    helloLen: EQU $-hello ; Длина строки hello
SECTION .text ; Начало секции кода
    GLOBAL _start
_start: ; Точка входа в программу
    mov eax,4 ; Системный вызов для записи (sys_write)
    mov ebx,1 ; Описатель файла '1' - стандартный вывод
    mov ecx,hello ; Адрес строки hello в ecx
    mov edx,helloLen ; Размер строки hello
    int 80h ; Вызов ядра
    mov eax,1 ; Системный вызов для выхода (sys_exit)
    mov ebx,0 ; Выход с кодом возврата '0' (без ошибок)
    int 80h ; Вызов ядра
  
  
![Превратил текст в объектный код с помощью соответсвующей команды, скомпилировал исходный файл в lab5.o, создал исполняемый файл lab5, запустил программу](image/7.png){ #fig:008 width=80% }

![Отправил все содержимое каталога lab05 на github](image/8.png){ #fig:009 width=80% }

# Выводы

Освоил процедуры компиляции и сборки программ, написанных на ассемблере NASM.

::: {#refs}
:::
