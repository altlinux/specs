%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$
%define name6 gsettings-dqt6
%define name5 gsettings-dqt5
%define name0 gsettings-qt
%define sover 1

%def_disable clang

Name: deepin-gsettings-qt
Version: 1.1.1
Release: alt1
Summary: Qt/QML bindings for GSettings
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/gsettings-qt
VCS: https://gitlab.com/ubports/development/core/gsettings-qt
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: libgio-devel ayatana-cmake-modules
BuildRequires: dqt6-declarative-devel libdqt6-qml libdqt6-widgets libdqt6-test libdqt6-quick libdqt6-quicktest
BuildRequires: dqt5-declarative-devel libdqt5-qml libdqt5-widgets libdqt5-test libdqt5-quicktest

# find libraries
%add_findprov_lib_path %_dqt6_libdir %_dqt5_libdir

%description
Qt/QML bindings for GSettings.

%package -n lib%{name6}_%sover
Summary: Qt/QML bindings for GSettings
Group: System/Libraries
Provides: lib%name6 = %EVR
Obsoletes: lib%name6 < %EVR

%description -n lib%{name6}_%sover
Libraries for %name6.

%package -n lib%name6-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: %name6-devel = %EVR
Obsoletes: %name6-devel < %EVR

%description -n lib%name6-devel
Header files and libraries for %name6.

%package -n lib%{name5}_%sover
Summary: Qt/QML bindings for GSettings
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%{name5}_%sover
Libraries for %name.

%package -n lib%name5-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name5-devel
Header files and libraries for %name.

%prep
%setup
%autopatch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif

%DQ6build \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DENABLE_QT6=ON \
 -DENABLE_WERROR=OFF \
 -DCMAKE_INSTALL_LIBDIR=%_lib/dqt6/lib \
 -DLIB_DESTINATION=%_lib \
#

export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake -B build5 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DCMAKE_SKIP_RPATH=NO \
 -DCMAKE_SKIP_INSTALL_RPATH=NO \
 -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
 -DENABLE_QT6=OFF \
 -DENABLE_WERROR=ON \
 -DCMAKE_INSTALL_LIBDIR=%_lib/dqt5/lib \
 -DLIB_DESTINATION=%_lib \
#
cmake --build "build5" -j%__nprocs

%install
export DESTDIR=%buildroot

%DQ6install
mkdir -p %buildroot%_dqt6_qmldir/GSettings/
mv -f %buildroot%_dqt6_libdir/qt6/qml/GSettings/* %buildroot%_dqt6_qmldir/GSettings/

cmake --install "build5" --verbose
mkdir -p %buildroot%_dqt5_qmldir/GSettings/
mv -f %buildroot%_dqt5_libdir/qt5/qml/GSettings/* %buildroot%_dqt5_qmldir/GSettings/

%files -n lib%{name6}_%sover
%doc COPYING
%_dqt6_libdir/lib%{name0}6.so.%{sover}*
%dir %_dqt6_qmldir/GSettings/
%_dqt6_qmldir/GSettings/libGSettingsQmlPlugin.so
%_dqt6_qmldir/GSettings/plugins.qmltypes
%_dqt6_qmldir/GSettings/qmldir

%files -n lib%name6-devel
%dir %_dqt6_headerdir/QGSettings/
%_dqt6_headerdir/QGSettings/*
%_dqt6_libdir/pkgconfig/%{name0}6.pc
%_dqt6_libdir/lib%{name0}6.so

%files -n lib%{name5}_%sover
%doc COPYING
%_dqt5_libdir/lib%{name0}.so.%{sover}*
%dir %_dqt5_qmldir/GSettings/
%_dqt5_qmldir/GSettings/libGSettingsQmlPlugin.so
%_dqt5_qmldir/GSettings/plugins.qmltypes
%_dqt5_qmldir/GSettings/qmldir

%files -n lib%name5-devel
%dir %_dqt5_headerdir/QGSettings/
%_dqt5_headerdir/QGSettings/*
%_dqt5_libdir/pkgconfig/%{name0}.pc
%_dqt5_libdir/lib%{name0}.so

%changelog
* Thu Mar 12 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Sun Feb 15 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt0.dde.1
- New version 1.1.0.
- Built on dqt5 and dqt6.

* Thu Oct 03 2024 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1.dde.2.gitd5e002d
- Renamed subpackages:
  + deepin-gsettings-qt-libgsettings-qt -> libgsettings-dqt5-1.
  + deepin-gsettings-qt-devel -> libgsettings-dqt5-devel.

* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1.dde.1.gitd5e002d
- Forked qt modules for separate deepin buildings (ALT #48138).

* Thu Dec 01 2022 Leontiy Volodin <lvol@altlinux.org> 0.2-alt2.gitd5e002d
- Built from commit d5e002d7e0bce46c315bcc99a44a8bd51f49f488.
- Updated url tag.

* Fri Aug 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for spec).
