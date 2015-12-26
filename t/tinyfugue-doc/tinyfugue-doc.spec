Name: tinyfugue-doc
Version: 5.0beta8
Release: alt1
Summary: Console MUD client documentation
License: GPLv2
Group: Games/Other
Url: http://tinyfugue.sourceforge.net/
BuildArchitectures: noarch

Packager: %packager
Requires: tinyfugue

Source: %name-%version.tar

%description
TinyFugue is a console MUD client with versatile scripting.
In comparison to TinTin++ it supports more complex
scripts and triggers.

This package contains documentation for TinyFugue.

%description -l ru_RU.UTF-8
TinyFugue или tf - это свободный клиент для игр MUD
(многопользовательских подземелий, к примеру Discworld MUD).
Интерфейс классического консольный, поддерживаются
различные пользовательские скрипты. По сравнению с TinTin++
клиент поддерживает более сложные скрипты и триггеры.
В этом пакете содержится документация TinyFugue.

%prep
%setup

%build

%install
%define docdir %_docdir/%name-%version/documentation

mkdir -p %buildroot%docdir
mkdir %buildroot%docdir/commands
mkdir %buildroot%docdir/topics

install -pm644 commands/* %buildroot%docdir/commands/
install -pm644 topics/* %buildroot%docdir/topics/

install -pm644 COPYING %buildroot%docdir/
install -pm644 index.html %buildroot%docdir/

%files
%dir %docdir
%docdir/*

%changelog
* Sat Dec 26 2015 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt1
- Initial release for Sisyphus.
