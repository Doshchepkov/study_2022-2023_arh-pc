---
## Front matter
title: "Отчёт по лабораторной работе №3"
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

%.pdf: %.md $(OUTPUT_DOTPNGS)
# Цель работы

Целью работы является изучить идеологию и применение
средств контроля версий. Приобрести практические навыки по работе с
системой git.

# Настройка github

![Создал учетную запись на github, чтобы выполнять дальнейшую работу.](image/1.png){ #fig:001 width=70% }

# Базовая настройка git 

![Сначала сделал предварительную конфигурацию git, настроил utf-8 в выводе сообщений git, задал имя начальной ветки (будем называть её master), также определил параметры autocrlf и safecrlf.](image/2.png){ #fig:002 width=70% }

# Создание SSh ключа

![На скрине выше для последующей идентификации пользователя на сервере репозиториев сгенерировал пару ключей (приватный и открытый)](image/3.png){ #fig:003 width=70% }

![При помощи команды cat скопировал в буфер обмена ключ](image/4.png){ #fig:004 width=70% }

![Скопированный ключ вставил в необходимое поле на github](image/5.png){ #fig:005 width=70% }

# Создание рабочего пространства и репозитория курса на основе шаблона

![Создаю каталог для предмета “Архитектура компьютера”](image/6.png){ #fig:006 width=70% }

# Создание репозитория курса на основе шаблона

![На github создал репозиторий с именем study_2022–2023_arh-pc](image/7.png){ #fig:007 width=70% }

![Перешел в ранее созданный каталог и клонировал туда только что созданный репозиторий с помощью команды gitclone –recursive “link”. Ссылку взял на github.](image/8.png){ #fig:008 width=70% }

# Настройка каталога курса

![Ничего особенного, просто удалил лишние файлы: rm package.json, создал необходимые каталоги: echo arch-pc > COURSE, make, отправил файлы на сервер: git add ., git commit -am 'feat(main): make course structure', git push.](image/9.png){ #fig:009 width=70% }

![Все корректно работает, появились необходимые папки на github, также контроль над выполнением процесса вел, просматривая каталоги самостоятельно (через один скрин выше)](image/10.png){ #fig:010 width=70% }

# Самостоятельная работа 

![Зашел на github в свой репозиторий, потомперешел в раздел labs, увидел 11 папок на для наших лабораторных работ.](image/11.png){ #fig:011 width=70% }

![](image/12.png){ #fig:012 width=70% }

![Перешел по нужному пути до папки report и загрузил туда первую лабораторную работу, аналогично загрузил вторую и третью.](image/13.png){ #fig:013 width=70% }
# Выводы:
Изучил идеологию средств контроля версий, приобрел практические
навыки по работе с системой git.
