%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-filebrowsing
Version: 4.0.2
Release: alt1

Summary: MauiKit File Browsing utilities and controls
License: LGPL-2.1-or-later
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-filebrowsing

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: /usr/bin/appstreamcli
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: kf6-kio-devel

Requires: kf6-kio
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

%find_lang mauikitfilebrowsing

%files -f mauikitfilebrowsing.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/filebrowsing
%_libdir/qt6/qml/org/mauikit/filebrowsing/*.*
%_libdir/qt6/qml/org/mauikit/filebrowsing/qmldir
%dir %_libdir/qt6/qml/org/mauikit/filebrowsing/private
%_libdir/qt6/qml/org/mauikit/filebrowsing/private/*

%files -n lib%{name}
%_libdir/libMauiKitFileBrowsing4.so.4
%_libdir/libMauiKitFileBrowsing4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/FileBrowsing
%_includedir/MauiKit4/FileBrowsing/*
%dir %_libdir/cmake/MauiKitFileBrowsing4
%_libdir/cmake/MauiKitFileBrowsing4/MauiKitFileBrowsing4Config.cmake
%_libdir/cmake/MauiKitFileBrowsing4/MauiKitFileBrowsing4ConfigVersion.cmake
%_libdir/cmake/MauiKitFileBrowsing4/MauiKitFileBrowsing4Targets-noconfig.cmake
%_libdir/cmake/MauiKitFileBrowsing4/MauiKitFileBrowsing4Targets.cmake
%_libdir/libMauiKitFileBrowsing4.so


%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
