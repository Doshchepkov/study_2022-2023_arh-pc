---
## Front matter
title: "Отчет по лабораторной работе №4"
subtitle: "Дисциплина: Архитектура компьютера"
author: "Ощепков Дмитрий Владимирович"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
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
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью работы является освоение процедуры оформления отчетов с помощью
легковесного языка разметки Markdown.

#Установка Tex Live

![На странице официального сайта TeX Live https://www.tug.org/texlive/acqu ire-netinstall.html скачал архив install-tl-unx.tar.gz через терминал](image/24.png){ #fig:001 width=70% }

![Распаковал архив](image/25.png){ #fig:002 width=70% }

![Перешел в архив](image/26.png){ #fig:003 width=70% }

![Запустил скрипт установки командой и дождался окончания установки](image/27.png){ #fig:004 width=70% }

![Добавил /usr/local/texlive/2022/bin/x86_64-linux в мой PATH для текущей и будущих сессий](image/28.png){ #fig:005 width=70% }

# Установка Pandoc и Pandoc-crossref

![Почему-то через терминал не распознавались ссылки, поэтому я сам все через сайт скачал](image/29.png){ #fig:006 width=70% }

![Распаковал скачанные файлы, но перед эти перешел в каталог загрузок](image/30.png){ #fig:007 width=70% }

![Скопировал необходимые файлы в нужную папку.](image/31.png){ #fig:008 width=70% }

![Совершая все действия, мониторил корректность выполнения действий через меню, вызванное командой nautilus, также проверил верность выполненных заданий командой ls, все на своем месте.](image/32.png){ #fig:009 width=70% }

# Порядок выполнения лабораторной работы 

![Перешел в каталог курса сформированный при выполнении лабораторной работы №3 и обновил локальный репозиторий](image/21.png){ #fig:010 width=70% }

![Перешел в каталог с шаблоном отч
ета по лабораторной работе № 4 и провел компиляцию шаблона, после чего проверил, все ли на месте. Потом удалил полученные файлы с использованием Makefile.](image/22.png){ #fig:011 width=70% }

![Начал редактировать файл при помощи gedit](image/23.png){ #fig:012 width=70% }

Оформил 3 и 4 лаборатоные работы в Markdown и загрузил 4 лабораторную так же, как и третью

# Выводы

Здесь кратко описываются итоги проделанной работы.


