Name: solarwolf
Version: 1.5
Release: alt3.qa3.1

Summary: SolarWolf is an action/arcade game written entirely in Python

License: LGPL
Group: Games/Arcade
Url: http://pygame.org/shredwheat/solarwolf

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

BuildArchitectures: noarch

%add_python_req_skip py2exe

# manually removed: eric
# Automatically added by buildreq on Fri Dec 31 2004 (-bi)
BuildRequires: python-base python-modules-compiler python-modules-encodings rpm-build-python

%description
SolarWolf is an action/arcade game written entirely in Python.
It is free and open source, released under the LGPL license.

The game is originally based of one of my childhood favorites,
SolarFox on the Atari 2600.

The point of the game is to scramble through 60 levels
collecting space boxes. Each level gets is harder than
the previous. Obstacles like bullets, mines, and asteroids
cover your every move. Beat the Skip timer and grab the
powerups for your only chance.

Solarwolf runs on nearly every platform. Windows, Mac OSX, Linux,
BeOS, and a large variety of Unix platforms.

%prep
%setup -q

%build

%install

mkdir -p %buildroot/{%_gamesdatadir,%_iconsdir,%_mandir/man6,%_gamesbindir}
cp -p ./dist/*.png %buildroot/%_iconsdir
cp -p ./dist/%name.6.gz %buildroot/%_man6dir
install -D -m644 ./dist/%name.desktop %buildroot%_datadir/applications/%name.desktop
cp -p %name.py %buildroot/%_gamesbindir
#rm -rf ./dist
cp -rp ./ %buildroot/%_gamesdatadir/%name

cat >%buildroot%_gamesbindir/%name <<EOF
#!/bin/sh
cd %_gamesdatadir/%name
./%name.py
EOF

# TODO; merge me with upstream desktop file
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=SolarWolf
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%attr (0755, root root) %_gamesbindir/*
%doc readme.txt
%_gamesdatadir/%name
%_datadir/applications/%{name}.desktop
%_iconsdir/*
%_man6dir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt3.qa3.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3.qa3
- NMU: dropped obsolete menu entry; cleaned up desktop file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt3.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.5-alt3.1
- Rebuilt with python-2.5.

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt3
- add desktop file (fix bug #7614)

* Wed Mar 23 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt2
- rebuild with python 2.4

* Wed Jan 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1.1
- remove py2exe from requires

* Fri Dec 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- first build for ALT Linux Sisyphus
