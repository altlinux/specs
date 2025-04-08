%def_without clang

%define repo dde-network-core6
%define sover 2
%define _cmake__builddir BUILD

Name: deepin-network-core
Version: 2.0.52
Release: alt1
Summary: Deepin desktop-environment - network core files
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-network-core
Vcs: git://github.com/linuxdeepin/dde-network-core.git

Source: %url/archive/%version/dde-network-core-%version.tar.gz
Patch1: deepin-network-core-2.0.20-alt-GNUInstallDirs.patch

# deepin-control-center
ExcludeArch: i586

BuildPreReq: rpm-build-ninja rpm-build-kf6 rpm-macros-dqt6 patchelf
%if_with clang
BuildPreReq: clang-devel
%else
BuildPreReq: gcc-c++
%endif
# Automatically added by buildreq on Fri Apr 04 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-tools gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdde-control-center6 libdouble-conversion3 libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libgio-devel libglvnd-devel libgpg-error libnm-devel libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers
BuildRequires: deepin-session-shell-devel dqt6-declarative-devel dqt6-tools-devel dtk6-common-devel kf6-networkmanager-qt-devel libcups-devel libdde-control-center-devel libdtk6widget-devel libgtest-devel libudev-devel

%description
Deepin desktop-environment - network core files.

%package -n lib%{repo}_%sover
Summary: Library for %name
Group: System/Libraries

%description -n lib%{repo}_%sover
This package provides library for %name.

%package -n lib%repo-devel
Summary: Development package for %name
Group: Development/C++
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%repo-devel
This package provides development files for %name.

%prep
%setup -n dde-network-core-%version
%autopatch -p1

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export CPLUS_INCLUDE_PATH=%_includedir/glib-2.0:%_libdir/glib-2.0/include:%_includedir/libnm:$CPLUS_INCLUDE_PATH
%DQ6build \
  -DLIB_DESTINATION=%_lib \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DCMAKE_EXE_LINKER_FLAGS:STRING='-L%_K6lib -L%_K6link' \
  -DCMAKE_MODULE_LINKER_FLAGS:STRING='-L%_K6lib -L%_K6link' \
  -DCMAKE_SHARED_LINKER_FLAGS:STRING='-L%_K6lib -L%_K6link' \
  -DCMAKE_LIBRARY_PATH='%_K6link;%_K6lib;/%_lib' \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%DQ6install
mkdir -p %buildroot%_libdir/dde-control-center/plugins_v1.0/network/
mv -f %buildroot%_prefix/%_libdir/dde-control-center/plugins_v1.0/network/* \
      %buildroot%_libdir/dde-control-center/plugins_v1.0/network/
# cleanup broken rpaths in elfs
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/network/network.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/network/network.so --add-needed libQt6Qml.so.6
# package translations
%find_lang --with-qt --output=%name.lang dde-control-center dss-network-plugin dde-network-core deepin-service-manager

%files -f %name.lang
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/plugins_v1.0/
%_libdir/dde-control-center/plugins_v1.0/network/
%dir %_libdir/dde-session-shell/
%dir %_libdir/dde-session-shell/modules/
%_libdir/dde-session-shell/modules/libdss-network-plugin.so
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libnetwork-service.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/system/
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/system/plugin-system-network.json
%_datadir/deepin-service-manager/user/plugin-session-network.json
%_datadir/dbus-1/system.d/org.deepin.service.SessionNetwork.conf
%_datadir/dbus-1/system.d/org.deepin.service.SystemNetwork.conf
%_datadir/polkit-1/rules.d/50-dss-network-plugin.rules
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.network/
%_datadir/dsg/configs/org.deepin.dde.network/org.deepin.dde.network.json
# package translations outside %%find_lang
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%dir %_datadir/dde-control-center/translations/v1.0/
%dir %_datadir/dde-network-core/
%dir %_datadir/dde-network-core/translations/
%_datadir/dde-network-core/translations/dde-network-core.qm
%_datadir/dde-network-core/translations/dde-network-core_es_419.qm
%_datadir/dde-network-core/translations/dde-network-core_ky@Arab.qm
%dir %_datadir/dss-network-plugin/
%dir %_datadir/dss-network-plugin/translations/
%_datadir/dss-network-plugin/translations/dss-network-plugin.qm
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/network-service/
%dir %_datadir/deepin-service-manager/network-service/translations/
%_datadir/deepin-service-manager/network-service/translations/network-service-plugin.qm
%_datadir/deepin-service-manager/network-service/translations/network-service-plugin_ky@Arab.qm

%files -n lib%{repo}_%sover
%_libdir/lib%repo.so.%{sover}*

%files -n lib%repo-devel
%dir %_includedir/libddenetworkcore/
%_includedir/libddenetworkcore/*.h
%_pkgconfigdir/dde-network-core.pc
%_libdir/lib%repo.so

%changelog
* Fri Apr 04 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.52-alt1
- New version 2.0.52.
- Added vcs tag.
- Switched to dqt6.

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
