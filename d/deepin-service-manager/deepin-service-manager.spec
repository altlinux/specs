%def_without clang

%define sover 0

Name: deepin-service-manager
Version: 1.0.3
Release: alt2.gitd16282e

Summary: Manage DBus service on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-service-manager

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake qt5-base-devel qt5-tools-devel libsystemd-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n libdeepin-qdbus-service%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdeepin-qdbus-service%sover
This package provides deepin-qdbus-service library for %name.

%package -n libdeepin-qdbus-service-devel
Summary: Development files for deepin-qdbus-service
Group: Development/Other

%description -n libdeepin-qdbus-service-devel
This package provides development files for deepin-qdbus-service.

%prep
%setup
sed -i 's|${CMAKE_INSTALL_PREFIX}/lib/systemd/system/|%_unitdir/|' \
  misc/CMakeLists.txt
# Fix pkg-config.
sed -i 's|Version: @PROJECT_VERSION@|Version: %version|' \
  misc/deepin-qdbus-service.pc.in

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_PROJECT_HOMEPAGE_URL=%url \
  -DPROJECT_VERSION=%version \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
# Fix library naming.
#mv -f %%buildroot%%_libdir/libdeepin-qdbus-service.so %%buildroot%%_libdir/libdeepin-qdbus-service.so.%%sover
#ln -s %%_libdir/libdeepin-qdbus-service.so.%%sover %%buildroot%%_libdir/libdeepin-qdbus-service.so
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_bindir/getfromqm
%dir %_libexecdir/deepin-daemon/
%dir %_libexecdir/deepin-daemon/service-trigger/
%_libexecdir/deepin-daemon/service-trigger/earlyoom.service.json
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libplugin-oom.so
%_unitdir/deepin-service*.service
%_unitdir/multi-user.target.wants/deepin-service-manager.service
%_userunitdir/deepin-service*.service
%_userunitdir/default.target.wants/deepin-service-manager.service
%_datadir/dbus-1/system.d/org.deepin.ServiceManager1.conf
%_datadir/dbus-1/system.d/org.deepin.oom1.conf
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/other/
%_datadir/deepin-service-manager/other/manager.json
%dir %_datadir/deepin-service-manager/system/
%_datadir/deepin-service-manager/system/plugin-oom.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.oom/
%_datadir/dsg/configs/org.deepin.oom/org.deepin.oom.json
# additional translations
%dir %_datadir/deepin-service-manager/oom/
%dir %_datadir/deepin-service-manager/oom/translations/
%_datadir/deepin-service-manager/oom/translations/plugin-oom_ky@Arab.qm

%files -n libdeepin-qdbus-service%sover
#%%_libdir/libdeepin-qdbus-service.so.%%{sover}*
%_libdir/libdeepin-qdbus-service.so

%files -n libdeepin-qdbus-service-devel
%dir %_includedir/deepin-qdbus-service/
%_includedir/deepin-qdbus-service/qdbusservice.h
%_libdir/cmake/deepin-qdbus-service/deepin-qdbus-serviceConfig.cmake
#%%_libdir/libdeepin-qdbus-service.so
%_pkgconfigdir/deepin-qdbus-service.pc

%changelog
* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt2.gitd16282e
- Applied usrmerge.

* Tue Nov 28 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1.gitd16282e
- Initial build for ALT Sisyphus.
