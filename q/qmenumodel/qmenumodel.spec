%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: qmenumodel
Version: 0.10.0
Release: alt1

Summary: Qt5 renderer for Ayatana Indicators
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/qmenumodel

Source: %name-%version.tar

# sync with version 0.9.2-1.1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)

%if_with check
BuildRequires: ctest
%endif

%description
Qt binding for GMenuModel that allows connecting to a menu model exposed
on D-Bus and presents it as a list model. It can be used to expose
indicator or application menus for applications using the Qt framework.

%package -n libqmenumodel1
Summary: Qt binding for GMenuModel - shared library
Group: System/Libraries

%description -n libqmenumodel1
Qt binding for GMenuModel that allows connecting to a menu model exposed
on D-Bus and presents it as a list model. It can be used to expose
indicator or  application menus for applications using the Qt framework.

This package contains the shared library required by applications using
QMenuModel.

%package -n libqmenumodel-devel
Summary: Qt binding for GMenuModel - development files
Group: Development/C
Requires: libqmenumodel1 = %{version}-%{release}

%description -n libqmenumodel-devel
Qt binding for GMenuModel that allows connecting to a menu model exposed
on D-Bus and presents it as a list model. It can be used to expose
indicator or application menus for applications using the Qt framework.

This package contains the development headers for libqmenumodel.

%package -n qml-module-qmenumodel1
Summary: Qt binding for GMenuModel - QML module
Group: System/Libraries
Requires: libqmenumodel1 = %{version}-%{release}

%description -n qml-module-qmenumodel1
Qt binding for GMenuModel that allows connecting to a menu model exposed
on D-Bus and presents it as a list model. It can be used to expose
indicator or application menus for applications using the Qt framework.

This package contains the QML module for building applications using the
QMenuModel library.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest -V

%files -n libqmenumodel1
%doc AUTHORS ChangeLog COPYING.LGPL NEWS README TODO
%_libdir/libqmenumodel.so.1
%_libdir/libqmenumodel.so.1.0.0

%files -n libqmenumodel-devel
%doc examples
%dir %_includedir/qt5/%name
%_includedir/qt5/%name/*
%_libdir/libqmenumodel.so
%_libdir/pkgconfig/*.pc

%files -n qml-module-qmenumodel1
%dir %_qt5_qmldir/QMenuModel.1
%_qt5_qmldir/QMenuModel.1/*

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus
