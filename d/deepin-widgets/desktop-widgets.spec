%define repo dde-widgets

%def_disable clang

Name: deepin-widgets
Version: 6.0.20
Release: alt1

Summary: Desktop widgets service/implementation for DDE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-widgets

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: %repo = %EVR

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake dtkcore libdtkwidget-devel qt5-svg-devel qt5-x11extras-devel libgtest-devel
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
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
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
* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- Initial build for ALT Sisyphus.
- Applied fixes from upstream branch.
