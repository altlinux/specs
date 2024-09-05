%define repo dde-widgets

%def_disable clang

Name: deepin-widgets
Version: 6.0.22
Release: alt1

Summary: Desktop widgets service/implementation for DDE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-widgets

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: deepin-widgets-6.0.22-upstream-link-libdde-calendarwidget-plugin.patch

Provides: %repo = %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
BuildRequires: cmake dtkcore libdtkwidget-devel dqt5-svg-devel dqt5-x11extras-devel libgtest-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package devel
Summary: Development files for %repo
Group: Development/C++

%description devel
The package provides development files for %repo.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_userunitdir/%repo.service
%dir %_userunitdir/dde-osd.target.wants/
%_userunitdir/dde-osd.target.wants/%repo.service
%dir %_libdir/%repo/
%dir %_libdir/%repo/plugins/
%_libdir/%repo/plugins/libdde-memorymonitorwidget-plugin.so
%_libdir/%repo/plugins/libdde-notificationwidget-plugin.so
%_libdir/%repo/plugins/libdde-worldclockwidget-plugin.so
%_libdir/%repo/plugins/libdde-calendarwidget-plugin.so
%_datadir/dbus-1/services/org.deepin.dde.Widgets1.service
%_libdir/libdde-widgets.so

%files devel
%dir %_includedir/%repo/
%_includedir/%repo/*.h
%dir %_libdir/cmake/DdeWidgets/
%_libdir/cmake/DdeWidgets/DdeWidgetsConfig.cmake

%changelog
* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.22-alt1
- New version 6.0.22.
- Built via separate qt5 instead system (ALT #48138).

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- Initial build for ALT Sisyphus.
- Applied fixes from upstream branch.
