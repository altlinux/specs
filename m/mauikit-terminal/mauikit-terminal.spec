%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-terminal
Version: 4.0.2
Release: alt1

Summary: Terminal support components for Maui applications
License: LGPL-2.0-or-later
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-terminal

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: libmauikit-devel
BuildRequires: kf6-kpty-devel
BuildRequires: pkgconfig(Qt6Core5Compat)

Requires: libmauikit
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

%find_lang mauikitterminal

%files -f mauikitterminal.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/terminal
%_libdir/qt6/qml/org/mauikit/terminal/*.*
%dir %_libdir/qt6/qml/org/mauikit/terminal/color-schemes
%_libdir/qt6/qml/org/mauikit/terminal/color-schemes/*.*
%dir %_libdir/qt6/qml/org/mauikit/terminal/color-schemes/historic
%_libdir/qt6/qml/org/mauikit/terminal/color-schemes/historic/*.*
%dir %_libdir/qt6/qml/org/mauikit/terminal/kb-layouts
%_libdir/qt6/qml/org/mauikit/terminal/kb-layouts/*
%dir %_libdir/qt6/qml/org/mauikit/terminal/private
%_libdir/qt6/qml/org/mauikit/terminal/private/*.qml
%_libdir/qt6/qml/org/mauikit/terminal/qmldir

%files -n lib%{name}
%_libdir/libMauiKitTerminal4.so.4
%_libdir/libMauiKitTerminal4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/Terminal
%_includedir/MauiKit4/Terminal/moduleinfo.h
%_includedir/MauiKit4/Terminal/terminal_export.h
%_includedir/MauiKit4/Terminal/terminal_version.h
%dir %_libdir/cmake/MauiKitTerminal4
%_libdir/cmake/MauiKitTerminal4/MauiKitTerminal4Config.cmake
%_libdir/cmake/MauiKitTerminal4/MauiKitTerminal4ConfigVersion.cmake
%_libdir/cmake/MauiKitTerminal4/MauiKitTerminal4Targets-noconfig.cmake
%_libdir/cmake/MauiKitTerminal4/MauiKitTerminal4Targets.cmake
%_libdir/libMauiKitTerminal4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
