%define _name qtgraphs
%define __name QtGraphs
%define ___name Qt6Graphs
%define ver_major 6.10
%define libname lib%___name

%def_enable docs
%def_enable check

Name: %_name-qt6
Version: %ver_major.2
Release: alt1.1

Summary: Qt Graphs library for data visualization
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://github.com/qt/qtgraphs

Vcs: https://github.com/qt/qtgraphs.git

Source: %url/archive/v%version/%_name-v%version.tar.gz

%define qt_ver %version

BuildRequires(pre): rpm-macros-cmake rpm-macros-qt6
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(Qt6Core) >= %qt_ver
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6QuickTest)
BuildRequires: pkgconfig(Qt6QuickWidgets)
BuildRequires: pkgconfig(Qt6Test)
# https://bugzilla.altlinux.org/56799
BuildRequires: pkgconfig(Qt6Quick3D) qt6-quick3d
BuildRequires: pkgconfig(Qt6PrintSupport)
%{?_enable_check:BuildRequires: ctest}

%description
%{summary}.

%package -n lib%name
Summary: %summary
Group: Development/KDE and QT
Requires: qt6-quick3d

%description -n lib%name
%{summary}.
This package provides shared %__name library.

%package -n lib%name-devel
Summary: Qt Graphs development package
Group: Development/KDE and QT
Requires: lib%name = %EVR

%description -n lib%name-devel
%{summary}.
This package contains files needed for development with %__name

%package examples
Summary: Qt Graphs examples
Group: Development/KDE and QT
Requires: lib%name = %EVR

%description examples
%{summary}.
This package provudes Qt Graphs examples.


%prep
%setup -n %_name-%version

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files -n lib%name
%_libdir/%libname.so.*
%_libdir/%{libname}Widgets.so.*
%_qt6_qmldir/%__name/
%_libdir/qt6/sbom/%_name-%version.spdx
#%_libdir/qt6/sbom/%_name-%version.cdx.json

%files -n lib%name-devel
%_qt6_headerdir/%__name/
%_qt6_headerdir/%{__name}Widgets/
%_libdir/%{libname}*.so
%_libdir/*.prl
%_pkgconfigdir/%___name.pc
%_pkgconfigdir/%{___name}Widgets.pc
%_qt6_mkspecsdir/modules/*.pri
%_libdir/qt6/metatypes/*.json
%_libdir/qt6/modules/*.json
%_libdir/cmake/%___name/
%_libdir/cmake/%{___name}Widgets/
%_libdir/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%_libdir/cmake/%{___name}Private/
%_libdir/cmake/%{___name}WidgetsPrivate/
%_libdir/cmake/Qt6Qml/QmlPlugins/*.cmake

%files examples
%_libdir/qt6/examples/*

%changelog
* Mon Apr 06 2026 Yuri N. Sedunov <aris@altlinux.org> 6.10.2-alt1.1
- fixed %%files after qt6-base-6.10.2-alt2

* Fri Feb 13 2026 Yuri N. Sedunov <aris@altlinux.org> 6.10.2-alt1
- 6.10.2

* Sun Jan 18 2026 Yuri N. Sedunov <aris@altlinux.org> 6.10.1-alt1
- 6.10.1

* Wed Nov 12 2025 Yuri N. Sedunov <aris@altlinux.org> 6.9.3-alt1
- 6.9.3
- new -examples subpackage

* Mon Nov 10 2025 Yuri N. Sedunov <aris@altlinux.org> 6.9.2-alt1
- first build for Sisyphus


