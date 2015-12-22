Name: tinyfugue
Version: 5.0beta8
Release: alt1
Summary: Console MUD client
License: GPLv2
Group: Games/Other
Url: http://tinyfugue.sourceforge.net/
Packager: %packager

Source: %name-%version.tar

%description
TinyFugue is a console MUD client with versatile scripting.
In comparison to TinTin++ it supports more complex
scripts and triggers.

%description -l ru_RU.UTF-8
TinyFugue или tf - это свободный клиент для игр MUD
(многопользовательских подземелий, к примеру Discworld MUD).
Интерфейс классического консольный, поддерживаются
различные пользовательские скрипты. По сравнению с TinTin++
клиент поддерживает более сложные скрипты и триггеры.

%prep
%setup

%build
%configure
%make

%install
%define docdir %_docdir/%name-%version

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%docdir
mkdir -p %buildroot%_datadir/tf-lib

install -pm755 src/tf %buildroot/%_bindir/

install -pm644 tf-lib/* %buildroot%_datadir/tf-lib

install -pm644 CHANGES %buildroot%docdir/
install -pm644 COPYING %buildroot%docdir/
install -pm644 CREDITS %buildroot%docdir/
install -pm644 README %buildroot%docdir/

%files
%_bindir/*
%dir %_datadir/tf-lib
%_datadir/tf-lib/*

%dir %docdir
%docdir/*

%changelog
* Tue Dec 22 2015 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt1
- Initial release for Sisyphus.


