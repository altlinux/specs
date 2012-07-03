Name: xmmsctrl
Version: 1.9
Release: alt1

Summary: Xmmsctrl is a small xmms control program
Summary(ru_RU.UTF-8): Xmmsctrl - управление xmms из командной строки
License: GPL
Group: Sound
Url: http://www.cs.aau.dk/~adavid/utils/

Packager: Dmitriy Khanzhin <jinn@altlinux.ru>

Source0: %name-%version.tar.gz
Patch0: %name-1.8-alt-makefile.patch.bz2

Requires: xmms

# Automatically added by buildreq on Sat Apr 07 2007
BuildRequires: libxmms-devel

%description
Xmmsctrl is a small utility to control xmms from the command line.
Its goal is to be used coupled with sh to test xmms state and perform
an appropriate action, e.g. if playing then pause else play. The
interest of this is to bind keys in a window manager to have control
over xmms with keys that do play/next/pause, prev, control sound...

%description -l ru_RU.UTF-8
Xmmsctrl - это маленькая утилита для управления xmms из командной строки.
Она предназаначена для выполнения соответствующих действий c xmms из скриптов,
как то приостановка, продолжение, переход на следующую мелодию.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%make DESTDIR=%buildroot PREFIX=%buildroot install

%files
%doc README Changelog samples/
%_bindir/*

%changelog
* Sat Apr 07 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 1.9-alt1
- next version
- spec cleanup and converted to utf8
- updated URL and build requires
- change packager

* Thu May 13 2004 Egor S. Orlov <oes@altlinux.ru> 1.8-alt1
- version 1.8

* Thu Apr 01 2004 Egor S. Orlov <oes@altlinux.ru> 1.7-alt1
- new version

* Mon Jul 14 2003 Egor S. Orlov <oes@altlinux.ru> 1.6-alt1.1
- Added URL

* Tue Jul 08 2003 Egor S. Orlov <oes@altlinux.ru> 1.6-alt1
- Build for sisyphus
- Cleanup spec acording the policy

* Fri Jun 27 2003 Egor S. Orlov <oes@altlinux.ru> 1.6-alt0.1
- Initial build for ALT

