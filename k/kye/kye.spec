Summary: Clone of the classic Kye puzzle game
Name: kye
Version: 0.9.4
Release: alt2.1
Source: %name-%version.tar.gz
# wget -r -k -np -X /kye/download http://games.moria.org.uk/kye/
Source1: games.moria.org.uk-%version.tar
License: GPLv2+
Group: Games/Puzzles

Url: http://games.moria.org.uk/kye
BuildArch: noarch

# Automatically added by buildreq on Sun Apr 18 2010
BuildRequires: python-devel

%description
This is a clone of the game Kye for Windows, originally by Colin Garbutt. It
is a puzzle game, which is a little like the old falling-rocks puzzle games,
and perhaps also inspired a little by Sokoban. But Kye has more variety of
objects, and so is capable of posing quite complex puzzles.

%prep
%setup
tar xf %SOURCE1

%build
%python_build

cat << EOF >> %name.desktop
[Desktop Entry]
Type=Application
Version=1.0
Name=Kye
Icon=%name
Exec=Kye %%f
Terminal=false
Categories=Game;LogicGame;
EOF

cat << EOF >> %name-edit.desktop
[Desktop Entry]
Type=Application
Version=1.0
Name=Kye Level Editor
Exec=Kye-edit %%f
Icon=%name-edit
Terminal=false
Categories=Game;LogicGame;
EOF

%install
%python_install -O1

install -D kye-icon.png %buildroot%_miconsdir/%name.png
install -D kye-edit-icon.png %buildroot%_miconsdir/%name-edit.png

install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D %name-edit.desktop %buildroot%_desktopdir/%name-edit.desktop

cp games.moria.org.uk*/kye/*.kye %buildroot%_datadir/%name/

%files
%doc NEWS README COPYING games.moria.org.uk*/kye
%_datadir/%name
%python_sitelibdir/%{name}*
%_bindir/*
%_miconsdir/*
%_desktopdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.4-alt2.1
- Rebuild with Python-2.7

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 0.9.4-alt2
- Remove Vendor spec tag

* Mon Apr 19 2010 Fr. Br. George <george@altlinux.ru> 0.9.4-alt1
- Initial build from upstream spec

* Sat Apr 03 2010 Colin Phipps <cph@moria.org.uk> - 0.9.4-1
- workaround change in librsvg - CSS selector specificity seems to no longer take ID selectors into account? This affected rendering of many of the tiles.
- improve level complete dialog box.
- improve error feedback when tileset is not found.
- update for GTK 2.12.
- lots of changelog omitted here...

* Fri Mar 24 2006 Colin Phipps <cph@moria.org.uk> - 0.6.0
- Use Viktor's spec file as a starting point.

* Fri Jan 20 2006 Viktor Kerkez <alef@atomixlinux.org> - 0.5.0-1.ato
- Initial build for Atomix.

