%def_without clang

%define sover 0

Name: deepin-service-manager
Version: 1.0.14
Release: alt1

Summary: Manage DBus service on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-service-manager
Vcs: git://github.com/linuxdeepin/deepin-service-manager.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: cmake dqt6-base-devel dqt6-tools-devel libsystemd-devel dtk6-common-devel libdtk6core-devel
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
%autopatch -p1
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
%DQ6build \
  -DCMAKE_PROJECT_HOMEPAGE_URL=%url \
  -DPROJECT_VERSION=%version \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
#

%install
%DQ6install
# Fix library naming.
#mv -f %%buildroot%%_libdir/libdeepin-qdbus-service.so %%buildroot%%_libdir/libdeepin-qdbus-service.so.%%sover
#ln -s %%_libdir/libdeepin-qdbus-service.so.%%sover %%buildroot%%_libdir/libdeepin-qdbus-service.so
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_sysconfdir/xdg/autostart/oom-score-adjust.desktop
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libOOMScoreAdjust.so
%_unitdir/deepin-service*.service
%_unitdir/multi-user.target.wants/deepin-service-manager.service
%_userunitdir/deepin-service*.service
%_userunitdir/default.target.wants/deepin-service-manager.service
%_datadir/dbus-1/system.d/org.deepin.ServiceManager1.conf
%_datadir/dbus-1/system.d/org.deepin.service.OOMScoreAdjust.conf
%_datadir/dbus-1/system-services/org.deepin.OOMScoreAdjust.service
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/other/
%_datadir/deepin-service-manager/other/manager.json
%dir %_datadir/deepin-service-manager/system/
%_datadir/deepin-service-manager/system/OOM-Score-Adjust.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.service.manager/
%_datadir/dsg/configs/org.deepin.service.manager/org.deepin.service.manager.oom-score-adjust.json

%files -n libdeepin-qdbus-service%sover
#%%_libdir/libdeepin-qdbus-service.so.%%{sover}*
%_libdir/libdeepin-qdbus-service.so

%files -n libdeepin-qdbus-service-devel
%dir %_includedir/deepin-qdbus-service/
%_includedir/deepin-qdbus-service/qdbusservice.h
%dir %_libdir/cmake/deepin-qdbus-service/
%_libdir/cmake/deepin-qdbus-service/deepin-qdbus-serviceConfig.cmake
#%%_libdir/libdeepin-qdbus-service.so
%_pkgconfigdir/deepin-qdbus-service.pc

%changelog
* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.14-alt1
- New version 1.0.14.

* Mon Apr 21 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- New version 1.0.11.
- Switched to dqt6.

* Mon Dec 23 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- New version 1.0.8.
- Added vcs tag.

* Thu Oct 31 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.4-alt1
- New version 1.0.4.
- Fixed build with gcc14.

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.3.0.36.ge15b893-alt1
- New version 1.0.3-36-ge15b893.
- Built via separate qt5 instead system (ALT #48138).

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt2.gitd16282e
- Applied usrmerge.

* Tue Nov 28 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1.gitd16282e
- Initial build for ALT Sisyphus.
