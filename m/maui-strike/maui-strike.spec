%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-strike
Version: 2.0.1
Release: alt1

Summary: Simple minimal IDE for the Linux phones based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/maui-strike

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
BuildRequires: libmauikit-filebrowsing-devel
BuildRequires: libmauikit-terminal-devel
BuildRequires: libmauikit-texteditor-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-terminal
Requires: libmauikit-texteditor

%description
Strike is a simple minimal IDE for the Linux phones based on Maui
framework.
Code, build, and run from the phone.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang strike

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/strike %buildroot%_bindir/org.kde.strike
sed -i "s|Exec=strike|Exec=org.kde.strike|" %buildroot%_desktopdir/org.kde.strike.desktop

%files -f strike.lang
%_bindir/org.kde.strike
%_desktopdir/org.kde.strike.desktop
%_iconsdir/hicolor/scalable/apps/strike.svg
%_datadir/metainfo/org.kde.strike.metainfo.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
