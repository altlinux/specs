%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-accounts
Version: 4.0.2
Release: alt1

Summary: MauiKit utilities to handle User Accounts
License: LGPL-2.1-or-later
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-accounts

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel

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

%find_lang mauikitaccounts

%files -f mauikitaccounts.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/accounts
%_libdir/qt6/qml/org/mauikit/accounts/*

%files -n lib%{name}
%_libdir/libMauiKitAccounts4.so.4
%_libdir/libMauiKitAccounts4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/Accounts
%_includedir/MauiKit4/Accounts/accounts_export.h
%_includedir/MauiKit4/Accounts/accounts_version.h
%_includedir/MauiKit4/Accounts/mauiaccounts.h
%_includedir/MauiKit4/Accounts/moduleinfo.h
%dir %_libdir/cmake/MauiKitAccounts4
%_libdir/cmake/MauiKitAccounts4/MauiKitAccounts4Config.cmake
%_libdir/cmake/MauiKitAccounts4/MauiKitAccounts4ConfigVersion.cmake
%_libdir/cmake/MauiKitAccounts4/MauiKitAccounts4Targets-noconfig.cmake
%_libdir/cmake/MauiKitAccounts4/MauiKitAccounts4Targets.cmake
%_libdir/libMauiKitAccounts4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
