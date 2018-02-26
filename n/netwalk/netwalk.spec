Name: netwalk
Version: 0.4.10
Release: alt3.qa2

Summary: NetWalk is a puzzle game where the object is to connect every terminal to the main server
URL: http://code.google.com/p/netwalk/
License: GPLv2+
Group: Games/Puzzles

Source0: %name-%version.tgz
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png

Patch0: %name-0.4.7-home.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sun Nov 16 2008
BuildRequires: libSDL-devel libSDL_ttf-devel

%description
NetWalk is a puzzle game where the object is to connect every terminal to the main server

In this version, not only must every terminal be connected, but every piece of
cable must also be connected to the main server somehow.
Click on a square to rotate its contents. A left click performs an
anticlockwise rotation and a right click performs a clockwise rotation.
You can select presets, or make a custom game in the options window.
There is one shortcut key: F2 starts a new game.

%prep
%setup -q
#patch0 -p1

%build
%make_build CFLAGS="%optflags -fomit-frame-pointer `sdl-config --cflags`"

%install
mkdir -p %buildroot%_usr/games/
install -pm 755 %name %buildroot%_usr/games/%name
mkdir -p %buildroot%_datadir/%name
install -D -pm 644 Vera.ttf %buildroot%_datadir/%name/Vera.ttf
mkdir -p %buildroot%_docdir/%name-%version
install -D -pm 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -pm 644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -pm 644 %SOURCE3 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=NetWalk
GenericName=NetWalk game
Comment=%{summary}
Icon=%{name}
Exec=%_usr/games/%name
Terminal=false
Categories=Game;LogicGame;
EOF

%files
%doc NEWS README copyright
%_usr/games/*
%_datadir/%name
%_desktopdir/%{name}.desktop
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.10-alt3.qa2
- NMU: converted debian menu to freedesktop

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.10-alt3.1
- friendly NMU from repocop (niconsdir fix).

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 0.4.10-alt3
- apply patch from repocop

* Wed Dec 26 2007 Igor Zubkov <icesik@altlinux.org> 0.4.10-alt2
- Update Url
- Clean up spec file
- Update License
- buildreq

* Sat Jan 13 2007 Igor Zubkov <icesik@altlinux.org> 0.4.10-alt1
- 0.4.8 -> 0.4.10 (closes #9985)

* Mon Mar 27 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.8-alt1
- 0.4.8
- buildreq

* Fri Mar 04 2005 Denis Klykvin <nikon@altlinux.ru> 0.4.7-alt3
- Build new version

* Sat Aug 21 2004 Denis Klykvin <nikon@altlinux.ru> 0.4.6-alt2
- Allowed key repeating
- Patch modified

* Thu Aug 05 2004 Denis Klykvin <nikon@altlinux.ru> 0.4.4-alt1
- Initial build
- Added patch for creating $HOME/.netwalk directory
