Name: tornado
Version: 1.4
Release: alt4

Summary: Curses-based game of destroing enemy's house by controlling the weather
License: GPLv2
Group: Games/Arcade

Url: https://github.com/kouya/tornado
Source: v%version.tar.gz
Patch: %name-1.4.patch

# Automatically added by buildreq on Tue Jan 29 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libncurses-devel libtinfo-devel python-base sh4
BuildRequires: libncursesw-devel

%description
The object of the game is to destroy your opponents house with the
powers of rain, snow, hail, lightning and the tornado. It resembles the
original C64 game.

%prep
%setup
%patch -p1
%ifarch %e2k
sed -i 's,-Og,-O%_optlevel,' Makefile.inc
%endif
sed -i 's/=CHARSET/=iso-8859-1/' po/pt.po po/no.po

%build
%make

%install
mkdir -p %buildroot{%_bindir,%_datadir/locale,%_localstatedir/games}
%makeinstall ROOT=%buildroot
%find_lang --with-man %name

%files -f %name.lang
%attr(2711,root,games) %_bindir/*
%attr(664,root,games) %_localstatedir/games/%{name}*
#_datadir/locale/*/*
%_man6dir/*
%doc [A-LN-Z]*

%changelog
* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 1.4-alt4
- Fix GCC15 build

* Mon Jul 17 2023 Fr. Br. George <george@altlinux.org> 1.4-alt3
- Rebuild with linbcurses6
- Fix UTF8 buffer underprovision

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 1.4-alt2
- E2K: proper optimization level

* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4
- Separate locales
- Convert russian lcale to UTF-8

* Thu Mar 16 2006 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build for ALT

