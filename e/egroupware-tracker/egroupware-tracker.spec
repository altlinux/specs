%define setupdir egroupware

Name: egroupware-tracker
Version: 19.1.20200430
Release: alt1

Summary: EGroupware (bug-)tracking or helpdesk application
Summary(ru_RU.UTF-8): Приложение EGroupware для отслеживания инцидентов или организации службы поддержки

Group: Networking/WWW
License: GPLv2
Url: https://github.com/EGroupware/tracker

Source: %name-%version.tar
Requires: egroupware

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>

%description
EGroupware is a multi-user, web-based groupware suite.
Currently available modules include: email, addressbook, calendar, infolog (notes, to-do's, phone calls), 
content management, wiki, project management, tracker, timesheet, knowledge base, CalDAV/CardDAV.
Tracker is EGroupware (bug-)tracking or helpdesk application.

%description -l ru_RU.UTF-8
EGroupware - многопользовательская, web-ориентированная система групповой работы.
Доступные модули включают: электронную почту, адресные книги, календарь, инфожурнал (заметки, задачи, звонки),
управление контентом, вики, управление проектами, трекер, табель, базу знаний, CalDAV/CardDAV.
Трекер - приложение EGroupware для отслеживания инцидентов или организации службы поддержки.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%setupdir
cp -aRf tracker %buildroot%_datadir/%setupdir

%files
# каталог файлов установки
%_datadir/%setupdir

%changelog
* Fri May 22 2020 Pavel Isopenko <pauli@altlinux.org> 19.1.20200430-alt1
- initial build for Sisyphus





