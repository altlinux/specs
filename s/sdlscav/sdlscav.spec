
Name: sdlscav
Version: 144
Release: alt4

Group: Games/Arcade
Summary: Cool arcade/thinking game very much like Lode Runner
Url: http://www.xdr.com/dash/scavenger.html
License: GPL

# Automatically added by buildreq on Mon Mar 28 2011 (-bi)
BuildRequires: libSDL-devel

Source: http://www.xdr.com/dash/%name-%version.tar.bz2
Source10: %name.16.xpm
Source11: %name.32.xpm
Source12: %name.48.xpm

Patch1: sdlscav-144-datapath.patch

%description
SDL Scavenger is a cool arcade/thinking game very much like Lode Runner.
You've got to run around and collect objects while avoiding enemies. Some
objects are buried and you've got to dig down to get at them. It's an
addictive game and some of the levels are devilishly (cruelly) complicated
to solve.

%prep
%setup -q
%patch1 -p1
[ -f data/regulargui.lbm -a ! -f data/regularguy.lbm ] ||
    mv data/regularguy.lbm data/regulargui.lbm

%build
%make_build CFLAGS="%optflags `sdl-config --cflags`" -C src

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_gamesdatadir/%name
install -m 0755 src/%name %buildroot%_gamesbindir/
for f in data/*
do
    install -m 0644 $f %buildroot%_gamesdatadir/%name/
done

mkdir -p %buildroot/%_desktopdir/
cat << __EOF__ > %buildroot/%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=SDL Scavenger
Name[ru]=SDL Scavenger
Comment=Cool arcade/thinking game very much like Lode Runner
Comment[ru]=Клевая игра для спинного и головного мозга типа Lode Runner
Icon=sdlscav
Exec=sdlscav
Terminal=false
Categories=Game;ArcadeGame;
__EOF__

mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_liconsdir
install -m 0644 %SOURCE10 %buildroot%_miconsdir/%name.xpm
install -m 0644 %SOURCE11 %buildroot%_niconsdir/%name.xpm
install -m 0644 %SOURCE12 %buildroot%_liconsdir/%name.xpm


%files
%doc README DOC
%_gamesbindir/*
%_gamesdatadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm

%changelog
* Mon Mar 28 2011 Sergey V Turchin <zerg@altlinux.org> 144-alt4
- add freedesktop menu entry

* Thu Jan 14 2010 Sergey V Turchin <zerg@altlinux.org> 144-alt3
- fix icons placement
- remove deprecated macroses

* Fri Jul 20 2007 Sergey V Turchin <zerg at altlinux dot org> 144-alt2
- fix data locations

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 144-alt1
- new version

* Thu Dec 25 2003 Sergey V Turchin <zerg at altlinux dot org> 137-alt3
- fix menu to launch via soundwrapper
- cleanup spec
- rebuild

* Tue Sep 24 2002 Sergey V Turchin <zerg@altlinux.ru> 137-alt2
- rebuild with gcc3.2

* Fri Jul 06 2001 Sergey V Turchin <zerg@altlinux.ru> 137-alt1
- first ALT release
