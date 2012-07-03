%define altname Welcome2L

Name: welcome2l
Version: 3.04
Release: alt4

Summary: Linux ANSI boot logo
License: GPL
Group: System/Configuration/Boot and Init
Url: http://www.LittleIgloo.org

Source: %altname-%version.src.tar.bz2
Patch: %altname-3.04-alt-fixes.patch.bz2

%description
Welcome2L is a little program that may run at login time
to produce a BBS like ANSI login logo. It's very similar
to Linux_Logo. But where Linux_Logo intends to be portable,
Welcome2L intends to produce the best looking ANSI screens
by making full usage of PC graphic characters. Therefore
an architecture able to display those characters
(i386, Alpha with TGA adapter, ... ) is required to use it.
And, even if it will work on larger screens, it will only
produce 80 column ANSI screens.

%prep
%setup -q -n %altname-%version
%patch -p1

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
#%_man1dir/*
%doc AUTHORS ChangeLog INSTALL README THANKS

%changelog
* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 3.04-alt4
- rebuild with gcc3

* Sat Dec 01 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.04-alt3
- Patched for release.

* Thu Nov 08 2001 Sergey V Turchin <zerg@altlinux.ru> 3.04-alt2
- fixed %%Group

* Thu Oct 25 2001 Sergey V Turchin <zerg@altlinux.ru> 3.04-alt1
- initial version
