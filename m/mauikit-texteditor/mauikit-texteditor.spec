%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-texteditor
Version: 4.0.2
Release: alt1

Summary: MauiKit Text Editor components
License: LGPL-2.1-or-later
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-texteditor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel

Requires: libkf6sonnetui
Requires: libmauikit
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quicklayouts

%description
%summary.

MauiKitTextEditor is a set of QtQuick components providing
basic text editing capabilities.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}
%summary.

MauiKitTextEditor is a set of QtQuick components providing
basic text editing capabilities.

Library files for %name.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary.

MauiKitTextEditor is a set of QtQuick components providing
basic text editing capabilities.

Development files for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang mauikittexteditor

%files -f mauikittexteditor.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/texteditor
%_libdir/qt6/qml/org/mauikit/texteditor/*

%files -n lib%{name}
%_libdir/libMauiKitTextEditor4.so.4
%_libdir/libMauiKitTextEditor4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/TextEditor
%_includedir/MauiKit4/TextEditor/moduleinfo.h
%_includedir/MauiKit4/TextEditor/texteditor_export.h
%_includedir/MauiKit4/TextEditor/texteditor_version.h
%dir %_libdir/cmake/MauiKitTextEditor4
%_libdir/cmake/MauiKitTextEditor4/MauiKitTextEditor4Config.cmake
%_libdir/cmake/MauiKitTextEditor4/MauiKitTextEditor4ConfigVersion.cmake
%_libdir/cmake/MauiKitTextEditor4/MauiKitTextEditor4Targets-noconfig.cmake
%_libdir/cmake/MauiKitTextEditor4/MauiKitTextEditor4Targets.cmake
%_libdir/libMauiKitTextEditor4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
