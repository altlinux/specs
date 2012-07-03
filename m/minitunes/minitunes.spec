Name: minitunes
Version: 1.0
Release: alt1
Summary: Minitunes is just another music player, only better
License: GPLv3
Group: Sound
Url: http://flavio.tordini.org/minitunes
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: gcc-c++ libqt4-devel libtag-devel
Requires: phonon-backend

%description
Minitunes is just another music player, only better.

Minitunes unclutters your music listening experience with a clean
and innovative interface.

%prep
%setup

%build
qmake-qt4 PREFIX=/usr INCLUDEPATH=/usr/include/kde4
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
%find_lang %name

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name

%changelog
* Sun Oct 09 2011 Egor Glukhov <kaman@altlinux.org> 1.0-alt1
- New version

* Tue Jan 25 2011 Egor Glukhov <kaman@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
