%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-communicator
Version: 4.0.2
Release: alt1

Summary: Contacts and dialer application based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/communicator

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kio-devel
BuildRequires: libmauikit-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: kf6-kpeople-devel
BuildRequires: libmauikit-filebrowsing-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing

%description
%summary.

%prep
%setup
sed -i "s|Categories=Qt;KDE;System;|Categories=Qt;KDE;Utility;TelephonyTools;|" org.kde.communicator.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang communicator

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/communicator %buildroot%_bindir/org.kde.communicator
sed -i "s|Exec=communicator|Exec=org.kde.communicator|" %buildroot%_desktopdir/org.kde.communicator.desktop

%files -f communicator.lang
%_bindir/org.kde.communicator
%_desktopdir/org.kde.communicator.desktop
%_iconsdir/hicolor/scalable/apps/communicator.svg
%_datadir/maui-accounts/manifests/org.kde.communicator.json
%_datadir/metainfo/org.kde.communicator.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
