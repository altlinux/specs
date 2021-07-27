%define _unpackaged_files_terminate_build 1
%define _cmake__builddir BUILD

Name: mixxx
Version: 2.3.0
Release: alt1.2

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга
License: GPL-2.0+
Group: Sound
Url: http://mixxx.org

# https://github.com/mixxxdj/mixxx.git
Source: %name-%version.tar

Patch1: %name-2.2.4-alt-find-shout2.patch
Patch2: %name-2.2.4-alt-rpath.patch

BuildPreReq: rpm-macros-qt5
# BuildPreReq: rpm-build-ninja
BuildRequires: flex gcc-c++ cmake libflac-devel libid3tag-devel libmad-devel
BuildRequires: libportaudio2-devel libportmidi-devel
BuildRequires: libsndfile-devel libtag-devel python-devel
BuildRequires: python-module-Reportlab scons
BuildRequires: swig libvamp-devel libprotobuf-devel
BuildRequires: libchromaprint-devel libusb-devel libfftw3-devel
BuildRequires: protobuf-compiler
BuildRequires: libGLU-devel librubberband-devel libopus-devel libopusfile-devel libsqlite3-devel
BuildRequires: libwavpack-devel libfaad-devel libmp4v2-devel
BuildRequires: libupower-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-svg-devel qt5-xmlpatterns-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: liblilv-devel libsoundtouch-devel libvorbis-devel libspeex-devel libtheora-devel
BuildRequires: liblame-devel libqtkeychain-qt5-devel libavcodec-devel libavformat-devel libavutil-devel libswresample-devel libavdevice-devel libavfilter-devel libpostproc-devel libswscale-devel
BuildRequires: libhidapi-devel libkeyfinder-devel libssl-devel

Requires: %name-data = %EVR
Requires: qt5-sql-sqlite3
Requires: bpm-tools

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

# %package -n vamp-%name-plugin
# Summary: %name plugin for Vamp
# Group: Sound
#
# %description -n vamp-%name-plugin
# Mixxx is free, open source DJ software that gives you everything
# you need to perform live mixes.
#
# This package contains %name plugin for Vamp.
#
# %package -n soundsource-%name-plugin
# Summary: %name plugin for Soundsource
# Group: Sound
#
# %description -n soundsource-%name-plugin
# Mixxx is free, open source DJ software that gives you everything
# you need to perform live mixes.
#
# This package contains %name plugin for Soundsource.

%prep
%setup
# %patch1 -p1
# %patch2 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
#
%cmake_build

%install
%cmake_install

# install -d %buildroot%_libdir
# mv %buildroot%_libexecdir/mixxx/plugins/vampqt5 \
# 	%buildroot%_libdir/
# mv %buildroot%_libexecdir/mixxx/plugins/soundsourceqt5 \
# 	%buildroot%_libdir/
mkdir -p %buildroot%_udevrulesdir/
mv %buildroot%_datadir/mixxx/udev/rules.d/* \
    %buildroot%_udevrulesdir/

%files
%_bindir/%name

%files data
%exclude %_datadir/doc
%doc README.md COPYING LICENSE res/Mixxx-Keyboard-Shortcuts.pdf
%_datadir/%name
%_datadir/metainfo/%name.metainfo.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/32x32/apps/%name.png
%_udevrulesdir/%name-usb-uaccess.rules

# %files -n vamp-%name-plugin
# %_libdir/vampqt5
#
# %files -n soundsource-%name-plugin
# %_libdir/soundsourceqt5

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1.2
- Fixed BuildRequires.

* Fri Jul 02 2021 Leontiy Volodin <lvol@altlinux.org> 2.3.0-alt1.1
- Adapted build for p9 branch.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.3.0-alt1
- Updated to upstream release version 2.3.0 (ALT #40319).
- Built with cmake and ninja.

* Tue Jun 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.4-alt1
- Updated to upstream release version 2.2.4.
- Added bpm-tools into Requires (ALT #39724).
- Built with internal libshout.

* Mon Jul 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream release version 2.1.1.

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
