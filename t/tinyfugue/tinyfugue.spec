Name: tinyfugue
Version: 5.0beta8
Release: alt3
Summary: Console MUD client
License: GPLv2
Group: Games/Other
Url: http://tinyfugue.sourceforge.net/
Packager: %packager

Source: %name-%version.tar
Patch0: %name-5.0beta8-alt-extern.patch
Patch1: %name-5.0beta8-alt-warning-fixes.patch

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
%patch0 -p2
%patch1 -p1

%build
%add_optflags -fcommon
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
* Sat Nov 02 2024 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt3
- Fix various warnings popped up after gcc 14.2.1
- Fix extern declaration.

* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 5.0beta8-alt2
- Fixed FTBFS with -fcommon.

* Tue Dec 22 2015 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt1
- Initial release for Sisyphus.
