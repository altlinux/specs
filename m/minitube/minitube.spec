Name: minitube
Version: 1.7
Release: alt1
Summary: YouTube desktop client
License: LGPL
Group: Video
Url: http://flavio.tordini.org/minitube
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel
Requires: phonon-backend

%description
Minitube is a YouTube desktop client.

With it you can watch YouTube videos in a new way: you type a keyword,
Minitube gives you an endless video stream.

Minitube is not about cloning the original YouTube web interface, it aims
to create a new TV-like experience.

%prep
%setup

%build
qmake-qt4
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
%find_lang %name
rm -rf -- %buildroot%_iconsdir/hicolor/512x512

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name

%changelog
* Mon Feb 20 2012 Mykola Grechukh <gns@altlinux.ru> 1.7-alt1
- 1.7

* Fri Nov 25 2011 Egor Glukhov <kaman@altlinux.org> 1.6-alt1
- 1.6

* Sun Aug 21 2011 Egor Glukhov <kaman@altlinux.org> 1.5-alt1
- 1.5

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 1.4.3-alt1
- new version

* Fri Jan 14 2011 Egor Glukhov <kaman@altlinux.org> 1.3-alt1
- 1.3

* Fri Sep 10 2010 Egor Glukhov <kaman@altlinux.org> 1.1-alt1.git.da913cd7
- Initial build for Sisyphus
