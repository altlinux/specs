%def_disable clang

%define repo dde-network-core
%define _cmake__builddir BUILD

Name: deepin-network-core
Version: 1.1.9
Release: alt1
Summary: Deepin desktop-environment - network core files
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-network-core

Source: %url/archive/%version/%repo-%version.tar.gz

BuildPreReq: rpm-build-ninja rpm-build-kf5
%if_enabled clang
BuildPreReq: clang-devel
%else
BuildPreReq: gcc-c++
%endif
BuildRequires: cmake qt5-base-devel kf5-networkmanager-qt-devel deepin-qt-dbus-factory-devel gsettings-qt-devel deepin-network-utils-devel
BuildRequires: qt5-tools-devel deepin-control-center deepin-control-center-devel dtk5-widget-devel dtk5-common libgtest-devel qt5-svg-devel deepin-dock-devel deepin-session-shell-devel libgio-devel

%description
Deepin desktop-environment - network core files.

%package devel
Summary: Development package for %name
Group: Development/C++

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
export CPLUS_INCLUDE_PATH=%_includedir/glib-2.0:%_libdir/glib-2.0/include:%_includedir/libnm:$CPLUS_INCLUDE_PATH
%K5cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%ifnarch i586 armh
mv -f %buildroot/usr/lib/{dde-control-center,dde-dock,dde-session-shell} %buildroot%_libdir
%endif
mkdir -p %buildroot%_bindir

%files
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/modules/
%_libdir/dde-control-center/modules/libdcc-network-plugin.so
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/libdock-network-plugin.so
%dir %_libdir/dde-session-shell/
%dir %_libdir/dde-session-shell/modules/
%_libdir/dde-session-shell/modules/libdss-network-plugin.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.network/
%_datadir/dsg/configs/org.deepin.dde.network/org.deepin.dde.network.json
/var/lib/polkit-1/localauthority/10-vendor.d/10-network-manager.pkla
%_libdir/libdde-network-core.so
%_datadir/dcc-network-plugin/
%_datadir/dock-network-plugin/
%_datadir/dss-network-plugin/

%files devel
%dir %_includedir/libddenetworkcore/
%_includedir/libddenetworkcore/*.h
%_pkgconfigdir/dde-network-core.pc

%changelog
* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.9-alt1
- New version.

* Tue Nov 15 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.71-alt1
- New version.
- Fixed FTBFS.

* Fri Aug 26 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.61-alt1
- Initial build for ALT Sisyphus.
