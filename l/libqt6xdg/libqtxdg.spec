# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 4

Name: libqt6xdg
Version: 4.4.0
Release: alt1

Summary: Qt implementation of freedesktop.org xdg specs
License: LGPL-2.1
Group: System/Libraries

Url: https://github.com/lxqt/libqtxdg
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt6-base-devel qt6-svg-devel libmagic-devel
BuildRequires: lxqt2-build-tools
BuildRequires: libgio-devel
Requires: libqt6-core = %_qt6_version

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
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/libQt6Xdg*.so.%sover
%_libdir/libQt6Xdg*.so.%sover.*
%_qt6_plugindir/iconengines/libQt6XdgIconPlugin.so
%config %_sysconfdir/xdg/lxqt-qtxdg.conf
%config %_sysconfdir/xdg/qtxdg.conf

%files devel
%_libdir/libQt6Xdg*.so
%_includedir/qt6xdg*/
%_pkgconfigdir/Qt6Xdg*.pc
%_datadir/cmake/qt6xdg*/

%changelog
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
