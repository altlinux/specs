%define summary Ri-li arcade game

Name: Ri-li
Version: 2.0.1
Release: alt3.2

Summary: Ri-li arcade game
License: GPL v2 or GPL v3
Group: Games/Arcade
URL: http://www.ri-li.org

Source0: http://surfnet.dl.sourceforge.net/sourceforge/ri-li/%name-%version.tar.bz2

Patch0: Ri-li-2.0.1-alt-auto.patch
Patch1: Ri-li-2.0.1-alt-gcc43.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: %name-data = %version

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel

%description
Full-featured, 19 languages: Arabic, Breton, Chinese, English, Esperanto, French,
			     German, Italian, Japanese, Korean, Portuguese, Russian,
			     Slovak, Spanish, Swedish, Polish, Turkish, Hungarian, Dutch.
Colorful animated wood engine, 50 levels and 3 beautiful musics and many sound effects.

%package data
Summary: Data files for Ri-li arcade game
Group: Games/Arcade
BuildArch: noarch

Conflicts: %name < 2.0.1-alt3

%description data
Full-featured, 19 languages: Arabic, Breton, Chinese, English, Esperanto, French,
			     German, Italian, Japanese, Korean, Portuguese, Russian,
			     Slovak, Spanish, Swedish, Polish, Turkish, Hungarian, Dutch.
Colorful animated wood engine, 50 levels and 3 beautiful musics and many sound effects.

This is package contains data files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

install -d %buildroot%_niconsdir/ %buildroot%_miconsdir/ %buildroot%_liconsdir/
install -m 644 data/Ri-li-icon-16x16.png %buildroot%_miconsdir/%name.png
install -m 644 data/Ri-li-icon-32x32.png %buildroot%_niconsdir/%name.png
install -m 644 data/Ri-li-icon-48x48.png %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=Ri-li
GenericName=%summary
Comment=Drive a toy wood engine
Exec=Ri_li
Icon=Ri-li
Terminal=false
StartupNotify=false
Categories=Game;ArcadeGame;
EOF


%files
%doc AUTHORS COPYING.* NEWS README
%_bindir/Ri_li

%files data
%_datadir/%name/levels.dat
%_datadir/%name/COPYING.Music
%_datadir/%name/sprites.dat
%_datadir/%name/language.*
%_datadir/%name/Ri-li-icon-*.png
%_datadir/%name/*.ico
%_datadir/%name/Sounds/*
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%{name}.desktop

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3.2
- NMU: converted debian menu to freedesktop

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3.1
- friendly NMU from repocop: fixed _niconsdir.

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.0.1-alt3
- apply patch from repocop
- fix build with gcc4.3
- move data files to Ri-li-data subpackage and pack it as noarch
- buildreq

* Thu Jan 03 2008 Igor Zubkov <icesik@altlinux.org> 2.0.1-alt2
- fix rebuild with new autotools

* Tue Nov 27 2007 Igor Zubkov <icesik@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1
- license change from GPL to 'GPL v2 or GPL v3'

* Sat Aug 04 2007 Igor Zubkov <icesik@altlinux.org> 2.0.0-alt1
- build for Sisyphus

* Mon Oct 16 2006 Dominique Roux-Serret <roux-serret@ifrance.com> 2.0.0-1
- New Polish language.
- New Turkish language.
- New Hungarian language.
- New Dutch language.
- Animate when Ri-li is loading.
- 10 news levels. Now 50 levels.
- Correction of the languages : Japanese, German, Italian, Russian.
- Define AMIGAOS4 flags for Amiga OS4 system.
- Organization of the data files remade.
- Ri-Li can be launched without a sound card.
- Ri-li is limited to 60 fps to relieve the CPU.
- Ri-li use less ram memory.
* Thu Jul 19 2006 Dominique Roux-Serret <roux-serret@ifrance.com> 1.2.0-1
-  Addition a help in the game to direct the engine.
-  New Breton language.
-  New Esperanto language.
-  New Italian language.
-  New Portuguese language.
-  New Slovak language.
-  New Swedish language.
-  Correction of the languages : German, Japanese, Spanish.
* Thu Jul 07 2006 Dominique Roux-Serret <roux-serret@ifrance.com> 1.0.3-1
- $pkgdatadir is use in source for more compatibility in all distributions (gentoo, ..). Thanks to B. GANNE.
* Thu Jun 29 2006 Dominique Roux-Serret <roux-serret@ifrance.com> 1.0.2-1
- first RPM pakage.
