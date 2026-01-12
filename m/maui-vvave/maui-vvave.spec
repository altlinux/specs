%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-vvave
Version: 4.0.2
Release: alt1

Summary: VVAVE Music Player based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/vvave

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel
BuildRequires: pkgconfig(taglib-2)
BuildRequires: libmauikit-accounts-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-accounts

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang vvave

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/vvave %buildroot%_bindir/org.kde.vvave
sed -i "s|Exec=vvave|Exec=org.kde.vvave|" %buildroot%_desktopdir/org.kde.vvave.desktop

%files -f vvave.lang
%doc README.md
%_bindir/org.kde.vvave
%_desktopdir/org.kde.vvave.desktop
%_iconsdir/hicolor/scalable/apps/vvave.svg
%_datadir/metainfo/org.kde.vvave.appdata.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
