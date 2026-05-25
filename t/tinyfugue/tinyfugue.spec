Name: tinyfugue
Version: 5.2.2
Release: alt1
Summary: Console MUD client
License: GPLv2
Group: Games/Other
Url: https://github.com/ingwarsw/tinyfugue
Packager: %packager

Source: %name-%version.tar
Patch0: %%name-5.2.2-alt-remove-ICU_CFLAGS.patch

# Automatically added by buildreq on Mon May 25 2026
BuildRequires: libicu-devel libncurses-devel libpcre2-devel zlib-devel

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
%patch0 -p1

%build
%add_optflags -fcommon
./configure --prefix=%buildroot/usr
%make

%install
%make install
%define docdir %_docdir/%name-%version

mkdir -p %buildroot%docdir

install -pm644 CHANGES %buildroot%docdir/
install -pm644 COPYING %buildroot%docdir/
install -pm644 CREDITS %buildroot%docdir/
install -pm644 README.md %buildroot%docdir/

%files
%_bindir/*
%dir %_datadir/tf-lib
%_datadir/tf-lib/*

%dir %docdir
%docdir/*

%changelog
* Mon May 25 2026 Andrey Bergman <vkni@altlinux.org> 5.2.2-alt1
- Change upstream (Ken Keys is no longer developing it, new author Karol Lassak)

* Sat Nov 02 2024 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt3
- Fix various warnings popped up after gcc 14.2.1
- Fix extern declaration.

* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 5.0beta8-alt2
- Fixed FTBFS with -fcommon.

* Tue Dec 22 2015 Andrey Bergman <vkni@altlinux.org> 5.0beta8-alt1
- Initial release for Sisyphus.
