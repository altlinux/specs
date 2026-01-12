%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit
Version: 4.0.2
Release: alt1

Summary: Toolkit for Multi Adaptable User Interfaces
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://mauikit.org
Vcs: https://invent.kde.org/maui/mauikit

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: mauiman-devel
BuildRequires: /usr/bin/appstreamcli
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: pkgconfig(xcb-icccm)

Requires: kf6-kirigami
Requires: kf6-purpose
Requires: libqt6-qmlcore
Requires: libqt6-multimediaquick
Requires: libqt6-qml
Requires: libqt6-qmlmodels
Requires: libqt6-quickcontrols2
Requires: libqt6-quickdialogs2
Requires: libqt6-quickeffects
Requires: libqt6-quicklayouts
Requires: libqt6-quickshapes
Requires: libqt6-quicktemplates2

Requires: plasma6-breeze
Requires: icon-theme-breeze

%description
%summary.

%package -n lib%{name}
Summary: Library files for MauiKit
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}
%summary. Library files for MauiKit.

%package -n lib%{name}-devel
Summary: Development files for MauiKit
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary. Development files for MauiKit.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit
%dir %_libdir/qt6/qml/org/mauikit/controls
%_libdir/qt6/qml/org/mauikit/controls/*
%dir %_libdir/qt6/qml/org/mauikit/style/
%_libdir/qt6/qml/org/mauikit/style/*
%dir %_datadir/org.mauikit.controls
%dir %_datadir/org.mauikit.controls/csd.6
%_datadir/org.mauikit.controls/csd.6/mauiproject.conf
%dir %_datadir/org.mauikit.controls/csd.6/Android
%_datadir/org.mauikit.controls/csd.6/Android/config.conf
%dir %_datadir/org.mauikit.controls/csd.6/Arena
%_datadir/org.mauikit.controls/csd.6/Arena/*
%dir %_datadir/org.mauikit.controls/csd.6/Breeze
%_datadir/org.mauikit.controls/csd.6/Breeze/*
%dir %_datadir/org.mauikit.controls/csd.6/Cadium
%_datadir/org.mauikit.controls/csd.6/Cadium/*
%dir %_datadir/org.mauikit.controls/csd.6/CadiumGloss
%_datadir/org.mauikit.controls/csd.6/CadiumGloss/*
%dir %_datadir/org.mauikit.controls/csd.6/Default
%_datadir/org.mauikit.controls/csd.6/Default/*
%dir %_datadir/org.mauikit.controls/csd.6/Gnome
%_datadir/org.mauikit.controls/csd.6/Gnome/config.conf
%dir %_datadir/org.mauikit.controls/csd.6/Lucid
%_datadir/org.mauikit.controls/csd.6/Lucid/*
%dir %_datadir/org.mauikit.controls/csd.6/Nitrux
%_datadir/org.mauikit.controls/csd.6/Nitrux/*
%dir %_datadir/org.mauikit.controls/csd.6/OSX
%_datadir/org.mauikit.controls/csd.6/OSX/*
%dir %_datadir/org.mauikit.controls/csd.6/Plastico
%_datadir/org.mauikit.controls/csd.6/Plastico/*
%dir %_datadir/org.mauikit.controls/csd.6/Windows
%_datadir/org.mauikit.controls/csd.6/Windows/config.conf


%files -n lib%{name}
%_libdir/libMauiKit4.so.4
%_libdir/libMauiKit4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4
%dir %_includedir/MauiKit4/Core
%_includedir/MauiKit4/Core/*.h
%dir %_libdir/cmake/MauiKit4
%_libdir/cmake/MauiKit4/MauiKit4*.cmake
%_libdir/libMauiKit4.so


%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
