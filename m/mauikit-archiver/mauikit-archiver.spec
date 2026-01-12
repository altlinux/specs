%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-archiver
Version: 4.0.2
Release: alt1

Summary: QtQuick plugin for online archived/compressed files management
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-archiver

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quicklayouts

%description
%summary.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}
%summary. Library files for %name.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary. Development files for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang mauikitarchiver

%files -f mauikitarchiver.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/archiver
%_libdir/qt6/qml/org/mauikit/archiver/*

%files -n lib%{name}
%_libdir/libMauiKitArchiver4.so.4
%_libdir/libMauiKitArchiver4.so.4.0.2

%files -n lib%{name}-devel
%_includedir/MauiKit4/Accounts/archiver_version.h
%dir %_includedir/MauiKit4/Archiver
%_includedir/MauiKit4/Archiver/archiver_export.h
%_includedir/MauiKit4/Archiver/moduleinfo.h
%_libdir/cmake/MauiKitArchiver4/MauiKitArchiver4Config.cmake
%_libdir/cmake/MauiKitArchiver4/MauiKitArchiver4ConfigVersion.cmake
%_libdir/cmake/MauiKitArchiver4/MauiKitArchiver4Targets-noconfig.cmake
%_libdir/cmake/MauiKitArchiver4/MauiKitArchiver4Targets.cmake
%_libdir/libMauiKitArchiver4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
