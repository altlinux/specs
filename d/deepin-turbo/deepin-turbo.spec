%define soname 0

Name: deepin-turbo
Version: 0.0.9.0.28.8f4b
Release: alt1
Summary: A daemon that helps to launch applications faster
License: LGPL-2.1-only and GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-turbo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Mon Sep 09 2024
# optimized out: cmake-modules dqt5-base-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-qml libdqt5-qmlmodels libdqt5-quick libdqt5-widgets libdqt5-x11extras libdqt5-xml libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libqt5-svg libsasl2-3 libssl-devel libstartup-notification libstdc++-devel pkg-config python3 python3-base sh5
BuildRequires: cmake dqt5-declarative-devel libdbus-devel libdtkdeclarative-devel libdtkwidget-devel libsystemd-devel

%description
%summary.
Deepin-trubo is a deepin project that derives from Applauncherd.

%package -n lib%name%soname
Summary: The library for %name
Group: System/Libraries

%description -n lib%name%soname
This package provides the library for %name.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
This package provides development files for %name.

%prep
%setup
# Fix python shebang.
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' scripts/library-helper.py
# Fix unmets.
sed -i 's|/usr/lib/binfmt.d|%_binfmtdir|' src/booster-desktop/CMakeLists.txt

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc CHANGELOG LICENSE README.md
%_bindir/deepin-turbo-invoker
%_bindir/deepin-turbo-single-instance
%_binfmtdir/binfmt.conf
%_userunitdir/*.service
%_libexecdir/%name/

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files devel
%_includedir/%name/
%_libdir/lib%name.so

%changelog
* Mon Sep 09 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.9.0.28.8f4b-alt1
- New version 0.0.9-28-g8f4b0a09.
- Built via separate qt5 instead system (ALT #48138).
- Upstream:
  + fix: dtkdeclarative changes the createApplication function.
  + chore: update license and copyright and readme.

* Thu Jun 09 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.6.3-alt1
- New version.
- Upstream:
  + fix: Repair the wm class name error using the window.
  + fix: The problem of collapse when the parameters are more frequent.
  + chore: Modify LGPL to GPL.
  + chore: V20 goes up booster service.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.0.5-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.5-alt1
- New version (0.0.5) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.3-alt1.git387889d
- Initial build for ALT Sisyphus.
