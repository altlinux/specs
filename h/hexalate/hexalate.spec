Name: hexalate
Summary: A color matching game
Version: 1.0.1
Release: alt1
License: GPLv3+
Group: Games/Arcade
Url: http://gottcode.org/hexalate/
Source0: http://gottcode.org/hexalate/%name-%version-src.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Fri Apr 10 2009
BuildRequires: gcc-c++ libqt4-devel

%description
Hexalate is a color matching game. The goal of the game is to rotate and position the circles so that each touching line matches in color. You rotate circles by right clicking, and you move circles by dragging them. The game stores the positions and rotations of the circles across runs.

%prep
%setup

%build
qmake-qt4 PREFIX=%_prefix
%make_build
sed -i 's/Qt;Game;/Game;LogicGame;/' icons/%name.desktop

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README ChangeLog
%_bindir/*
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Wed Jun 02 2010 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Version up

* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- Repocop fail fixed

* Fri Apr 10 2009 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

