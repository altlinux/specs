Name:		Stringrolled
Version:	4
Release:	alt1.1
Summary:	Help a cat and a princess escape a castle
License:	Public Domain
Group:		Games/Arcade
Source:		Stringrolled_4.zip
Source1:	16x16.png
Source2:	24x24.png
Source3:	48x48.png
URL:		http://www.pyweek.org/e/Rambo
BuildArch:	noarch

# Automatically added by buildreq on Mon Jun 20 2011
# optimized out: python-base
BuildRequires: unzip

%description
Help a cat and a princess escape a castle in this _epic_ platformer.
The game provides oldschool EGA-style graphics and puzzling gameplay.

%prep
%setup -n %name

%build
cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Version=1.0
Name=%name
GenericName=EGA-styled platform puzzle arcade
Comment=%summary
Icon=%name
Exec=%name
Terminal=false
StartupNotify=false
Categories=Game;ArcadeGame;
@@@

cat > %name.sh <<@@@
#!/bin/sh -e
GHOME="\$HOME/.%name"
test -d "\$GHOME" || {
mkdir -p "\$GHOME"
cp -as %python_sitelibdir_noarch/%name "\$GHOME/gamelib"
cp -a %_gamesdatadir/%name "\$GHOME/data"
}
cd "\$GHOME"
python -c "from gamelib import main; main.main()"
@@@

cp %SOURCE1 %SOURCE2 %SOURCE3 .

%install
mkdir -p %buildroot%_gamesdatadir
mkdir -p %buildroot%python_sitelibdir_noarch
cp -a data %buildroot%_gamesdatadir/%name
cp -a gamelib %buildroot%python_sitelibdir_noarch/%name
install -Dm755 %name.sh %buildroot%_gamesbindir/%name
for n in 16 24 48; do
  install -D ${n}x${n}.png %buildroot%_iconsdir/hicolor/${n}x${n}/apps/%name.png
done
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files 
%doc README.txt
%python_sitelibdir_noarch/%name
%_gamesdatadir/%name
%_gamesbindir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4-alt1.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 4-alt1
- Initial build from scratch

