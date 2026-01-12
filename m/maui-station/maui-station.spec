%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-station
Version: 4.0.2
Release: alt1

Summary: Convergent terminal emulator based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/station

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
BuildRequires: libmauikit-terminal-devel
BuildRequires: libmauikit-filebrowsing-devel

Requires: libmauikit
Requires: libmauikit-terminal
Requires: libmauikit-filebrowsing

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang station

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/station %buildroot%_bindir/org.kde.station
sed -i "s|Exec=station|Exec=org.kde.station|" %buildroot%_desktopdir/org.kde.station.desktop

%files -f station.lang
%_bindir/org.kde.station
%_desktopdir/org.kde.station.desktop
%_iconsdir/hicolor/scalable/apps/station.svg
%_datadir/metainfo/org.kde.station.appdata.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
