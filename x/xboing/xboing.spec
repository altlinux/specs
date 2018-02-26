Summary: A Breakout style X Window System based game.
Name: xboing
Version: 2.4
Release: alt1
License: MIT
Group: Games/Arcade
Patch1: 010_initial_patches.diff
Patch2: Imakefile.fhs.diff
Patch3: init.c.diff
Patch4: mousemove.diff
Patch5: speed_fix.diff
Patch6: xboing.6x_man_section.diff
Patch7: 030_auto_validate_yn.diff
Patch8: 040_manpage_errors.diff
Source: http://www.techrescue.org/%name/%{name}%{version}.tar.gz
Source1: %name.xpm
Source2: %name.desktop
Url: http://www.catt.rmit.edu.au/%name/%name.html
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Dec 10 2009
BuildRequires: gccmakedep imake libXext-devel libXpm-devel xorg-cf-files

%description
Xboing is an X Window System based game like the Breakout arcade game.
The object of the game is to keep a ball bouncing on the bricks until
you've broken through all of them.

%prep
%setup -q -n %name
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
cp %SOURCE1 .
cp %SOURCE2 .

%build
xmkmf -a
%make_build

%install
%makeinstall PREFIX=%buildroot
install -D -m 644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -D -m 644 %name.xpm %buildroot%_niconsdir/%name.xpm
install -D -m 664 /dev/null %buildroot%_localstatedir/games/%name.score
install -D -m 644 %name.man %buildroot%_man6dir/%name.6

%files
%doc README docs/problems.doc docs/todo.doc
%attr(2711,games,games) %_gamesbindir/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_man6dir/*
%config %attr(0664,games,games) %_localstatedir/games/%name.score

%changelog
* Sun Dec 16 2007 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Initial build from Debian Sid
