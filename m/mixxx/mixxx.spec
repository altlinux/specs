%def_disable clang

%define _unpackaged_files_terminate_build 1
%define _cmake__builddir BUILD
%if_enabled clang
%define optflags_lto -flto=thin
%endif

Name: mixxx
Version: 2.3.4
Release: alt1

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга
License: GPL-2.0+
Group: Sound
Url: http://mixxx.org

# https://github.com/mixxxdj/mixxx.git
Source: %name-%version.tar

Patch1: %name-2.2.4-alt-find-shout2.patch
Patch2: %name-2.2.4-alt-rpath.patch

Requires: %name-data = %EVR
Requires: qt5-sql-sqlite3

BuildPreReq: rpm-macros-qt5
BuildPreReq: rpm-build-ninja
%if_enabled clang
BuildRequires: clang-devel llvm-devel-static
%else
BuildRequires: gcc-c++
%endif
BuildRequires: flex git-core cmake libflac-devel libid3tag-devel libmad-devel
BuildRequires: libportaudio2-devel libportmidi-devel
BuildRequires: libsndfile-devel libtag-devel
#BuildRequires: scons
BuildRequires: swig libvamp-devel libprotobuf-devel
BuildRequires: libchromaprint-devel libusb-devel libfftw3-devel
BuildRequires: protobuf-compiler
BuildRequires: libGLU-devel librubberband-devel libopus-devel libopusfile-devel libsqlite3-devel
BuildRequires: libwavpack-devel libfaad-devel libmp4v2-devel
BuildRequires: libupower-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-svg-devel qt5-xmlpatterns-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: liblilv-devel libsoundtouch-devel libvorbis-devel libspeex-devel libtheora-devel
BuildRequires: liblame-devel libqtkeychain-qt5-devel libavcodec-devel libavformat-devel libavutil-devel libswresample-devel libavdevice-devel libavfilter-devel libpostproc-devel libswscale-devel libavresample-devel
BuildRequires: libhidapi-devel libkeyfinder-devel libssl-devel
BuildRequires: libebur128-devel libshout-idjc-devel libmodplug-devel

%if_enabled clang
ExcludeArch: armh
%endif

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
# %patch1 -p1
# %patch2 -p1

%build
%if_enabled clang
export CC=clang
export CXX=clang++
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_datadir/mixxx/controllers/novation-launchpad/scripts/compile-mapping.js
chmod +x %buildroot%_datadir/mixxx/controllers/novation-launchpad/scripts/compile-scripts.js

%files
%_bindir/%name

%files data
%exclude %_datadir/doc
%doc README.md COPYING LICENSE res/Mixxx-Keyboard-Shortcuts.pdf
%_datadir/%name
%_datadir/metainfo/org.mixxx.Mixxx.metainfo.xml
%_desktopdir/org.mixxx.Mixxx.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/??x??/apps/%name.png
%_iconsdir/hicolor/???x???/apps/%name.png
%_udevrulesdir/69-%name-usb-uaccess.rules

%changelog
* Mon Mar 06 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.4-alt1
- Updated to upstream release version 2.3.4.

* Thu Jun 23 2022 Leontiy Volodin <lvol@altlinux.org> 2.3.3-alt1
- Updated to upstream release version 2.3.3.
- Built via gcc again.

* Mon Feb 14 2022 Leontiy Volodin <lvol@altlinux.org> 2.3.2-alt1
- Updated to upstream release version 2.3.2 (ALT #41883).
- Removed bpm-tools from requires.

* Fri Dec 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.3.1-alt2
- Fixed build.
- Built with debuginfo.

* Thu Nov 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.3.1-alt1
- Updated to upstream release version 2.3.1.
- Built with cmake and ninja again.

* Thu Aug 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt2
- drop python2 packages from BR

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
