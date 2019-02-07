Name: tornado
Version: 1.4
Release: alt1

Summary: Curses-based game of destroing enemy's house by controlling the weather
License: GPL
Url: http://kiza.kcore.de/software/tornado/
Group: Games/Arcade

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
* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4
- Separate locales
- Convert russian lcale to UTF-8

* Thu Mar 16 2006 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build for ALT

