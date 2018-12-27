%define _unpackaged_files_terminate_build 1
Name:    dreamchess
Version: 0.3.0
Release: alt1.git5174b54

Summary: DreamChess is a user interface for playing chess.
License: GPL
URL: http://www.dreamchess.org/

Group: Games/Boards

Source: %name-%version.tar

Summary(ru_RU.UTF8): DreamChess - пользовательский интерфейс для игры в шахматы.

BuildRequires: cmake gcc-c++ bison flex libmxml-devel libGLEW-devel libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel 

Requires: %name-data = %EVR

%description
DreamChess is a user interface for playing chess. It comes with its own
engine called Dreamer. Both DreamChess and Dreamer are compatible with the
xboard/Winboard chess engine communication protocol. This means that
DreamChess can be used with other xboard-compatible chess engines such as
crafty (ftp://ftp.cis.uab.edu/pub/hyatt/) and GNU Chess
(http://www.gnu.org/software/chess/). Similarly, the Dreamer chess engine can
be used with other xboard-compatible user interfaces such as xboard and
Winboard (http://www.tim-mann.org/xboard.html) and recent editions of the
commercial chess program Chessmaster (http://www.chessmaster.com/).

%description -l ru_RU.UTF-8
DreamChess - пользовательский интерфейс для игры в шахматы. Она построена на своем собственной
движке - Dreamer. DreamChess и Dreamer совместимы с xboard/Winboard шахматными движками по протоколу.
Это означает, что DreamChess может быть использована с другими xboard-совместими шахматными движками, такие, как
crafty (ftp://ftp.cis.uab.edu/pub/hyatt/) и GNU Chess (http://www.gnu.org/software/chess/).
Кроме того, шахматный двигатель Dreamer может быть использован с другими xboard-совместимыми пользовательскими интерфейсами,
таких, как xboard и Winboard (http://www.tim-mann.org/xboard.html) и последними изданиями
коммерческой шахматной программы Chessmaster (http://www.chessmaster.com/).

%package data
Summary: Data files for DreamChess game
Group: Games/Boards
BuildArch: noarch
Requires: %name = %EVR

%description data
This package contains data files for DreamChess game

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%doc %_man6dir/*
%_datadir/doc/DreamChess

%files data
%_datadir/%name

%changelog
* Thu Dec 27 2018 Alexey Melyashinsky <bip@altlinux.org> 0.3.0-alt1.git5174b54
- Update to upstream snapshot 5174b54.

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt5.1
- Fixed build

* Wed May 12 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.2.0-alt5
- add Requires. Sorry.

* Wed May 12 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.2.0-alt4
- update BuildRequires
- Exctacted data files into separate package

* Mon Nov 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.2.0-alt3
- remove update_menus, clean_menus from spec file
    (update_menus repocop test)

* Mon Oct 27 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.2.0-alt2
- fix .desktop file

* Thu Oct 16 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.2.0-alt1
- Initial build
