Name: tofu
Version: 3.2
Release: alt2

Summary: Tofu is plain (stupid) text-based todo(s) manager
License: GPL
Group: Office

Url: http://requiescant.tuxfamily.org/pages/PAGE20080212T.html
Source: %name-%version.tar.bz2
Packager: Malo Skryleve <malo@altlinux.org>

Requires: perl
BuildPreReq: perl-Encode
BuildArch: noarch

Summary(ru_RU.UTF-8): Тофу есть простейший текстовый распорядитель задач

%description
Tofu provides an easy, very lightweight, and effiscient way to manage
your todo list(s). It is primarily dedicated to (command-line addicted)
developers, but should be convenient for other usages (administration,
documentation, and so on).

The leading idea is quite simple: all the tasks are bundled in a plain
text file, then tofu provides an interface to order, tag and manipulate
(list, view, edit, delete, ...) them easily through built-in or
user-defined commands.

%description -l ru_RU.UTF-8
Тофу предоставляет простой, очень лёгкий и удобный способ управления
списком задач пользователя. Изначально он был посвящён разработчикам
"командной строки", т.е. тех, кто привык к работе с командною строкою,
но он пригоден также и для использования в иных областях, таких как:
распорядительство, написание документации и т.д.

В его основе лежит удивительно простой замысел: все задачи описаны и
связаны друг с другом в виде простого текстового файла. Тофу же
предоставляет интерфейс для управления, проставления меток,
и упорядочивания (отображения, правки, удаления, ...) сих задач с
помощью не сложных встроенных или определяемых пользователем команд.

%prep
%setup

%build
./configure --prefix=%prefix --mandir=%_mandir --docdir=%_docdir/%name-%version

%install
%makeinstall_std

%files
%doc CHANGELOG README
%_bindir/*
%_mandir/man?/*

%changelog
* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 3.2-alt2
- Fixed spec file

* Fri Feb 18 2011 Malo Skryleve <malo@altlinux.org> 3.2-alt1
- initial build for ALT Linux Sisyphus

