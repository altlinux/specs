Name: pathological
Version: 1.1.3
Release: alt3.qa3.1

Summary: Pathological - Logical game written in Python

License: GPL
Group: Games/Arcade
Url: http://pathological.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

Requires: python-module-pygame
BuildArchitectures: noarch

%description
Pathological is an enriched clone of the game "Logical" by Rainbow Arts. 
To solve a level, fill each wheel with four marbles of matching color. 
Various board elements such as teleporters, switches, filters, etc., 
make the game interesting and challenging. 
New levels can be created using your favorite text editor. 

%prep
%setup -q

%build

%install
mkdir -p %buildroot/%_gamesdatadir/%name
cp -pr ./ %buildroot/%_gamesdatadir/%name

mkdir -p %buildroot%_gamesbindir
cp %name %buildroot%_gamesbindir

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Pathological
Comment=Pathological - Logical game written in Python
Icon=%{name}
Exec=%_gamesbindir/%name
Terminal=false
Categories=Game;LogicGame;
EOF

%files
#%doc README changelog
%_gamesbindir/%name
%_gamesdatadir/%name
%_desktopdir/%{name}.desktop
#%_iconsdir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt3.qa3.1
- Rebuild with Python-2.7

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt3.qa3
- NMU: converted menu to desktop file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt3.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1.3-alt3.1
- Rebuilt with python-2.5.

* Mon May 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt3
- add pygame require (fix bug #6850)

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt2
- rebuild with python 2.4

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- first build for ALT Linux Sisyphus
