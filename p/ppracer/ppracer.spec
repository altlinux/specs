%define contrib 20050629

Name: ppracer
Version: 0.3.1
Release: alt3.1

Summary: PlanetPenguin Racer 
License: GPL
Group: Games/Sports
URL: http://racer.planetpenguin.de/

Source0: ppracer-%version.tar.bz2
Source1: ppracer-contrib-%contrib.tar.bz2

Patch0: ppracer-0.3.1-alt-i18n.patch
Patch1: ppracer-0.3.1-alt-ui_lang.patch
Patch2: ppracer-0.3.1-alt-gcc41.patch
Patch3: ppracer-contrib-alt-hud.patch

# Automatically added by buildreq on Fri Sep 01 2006
BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel libX11-devel libXext-devel libXi-devel libXmu-devel libfreetype-devel libGL-devel libpng-devel tcl-devel

%description
PlanetPenguin Racer is an OpenGL racing game featuring Tux, the Linux mascot.
The goal of the game is to slide down a snow- and ice-covered mountain as
quickly as possible. It is based on the GPL version of TuxRacer.

%prep
%setup -q -a 1
%patch -p1
%patch1 -p1
%patch2 -p1
pushd %name-contrib-%contrib
%patch3 -p0
popd

%build
%configure --with-data-dir=%_gamesdatadir/%name --with-tcl=%_libdir
%make_build

%install
%make_install install DESTDIR=%buildroot

cd %name-contrib-%contrib
cp -a courses/* %buildroot%_gamesdatadir/%name/courses/contrib/
cp -a themes/* %buildroot%_gamesdatadir/%name/courses/

cat <<__MENU__ >%name.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=PP Racer
Comment=PlanetPenguin Racer
Icon=ppracer
Exec=ppracer
Terminal=false
Categories=Game;ArcadeGame;
__MENU__

install -pD -m644 %name.desktop %buildroot%_datadir/applications/%name.desktop
install -pD -m644 icons/ppracer-16x16.png %buildroot%_miconsdir/%name.png
install -pD -m644 icons/ppracer-32x32.png %buildroot%_niconsdir/%name.png
install -pD -m644 icons/ppracer-48x48.png %buildroot%_liconsdir/%name.png

%files
%doc AUTHORS ChangeLog
%_bindir/%name
%_gamesdatadir/%name
%_datadir/applications/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt3.1
- NMU: updated build dependencies

* Fri Sep 01 2006 Alexey Tourbin <at@altlinux.ru> 0.3.1-alt3
- fixed gcc-4.1 issue
- ppracer does not obsolete tuxracer any more
- specfile cosmetics

* Wed Jun 29 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.1-alt2
- fixed:
    + select UI language using current locale (#7024)
    + orthographical error in menu (#7025)
- added:
    + new official icons from CVS
    + many courses from CVS

* Mon Apr 11 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.1-alt1
- 0.3.1
- added --with-tcl=%%_libdir to make compile on x86_64

* Wed Jan 19 2005 Kachalov Anton <mouse@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Tue Dec 28 2004 Kachalov Anton <mouse@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Thu Dec 16 2004 Kachalov Anton <mouse@altlinux.ru> 0.2.1-alt1
- first build 
