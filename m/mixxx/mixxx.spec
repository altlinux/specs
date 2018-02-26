Name: mixxx
Version: 1.10.0
Release: alt1

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга
License: GPLv2+
Group: Sound
Url: http://mixxx.org

Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar

BuildPreReq: rpm-macros-qt4
BuildRequires: cvs flex gcc-c++ libflac-devel libid3tag-devel libmad-devel
BuildRequires: libportaudio2-devel libportmidi libportmidi-devel
BuildRequires: libshout2-devel libsndfile-devel libtag-devel python-devel
BuildRequires: python-module-Reportlab python-module-bzr-fastimport scons
BuildRequires: swig time libqt4-devel
Requires: %name-data = %version-%release
Requires: libqt4-sql-sqlite

%description
Mixxx is free, open source DJ software that gives you everything 
you need to perform live mixes.

%description -l ru_RU.UTF-8
Mixxx - это бесплатная, с открытым исходным кодом программа для DJ,
дающая вам всё необходимое для живых выступлений.

%package data
Summary: Data files for Mixxx
Group: Sound
BuildArch: noarch

%description data
This package contains data files for Mixxx.

%prep
%setup

%build
scons qtdir=%_qt4dir prefix=%_prefix

%install
scons prefix=%_prefix install_root=%buildroot%_prefix install

%files
%_bindir/%name

%files data
%exclude %_datadir/doc
%doc README README.macro COPYING LICENSE Mixxx-Manual.pdf
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name-icon.png

%changelog
* Fri Dec 30 2011 Egor Glukhov <kaman@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sat Apr 23 2011 Egor Glukhov <kaman@altlinux.org> 1.9.0-alt3
- Qt's SQLite requirement

* Tue Mar 01 2011 Egor Glukhov <kaman@altlinux.org> 1.9.0-alt2
- Fixed desktop file

* Sun Feb 27 2011 Egor Glukhov <kaman@altlinux.org> 1.9.0-alt1
- 1.9.0

* Fri Nov 11 2010 Egor Glukhov <kaman@altlinux.org> 1.8.1-alt1
- 1.8.1
- Disabled LADSPA support (broken in 1.8 branch)
- Split data files into subpackage

* Fri May 28 2010 Egor Glukhov <kaman@altlinux.org> 1.7.2-alt1
- initial build for Sisyphus
