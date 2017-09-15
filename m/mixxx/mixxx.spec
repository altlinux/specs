Name: mixxx
Version: 2.0.0
Release: alt1

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга
License: GPLv2+
Group: Sound
Url: http://mixxx.org

# https://github.com/mixxxdj/mixxx.git
Source: %name-%version.tar

Patch1: %name-%version-upstream-gcc6.patch
Patch2: %name-%version-alt-find-shout2.patch
Patch3: %name-%version-gentoo-sqlite3.patch
Patch4: %name-%version-gentoo-chromaprint-1.4.patch
Patch5: %name-%version-alt-rpath.patch

BuildPreReq: rpm-macros-qt5
BuildRequires: flex gcc-c++ libflac-devel libid3tag-devel libmad-devel
BuildRequires: libportaudio2-devel libportmidi libportmidi-devel
BuildRequires: libshout2-devel libsndfile-devel libtag-devel python-devel
BuildRequires: python-module-Reportlab python-module-bzr-fastimport scons
BuildRequires: swig libvamp-devel libprotobuf-devel
BuildRequires: libchromaprint-devel libusb-devel libfftw3-devel
BuildRequires: protobuf-compiler
BuildRequires: libGLU-devel librubberband-devel libshout2-devel libopus-devel libopusfile-devel libsqlite3-devel
BuildRequires: libwavpack-devel libfaad-devel libmp4v2-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-svg-devel qt5-xmlpatterns-devel qt5-tools-devel

Requires: %name-data = %version-%release
Requires: qt5-sql-sqlite3

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
scons \
	prefix=%_prefix \
	qtdir=%_qt5_prefix \
	qt5=1 \
	faad=1 \
	wv=1

%install
scons \
	prefix=%_prefix \
	qtdir=%_qt5_prefix \
	qt5=1 \
	faad=1 \
	wv=1 \
	install_root=%buildroot%_prefix \
	install

install -d %buildroot%_libdir
mv %buildroot%_libexecdir/mixxx/plugins/vamp \
	%buildroot%_libdir/

%files
%_bindir/%name

%files data
%exclude %_datadir/doc
%doc README README.md COPYING LICENSE Mixxx-Manual.pdf
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name-icon.png

%files -n vamp-%name-plugin
%_libdir/vamp

%changelog
* Thu Sep 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream release version 2.0.0.

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1.bzr20130612.2
- rebuild with fix libportmidi

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.11.0-alt1.bzr20130612.1
- Rebuilt for gcc5 C++11 ABI.

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
