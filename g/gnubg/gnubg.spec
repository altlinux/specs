Name:       gnubg
Version:    1.06.002
Release:    alt1
Summary:    A backgammon game and analyser
License:    GPLv3
Group:      Games/Boards
Url:        http://www.gnubg.org
Packager:   Motsyo Gennadi <drool@altlinux.ru>
Source:     %name-%version.tar
Source1:    %name.desktop
Patch:      %name-1.04.000-no-python-win-deps.patch

Requires:   %name-data = %version-%release

BuildRequires: flex libcanberra-gtk2-devel libgtkglext-devel libreadline-devel libsqlite3-devel

ExclusiveArch: %ix86 x86_64

%description
GNU Backgammon (@gnubg{}) is software for playing and analysing backgammon
positions, games and matches. It's based on a neural network. Although it
already plays at a very high level, it's still work in progress. You may
play GNU Backgammon using the command line or a graphical interface

%package data
Summary: Documentation and data files for gnubg
Group: Games/Boards
Requires: %name = %version-%release

%description data
This package contains the GNU Backgammon arch-independent data files and documentation.

%prep
%setup
%patch -p1

%build
./configure --with-python=no \
    --prefix=/usr \
    --datadir=/usr/share \
    --enable-simd=no
%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_desktopdir
install -p -m644 %SOURCE1 %buildroot%_desktopdir

%find_lang %name

%files
%_bindir/*
%_desktopdir/*

%files data -f %name.lang
%doc TODO INSTALL NEWS AUTHORS README ChangeLog
%_datadir/icons/hicolor/22x22/apps/*
%_datadir/icons/hicolor/24x24/apps/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/man/*/*
%_datadir/doc/%name
%_datadir/%name

%changelog
* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.06.002-alt1
- Just fix version number.

* Wed Sep 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.06.001-alt1
- Build new version (based on spec-file from drool@).
- Appstream says it made a work on AVX issue (Closes: #31209).

* Sat Jul 25 2015 Motsyo Gennadi <drool@altlinux.ru> 1.05.000-alt1
- new version

* Thu Nov 20 2014 Motsyo Gennadi <drool@altlinux.ru> 1.04.000-alt1
- 1.04.000 (based on spec-file from Serg A. kotlyarov <shadowsbrother at gmail dot com>)
