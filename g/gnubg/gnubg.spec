Name:		gnubg
Version:	1.05.000
Release:	alt1
Summary:	A backgammon game and analyser
License:	GPLv3
Group:		Games/Boards
Url:		http://www.gnubg.org
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source:		%name-release-%version-sources.tar.gz
Source1:	%name.desktop
Patch:		%name-1.04.000-no-python-win-deps.patch

Requires:	%name-data = %version-%release

# Automatically added by buildreq on Thu Nov 20 2014 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gnu-config libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libatk-devel libcairo-devel libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk2 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libncurses-devel libpango-devel libpangox-compat libpangox-compat-devel libpng-devel libtinfo-devel libwayland-client libwayland-server makeinfo pkg-config python-base python-devel python-modules rpm-build-gir shared-mime-info xorg-xproto-devel
BuildRequires: flex libcanberra-gtk2-devel libgtkglext-devel libreadline-devel libsqlite3-devel

%description
GNU Backgammon (@gnubg{}) is software for playing and analysing backgammon
positions, games and matches. It's based on a neural network. Although it
already plays at a very high level, it's still work in progress. You may
play GNU Backgammon using the command line or a graphical interface

Authors:
--------
Joseph Heled <joseph@gnubg.org>
Oystein Johansen <oystein@gnubg.org>
David Montgomery
Jim Segrave
Joern Thyssen <jth@gnubg.org>
Gary Wong <gtw@gnu.org>

%package data
Summary: Documentation and data files for gnubg
Group: Games/Boards
BuildArch: noarch
Requires: %name = %version-%release

%description data
This package contains the GNU Backgammon arch-independent data files and documentation.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
export LDFLAGS="$LDFLAGS -lpython2.7"
%configure \
--with-python \
--with-board3d
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
* Sat Jul 25 2015 Motsyo Gennadi <drool@altlinux.ru> 1.05.000-alt1
- new version

* Thu Nov 20 2014 Motsyo Gennadi <drool@altlinux.ru> 1.04.000-alt1
- 1.04.000 (based on spec-file from Serg A. kotlyarov <shadowsbrother at gmail dot com>)
