Name:    dreamchess
Version: 0.2.0
Release: alt5

Summary: DreamChess is a user interface for playing chess.
License: GPL
URL: http://www.dreamchess.org/

Group: Games/Boards

Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name-16.png
Source3: %name-32.png
Source4: %name-48.png

Packager: Evgeny V. Shishkov <shev@altlinux.org>

Summary(ru_RU.UTF8): DreamChess - пользовательский интерфейс для игры в шахматы.

# Automatically added by buildreq on Wed May 12 2010
BuildRequires: libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libjpeg-devel libpng-devel libmxml-devel zlib-devel

Requires: %name-data = %version-%release

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
Requires: %name = %version-%release

%description data
This package contains data files for DreamChess game

%prep
%setup -q

%build
%configure --datadir=%_gamesdatadir/
%make_build

%install
%make_install DESTDIR="%buildroot/" install
%__install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%__install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png

%files
%defattr(-, root, root)
%_bindir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop
%doc README COPYING ChangeLog AUTHORS INSTALL
%doc %_man6dir/*

%files data
%_gamesdatadir/*

%changelog
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
