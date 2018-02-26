Name: wmacpi
Version: 2.2rc4
Release: alt0.1

Summary: This is a ACPI status monitor for Window Maker.
License: GPL
Group: Graphical desktop/Window Maker

Url: http://himi.org/wmacpi
Source0: http://himi.org/wmacpi/%name-%version.tar.bz2
Source1: %name.menu
Patch: wmacpi-2.1-alt-newld.patch
Packager: Pavlov Konstantin <thresh@altlinux.ru>

# Automatically added by buildreq on Sat May 06 2006
BuildRequires: libdockapp-devel libXext-devel libXpm-devel

Summary(ru_RU.KOI8-R): Удобный монитор состояния батарей для Window Maker

%description
This is an ACPI status monitor for Window Maker.
This version is a complete rewrite of wmacpi-1.34.

%description -l ru_RU.KOI8-R
Удобный монитор состояния батарей для Window Maker. Поддерживается ACPI.
Эта версия полностью переписана от версии wmacpi-1.34.

%prep
%setup
%patch -p1

%build
%make_build OPT="%optflags"

%install
install -pDcs -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1
install -pD -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS INSTALL README COPYING TODO ChangeLog
%_bindir/*
%_menudir/*
%_man1dir/%name.*

# TODO:
# - replace debian menufile with freedesktop one some day

%changelog
* Sat Jan 17 2009 Michael Shigorin <mike@altlinux.org> 2.2rc4-alt0.1
- NMU: 2.2rc4 (closes: #18543)
  + should be better regarding wakeups
- removed obsolete package scriptlets
- spec cleanup

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.2rc1-alt1
- 2.2rc1 release.
- Removed unneeded patches.

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.2a1-alt1
- 2.2a1 release.
- Spelling fixes.

* Tue Jun 27 2006 Igor Zubkov <icesik@altlinux.ru> 2.1-alt2.1
- fix changelog (thanks to mike@)

* Mon Jun 26 2006 Igor Zubkov <icesik@altlinux.ru> 2.1-alt2
- bump release
- spec clean up

* Sat May 06 2006 Igor Zubkov <icesik@altlinux.ru> 2.1-alt1
- 2.1
- fix seg fault (#8430) (patch from debian)
- add man from debian
- relocate to /usr/ from /usr/X11R6/
- buildreq

* Mon Apr 11 2005 Sir Raorn <raorn@altlinux.ru> 2.0rc1-alt1.1
- Rebuilt with new libdockapp

* Thu Sep 30 2004 Serge A. Volkov <vserge@altlinux.ru> 2.0rc1-alt1
- Update to new version 2.0rc1

* Wed Aug 18 2004 Serge A. Volkov <vserge@altlinux.ru> 1.99r7-alt1
- Update to new version 1.99r7

* Mon Sep 22 2003 Serge A. Volkov <vserge@altlinux.ru> 1.34-alt1
- initial build
