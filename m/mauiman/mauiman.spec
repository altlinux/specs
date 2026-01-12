%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauiman
Version: 4.0.2
Release: alt1

Summary: Maui Manager Library. Server and Library
License: LGPL-3.0-only
Group: Graphical desktop/KDE
Url: https://invent.kde.org/maui/mauiman

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)

%description
%summary.

%package devel
Summary: Development files for MauiMan
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description devel
%summary. Development files for MauiMan.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_bindir/MauiManServer4
%_libdir/libMauiMan4.so.4
%_libdir/libMauiMan4.so.4.0.2
%_datadir/dbus-1/services/org.mauiman.Manager4.service

%files devel
%dir %_includedir/MauiMan4
%_includedir/MauiMan4/accessibilitymanager.h
%_includedir/MauiMan4/backgroundmanager.h
%_includedir/MauiMan4/formfactormanager.h
%_includedir/MauiMan4/inputdevicesmanager.h
%_includedir/MauiMan4/mauiman_export.h
%_includedir/MauiMan4/mauimanutils.h
%_includedir/MauiMan4/screenmanager.h
%_includedir/MauiMan4/settingsstore.h
%_includedir/MauiMan4/thememanager.h
%dir %_libdir/cmake/MauiMan4
%_libdir/cmake/MauiMan4/MauiMan4Config.cmake
%_libdir/cmake/MauiMan4/MauiMan4ConfigVersion.cmake
%_libdir/cmake/MauiMan4/MauiMan4Targets-noconfig.cmake
%_libdir/cmake/MauiMan4/MauiMan4Targets.cmake
%_libdir/libMauiMan4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
