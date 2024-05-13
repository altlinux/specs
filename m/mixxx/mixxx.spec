%def_disable clang

%define _unpackaged_files_terminate_build 1
%define _cmake__builddir BUILD
%if_enabled clang
%define optflags_lto -flto=thin
%endif

Name: mixxx
Version: 2.4.1
Release: alt1

Summary: Free digital DJ software
Summary(ru_RU.UTF-8): Свободная программа для цифрового диджеинга

License: GPL-2.0+
Group: Sound
Url: http://mixxx.org

# https://github.com/mixxxdj/mixxx.git
Source: %name-%version.tar

Provides: %name-data = %EVR
Obsoletes: %name-data < %EVR
Requires: qt5-sql-sqlite

BuildPreReq: rpm-macros-qt5 rpm-build-ninja
# Automatically added by buildreq on Mon Feb 26 2024
# optimized out: cmake-modules fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libalsa-devel libavcodec-devel libavformat-devel libavutil-devel libcairo-gobject libdouble-conversion3 libfftw3-devel libflac-devel libfreetype-devel libgdk-pixbuf libgio-devel libglvnd-devel libgmock-devel libgpg-error liblame-devel libmp4v2-3 libogg-devel libopencore-amrnb0 libopencore-amrwb0 libopus-devel libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml librabbitmq-c4 libsamplerate-devel libsasl2-3 libserd-devel libsord-devel libsqlite3-devel libsratom-devel libssl-devel libstdc++-devel libvorbis-devel libx265-199 libxcb-devel libxcbutil-keysyms-devel libxkbcommon-devel libxkbfile-devel lv2-devel pipewire-jack-libs pipewire-libs pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel sh5 xorg-proto-devel xorg-xf86miscproto-devel zlib-devel
BuildRequires: cmake git-core libGLU-devel libavdevice-devel libavfilter-devel libbenchmark-devel libchromaprint-devel libdjinterop-devel = 0.20.2 libebur128-devel libgtest-devel libhidapi-devel libid3tag-devel libkeyfinder-devel libmad-devel libmicrosoft-gsl-devel libmodplug-devel libmp4v2-devel libopusfile-devel libportaudio2-devel libportmidi-devel libprotobuf-devel libqtkeychain-qt5-devel librubberband-devel libshout-idjc-devel libsndfile-devel libsoundtouch-devel libswresample-devel libswscale-devel libtag-devel libupower-devel libusb-devel libwavpack-devel lilv-devel protobuf-compiler qt5-declarative-devel qt5-svg-devel qt5-x11extras-devel
%if_enabled clang
BuildRequires: clang-devel llvm-devel-static
%else
BuildRequires: gcc-c++
%endif
# BuildRequires: /proc

%if_enabled clang
ExcludeArch: armh
%endif

%description
Mixxx is free, open source DJ software that gives you everything
you need to perform live mixes.

%description -l ru_RU.UTF-8
Mixxx - это бесплатная, с открытым исходным кодом программа для DJ,
дающая вам всё необходимое для живых выступлений.

%prep
%setup

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
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%exclude %_datadir/doc
%doc README.md COPYING LICENSE res/Mixxx-Keyboard-Shortcuts.pdf
%dir %_datadir/%name/
%dir %_datadir/%name/skins/
%dir %_datadir/%name/controllers/
%dir %_datadir/%name/effects/
%dir %_datadir/%name/keyboard/
%_datadir/%name/skins/*
%_datadir/%name/controllers/*
%_datadir/%name/controllers/.eslintrc.json
%_datadir/%name/effects/*
%_datadir/%name/keyboard/*.cfg
# package translations outside %%find_lang
%dir %_datadir/%name/translations/
%_datadir/%name/translations/mixxx_es_419.qm
# ---
%_datadir/metainfo/org.mixxx.Mixxx.metainfo.xml
%_desktopdir/org.mixxx.Mixxx.desktop
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_iconsdir/hicolor/??x??/apps/%name.png
%_iconsdir/hicolor/???x???/apps/%name.png
%_udevrulesdir/69-%name-usb-uaccess.rules

%changelog
* Mon May 13 2024 Leontiy Volodin <lvol@altlinux.org> 2.4.1-alt1
- New version 2.4.1.

* Mon Feb 26 2024 Leontiy Volodin <lvol@altlinux.org> 2.4.0-alt1
- New version 2.4.0.
- Cleanup BRs.

* Tue Oct 17 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.6-alt3.2
- Fixed file conflicts (ALT #48039).

* Wed Oct 11 2023 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt3.1
- NMU: fix requires

* Tue Oct 10 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.6-alt3
- Merged data subpackage for compatibility with packagekit.

* Mon Sep 11 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.6-alt2
- Spec:
  + Updated BuildRequires.
  + Fixed build with new ffmpeg.
  + Removed obsoleted patches.

* Wed Aug 16 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.6-alt1
- New version 2.3.6.

* Thu May 11 2023 Leontiy Volodin <lvol@altlinux.org> 2.3.5-alt1
- New version 2.3.5.

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
