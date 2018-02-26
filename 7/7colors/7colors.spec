%define rname sevencolors

Summary: Little addicting game, take over the gaming area with your color
Name: 7colors
Version: 0.80
Release: alt13
Source0: http://digilander.iol.it/sbel/7colors/%rname-%version.tar.bz2
URL: http://digilander.libero.it/sbel/7colors.english.html
Packager: Sergei Epiphanov <serpiph@altlinux.ru>
Source4: %name.menu
Source5: %name-16.xpm
Source6: %name-32.xpm
Source7: %name-48.xpm
Source8: %name.desktop
Patch0: %name-build.patch
License: GPLv2
Group: Games/Boards

# Automatically added by buildreq on Mon Jul 21 2008
BuildRequires: gnome-libs-devel gtk+-devel gtk+-devel

%description
7colors is a game for XWindow, for one or two players, the goal is to color the
50%% (plus one) of the rhombs on the screen, before the other player does. Each
turn the player choose a color, this color propagates from the own corner (the
lower left for player 1, the upper right for player 2) to all the neighbour
rhombs with the same color.

%prep
%setup -n %rname-%version -q
%patch0 -p1

%build
%configure
%make_build

%install
install -D src/%rname %buildroot%_bindir/%rname

#install -D -m644 %SOURCE4 %buildroot%_menudir/%name
install -D -m644 %SOURCE6 %buildroot%_niconsdir/%name.xpm
install -D -m644 %SOURCE5 %buildroot%_miconsdir/%name.xpm
install -D -m644 %SOURCE7 %buildroot%_liconsdir/%name.xpm
install -D -m644 %SOURCE8 %buildroot%_desktopdir/%name.desktop

%post

%postun

%files
%doc TODO README HISTORY
%_bindir/*
#_menudir/*
%_niconsdir/*.xpm
%_miconsdir/*
%_liconsdir/*
%_desktopdir/*

%changelog
* Sun Jun 03 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt13
- Fix build

* Wed May 23 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt12
- Fix with libgtk build

* Sat Oct 31 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt11
- Fix .desktop file repocop warning

* Sun Feb 08 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt10
- Fix .desktop file error

* Sat Jan 24 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt9
- Fix .desktop file install

* Mon Dec 15 2008 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt8
- Change .menu to .desktop

* Fri Jul 25 2008 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt7
- Add Packager tag

* Mon Jul 21 2008 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt6
- Cleanup spec

* Wed Sep 27 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.80-alt5
- Cleanup spec

* Thu Jan 09 2003 Rider <rider@altlinux.ru> 0.80-alt4
- build requires fix

* Fri Oct 11 2002 Rider <rider@altlinux.ru> 0.80-alt3
- gcc 3.2 rebuild

* Tue Nov 08 2001 Rider <rider@altlinux.ru> 0.80-alt2
- cleanup spec
- bug #000130 fixed (menu)

* Wed Apr 10 2001 Rider <rider@altlinux.ru>
- 0.80

* Tue Dec 12 2000 AEN <aen@logic.ru>
- cleanup spec
- build for RE

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 0.10-4mdk
- make rpmlint happy

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.10-3mdk
- capitalize menu, longtitle added

* Mon Oct  2 2000 Pixel <pixel@mandrakesoft.com> 0.10-2mdk
- add nice icons from author (Stefano Bellotti)

* Wed Sep 27 2000 Pixel <pixel@mandrakesoft.com> 0.10-1mdk
- initial spec

# end of file
