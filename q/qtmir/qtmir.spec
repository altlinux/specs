%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: qtmir
# NOTE: use .gear/tagit.sh to get a tag name
Version: 0.8.0_git20260226.fb30a11
Release: alt1

Summary: Qt platform abstraction (QPA) plugin for a Mir server
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/qtmir

Source: %name-%version.tar

# sync with version 0.8.0~git20260226.fb30a11-8 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(mirserver)
BuildRequires: pkgconfig(mircommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(liblomiri-content-hub)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: qt5-base-devel-static
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)

%if_with check
BuildRequires: ctest
%endif

# qt5/qml/Lomiri/Components/ListItems/qmldir qt5/qml/Lomiri/Components/Pickers/qmldir qt5/qml/Lomiri/Components/Popups/qmldir qt5/qml/Lomiri/Components/Styles/qmldir qt5/qml/Lomiri/Components/qmldir
Requires: lomiri-ui-toolkit

%description
QtMir is a set of Qt5 components to enable one to write a Mir server with
Qt. It contains a QPA (Qt Platform Abstraction) plugin which creates and
manages a Mir server. It also exposes some internal Mir functionality.

%package -n lib%{name}
Summary: QtMir server API shared library
Group: System/Libraries

%description -n lib%{name}
QtMir is a set of Qt5 components to enable one to write a Mir server with
Qt. It contains a QPA (Qt Platform Abstraction) plugin which creates and
manages a Mir server. It also exposes some internal Mir functionality.

Contains the shared library containing QtMir server API.

%package -n lib%{name}-devel
Summary: Developer files for QtMir server API
Group: System/Libraries
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
QtMir is a set of Qt5 components to enable one to write a Mir server with
Qt. It contains a QPA (Qt Platform Abstraction) plugin which creates and
manages a Mir server. It also exposes some internal Mir functionality.

This package contains the library headers for developers.

%package demo
Summary: QtMir demo files
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}

%description demo
QtMir is a set of Qt5 components to enable one to write a Mir server with
Qt. It contains a QPA (Qt Platform Abstraction) plugin which creates and
manages a Mir server. It also exposes some internal Mir functionality.

This package provides benchmark tests and a simple shell and client using
the QtMir QPA.

%prep
%setup
%patch -p1

%build
%cmake \
       -DWITH_CONTENTHUB=ON \
       -DWerror=OFF \
       -DWITH_MIR2=on \
%if_with check
       -DNO_TESTS=OFF \
%else
       -DNO_TESTS=ON \
%endif
       -DWITH_VALGRIND=OFF \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS COPYING COPYING.LESSER NEWS README
%_qt5_plugindir/platforms/libqpa-mirserver.so
%_qt5_qmldir/QtMir/Application/libqtmirapplicationplugin.so
%_qt5_qmldir/QtMir/Application/qmldir
%_desktopdir/xwayland.qtmir.desktop
%_datadir/glib-2.0/schemas/com.canonical.qtmir.gschema.xml
%_iconsdir/hicolor/512x512/apps/xwayland.qtmir.png

%files -n lib%{name}
%_libdir/libqtmirserver.so.2*

%files -n lib%{name}-devel
%_libdir/libqtmirserver.so
%dir %_includedir/qtmir
%dir %_includedir/qtmir/qtmir
%_includedir/qtmir/qtmir/displayconfigurationpolicy.h
%_includedir/qtmir/qtmir/displayconfigurationstorage.h
%_includedir/qtmir/qtmir/mirserverapplication.h
%_includedir/qtmir/qtmir/qtmir.h
%_includedir/qtmir/qtmir/screen.h
%_includedir/qtmir/qtmir/screens.h
%_includedir/qtmir/qtmir/sessionauthorizer.h
%_includedir/qtmir/qtmir/types.h
%_includedir/qtmir/qtmir/windowmanagementpolicy.h
%_pkgconfigdir/qtmirserver.pc

%files demo
%_bindir/qtmir-demo-client
%_bindir/qtmir-demo-shell
%_datadir/applications/qtmir-demo-client.desktop
%dir %_datadir/qtmir/qtmir-demo-client
%_datadir/qtmir/qtmir-demo-client/*
%dir %_datadir/qtmir/qtmir-demo-shell
%_datadir/qtmir/qtmir-demo-shell/*

%changelog
* Sun Jun 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.0_git20260226.fb30a11-alt1
- Updated to allow build with mir 2.28.0.

* Wed Jul 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.8.0_git20250626.c74a08da-alt1
- Initial build for Sisyphus
