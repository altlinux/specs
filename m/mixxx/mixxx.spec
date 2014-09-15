Name: mixxx
Version: 1.11.0
Release: alt1.bzr20130612

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга
License: GPLv2+
Group: Sound
Url: http://mixxx.org

Source0: %name-%version.tar

BuildPreReq: rpm-macros-qt4
BuildRequires: cvs flex gcc-c++ libflac-devel libid3tag-devel libmad-devel
BuildRequires: libportaudio2-devel libportmidi libportmidi-devel
BuildRequires: libshout2-devel libsndfile-devel libtag-devel python-devel
BuildRequires: python-module-Reportlab python-module-bzr-fastimport scons
BuildRequires: swig time libqt4-devel libvamp-devel libprotobuf-devel
BuildPreReq: libchromaprint-devel libusb-devel libfftw3-devel
BuildPreReq: protobuf-compiler
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

%package -n vamp-%name-plugin
Summary: %name plugin for Vamp
Group: Sound

%description -n vamp-%name-plugin
Mixxx is free, open source DJ software that gives you everything
you need to perform live mixes.

This package contains %name plugin for Vamp.

%prep
%setup

%build
scons qtdir=%_qt4dir prefix=%_prefix

%install
scons prefix=%_prefix install_root=%buildroot%_prefix install

install -d %buildroot%_libdir
mv %buildroot%_libexecdir/mixxx/plugins/vamp \
	%buildroot%_libdir/

%files
%_bindir/%name

%files data
%exclude %_datadir/doc
%doc README README.macro COPYING LICENSE Mixxx-Manual.pdf
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name-icon.png

%files -n vamp-%name-plugin
%_libdir/vamp

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.bzr20130612
- Version 1.11.0

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1.1
- Fixed build with glibc 2.16

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
