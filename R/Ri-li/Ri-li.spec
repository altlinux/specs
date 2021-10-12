%define summary Ri-li arcade game

Name: Ri-li
Version: 2.0.1
Release: alt4

Summary: Ri-li arcade game
License: GPL v2 or GPL v3
Group: Games/Arcade
URL: http://www.ri-li.org

Source0: http://surfnet.dl.sourceforge.net/sourceforge/ri-li/%name-%version.tar.bz2

Patch0: Ri-li-2.0.1-alt-auto.patch
Patch1: Ri-li-2.0.1-gcc43.patch
Patch2: Ri-li-gcc11.patch

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
%patch2 -p1

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
Name=Ri-li
GenericName=%summary
Comment=Drive a toy wood engine
Exec=Ri_li
Icon=Ri-li
Terminal=false
StartupNotify=false
Categories=Game;ArcadeGame;Simulation;
Keywords=game;train;toy;wood;engine;switches;kids;
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
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.0.1-alt4
- NMU: fixed build

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.1-alt3.2.qa1
- NMU: rebuilt for updated dependencies.

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
