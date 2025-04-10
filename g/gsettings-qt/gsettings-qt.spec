%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$
%define name6 gsettings-qt6
%define sover 1

%def_disable clang

Name: gsettings-qt
Version: 1.0.0
Release: alt1
Summary: Qt/QML bindings for GSettings
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/gsettings-qt
Vcs: https://gitlab.com/ubports/development/core/gsettings-qt.git
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %name-%version.tar.gz
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: libgio-devel ayatana-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: qt5-declarative-devel

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

%package -n lib%name%sover
Summary: Qt/QML bindings for GSettings
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%name%sover
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
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

export PATH=%_qt6_bindir:$PATH
export LC_ALL=C.UTF-8
%cmake -B build6 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DENABLE_QT6=ON \
 -DENABLE_WERROR=OFF \
#
cmake --build "build6" -j%__nprocs

export PATH=%_qt5_bindir:$PATH
%cmake -B build5 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DENABLE_QT6=OFF \
 -DENABLE_WERROR=ON \
#
cmake --build "build5" -j%__nprocs

%install
export DESTDIR=%buildroot
cmake --install "build6" --verbose
mkdir -p %buildroot%_qt6_qmldir/GSettings/
mv -f %buildroot%_qt5_qmldir/GSettings/* %buildroot%_qt6_qmldir/GSettings/
cmake --install "build5" --verbose

%files -n lib%{name6}_%sover
%doc COPYING
%_libdir/lib%name6.so.%{sover}*
%dir %_qt6_qmldir/GSettings/
%_qt6_qmldir/GSettings/libGSettingsQmlPlugin.so
%_qt6_qmldir/GSettings/plugins.qmltypes
%_qt6_qmldir/GSettings/qmldir

%files -n lib%name6-devel
%dir %_qt6_headerdir/QGSettings/
%_qt6_headerdir/QGSettings/*
%_pkgconfigdir/%name6.pc
%_libdir/lib%name6.so

%files -n lib%name%sover
%doc COPYING
%_libdir/lib%name.so.%{sover}*
%dir %_qt5_qmldir/GSettings/
%_qt5_qmldir/GSettings/libGSettingsQmlPlugin.so
%_qt5_qmldir/GSettings/plugins.qmltypes
%_qt5_qmldir/GSettings/qmldir

%files -n lib%name-devel
%dir %_qt5_headerdir/QGSettings/
%_qt5_headerdir/QGSettings/*
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Thu Apr 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- New version 1.1.0.
- Added vcs tag.

* Thu Oct 03 2024 Leontiy Volodin <lvol@altlinux.org> 0.2-alt3.gitd5e002d
- Renamed subpackages:
  + libgsettings-qt -> libgsettings-qt1.
  + gsettings-qt-devel -> libgsettings-qt-devel.

* Thu Dec 01 2022 Leontiy Volodin <lvol@altlinux.org> 0.2-alt2.gitd5e002d
- Built from commit d5e002d7e0bce46c315bcc99a44a8bd51f49f488.
- Updated url tag.

* Fri Aug 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for spec).
