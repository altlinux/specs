%def_without clang

%define repo dde-network-core
%define sover 2
%define _cmake__builddir BUILD

Name: deepin-network-core
Version: 2.0.26
Release: alt1
Summary: Deepin desktop-environment - network core files
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-network-core

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: deepin-network-core-2.0.20-alt-GNUInstallDirs.patch

BuildPreReq: rpm-build-ninja rpm-build-kf5 rpm-macros-dqt5
%if_with clang
BuildPreReq: clang-devel
%else
BuildPreReq: gcc-c++
%endif
# Automatically added by buildreq on Wed Oct 25 2023
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdcc-interface6 libdcc-widgets6 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libgio-devel libglvnd-devel libgpg-error libgsettings-qt libnm-devel libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel pkg-config python3 python3-base dqt5-base-devel dqt5-tools sh5
BuildRequires: cmake deepin-control-center-devel deepin-dock-devel deepin-session-shell-devel gsettings-qt-devel kf5-networkmanager-qt-devel libdtkwidget-devel libgtest-devel dqt5-svg-devel dqt5-tools-devel

%description
Deepin desktop-environment - network core files.

%package -n lib%repo%sover
Summary: Library for %name
Group: System/Libraries

%description -n lib%repo%sover
This package provides library for %name.

%package -n lib%repo-devel
Summary: Development package for %name
Group: Development/C++
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%repo-devel
This package provides development files for %name.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export CPLUS_INCLUDE_PATH=%_includedir/glib-2.0:%_libdir/glib-2.0/include:%_includedir/libnm:$CPLUS_INCLUDE_PATH
# %%K5cmake fails build on ppc64le
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_EXE_LINKER_FLAGS:STRING='-L%_K5lib -L%_K5link' \
  -DCMAKE_MODULE_LINKER_FLAGS:STRING='-L%_K5lib -L%_K5link' \
  -DCMAKE_SHARED_LINKER_FLAGS:STRING='-L%_K5lib -L%_K5link' \
  -DCMAKE_LIBRARY_PATH='%_K5link;%_K5lib;/%_lib' \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt --output=%name.lang dde-control-center dock-network-plugin dss-network-plugin

%files -f %name.lang
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/modules/
%_libdir/dde-control-center/modules/libdcc-network-plugin.so
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%dir %_libdir/dde-dock/plugins/quick-trays/
%_libdir/dde-dock/plugins/quick-trays/libdock-network-plugin.so
%dir %_libdir/dde-session-shell/
%dir %_libdir/dde-session-shell/modules/
%_libdir/dde-session-shell/modules/libdss-network-plugin.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.network/
%_datadir/dsg/configs/org.deepin.dde.network/org.deepin.dde.network.json
/var/lib/polkit-1/localauthority/10-vendor.d/10-network-manager.pkla
# package translations outside %%find_lang
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%_datadir/dde-control-center/translations/dcc-network-plugin.qm
%dir %_datadir/dock-network-plugin/
%dir %_datadir/dock-network-plugin/translations/
%_datadir/dock-network-plugin/translations/dock-network-plugin.qm
%dir %_datadir/dss-network-plugin/
%dir %_datadir/dss-network-plugin/translations/
%_datadir/dss-network-plugin/translations/dss-network-plugin.qm

%files -n lib%repo%sover
%_libdir/libdde-network-core.so.%{sover}*

%files -n lib%repo-devel
%dir %_includedir/libddenetworkcore/
%_includedir/libddenetworkcore/*.h
%_pkgconfigdir/dde-network-core.pc
%_libdir/libdde-network-core.so

%changelog
* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 2.0.26-alt1
- New version 2.0.26.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 21 2024 Leontiy Volodin <lvol@altlinux.org> 2.0.22-alt1
- New version 2.0.22.

* Thu Jan 25 2024 Leontiy Volodin <lvol@altlinux.org> 2.0.20-alt1
- New version 2.0.20.
- Updated license tag.

* Wed Oct 25 2023 Leontiy Volodin <lvol@altlinux.org> 2.0.16-alt1
- New version 2.0.16.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.9-alt1
- New version.

* Tue Nov 15 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.71-alt1
- New version.
- Fixed FTBFS.

* Fri Aug 26 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.61-alt1
- Initial build for ALT Sisyphus.
