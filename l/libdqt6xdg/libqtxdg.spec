# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 4

Name: libdqt6xdg
Version: 4.4.0
Release: alt0.dde.1

Summary: Qt implementation of freedesktop.org xdg specs
License: LGPL-2.1
Group: System/Libraries

Url: https://github.com/lxqt/libqtxdg
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: dqt6-base-devel dqt6-svg-devel libmagic-devel
BuildRequires: libdqt6-xml
BuildRequires: dqt6-lxqt2-build-tools
BuildRequires: libgio-devel
Requires: libdqt6-core = %_dqt6_version

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
%summary.

%package devel
Summary: Development headers for QtXdg library
Group: Development/C++
Requires: %name = %EVR
Requires: libgio-devel

%description devel
This package provides the development files for qtxdg library
which implements functions of the XDG Specifications in Qt.

%prep
%setup
%autopatch -p1
%ifarch %e2k
sed -i 's,-flto -fuse-linker-plugin,,' cmake/compiler_settings.cmake
%endif

%build
export CMAKE_PREFIX_PATH=%_dqt6_libdir/cmake:%_dqt6_datadir/cmake:$CMAKE_PREFIX_PATH
%DQ6cmake \
  -DQTXDG_DEFAPPS_CONF_INSTALL_DIR=%_dqt6_sysconfdir \
  -DCMAKE_INSTALL_INCLUDEDIR=%_dqt6_headerdir \
  -DCMAKE_INSTALL_DATAROOTDIR=%_dqt6_datadir \
  -DCMAKE_INSTALL_LIBDIR=%_dqt6_libdir \
#
%DQ6make

%install
%DQ6install

%files
%_dqt6_libdir/libQt6Xdg*.so.%sover
%_dqt6_libdir/libQt6Xdg*.so.%sover.*
%_dqt6_plugindir/iconengines/libQt6XdgIconPlugin.so
%config %_dqt6_sysconfdir/lxqt-qtxdg.conf
%config %_dqt6_sysconfdir/qtxdg.conf

%files devel
%_dqt6_libdir/libQt6Xdg*.so
%_dqt6_headerdir/qt6xdg*/
%_dqt6_libdir/pkgconfig/Qt6Xdg*.pc
%_dqt6_datadir/cmake/qt6xdg*/

%changelog
* Thu Sep 17 2026 Leontiy Volodin <lvol@altlinux.org> 4.4.0-alt0.dde.1
- Forked for independent deepin buildings (for deepin-qt6integration).

* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 4.4.0-alt1
- New version 4.4.0.

* Sun Feb 08 2026 Anton Midyukov <antohami@altlinux.org> 4.3.0-alt2
- Add upstream fix:
  + Fix FTBFS dev utils with Qt >= 6.10.

* Wed Nov 05 2025 Anton Midyukov <antohami@altlinux.org> 4.3.0-alt1
- New version 4.3.0.

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 4.2.0-alt1
- New version 4.2.0.

* Tue Nov 05 2024 Anton Midyukov <antohami@altlinux.org> 4.1.0-alt1
- new version 4.1.0

* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- Initial build
