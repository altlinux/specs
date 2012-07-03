Name: tornado
Version: 1.3
Release: alt1

Summary: Curses-based game of destroing enemy's house by controlling the weather
License: GPL
Url: http://kiza.kcore.de/software/tornado/
Group: Games/Arcade

Source: http://kiza.kcore.de/software/tornado/download/%name-%version.tar.gz
Patch: %name-%version.patch

# Automatically added by buildreq on Thu Jun 01 2006
BuildRequires: libncurses-devel coreutils

%description
The object of the game is to destroy your opponents house with the powers of rain, snow, hail, lightning and the tornado. It resembles the original C64 game.

%prep
%setup -q
%patch -p1

%build
%make

%install
%__mkdir_p %buildroot{%_bindir,%_datadir/locale,%_localstatedir/games}
#%__install  %buildroot%_bindir
%makeinstall ROOT=%buildroot

%files
%attr(2711,root,games) %{_bindir}/*
%attr(664,root,games) %_localstatedir/games/%{name}*
%_datadir/locale/*/*
%_mandir/*/*
%doc [A-LN-Z]*

%changelog
* Thu Mar 16 2006 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build for ALT

