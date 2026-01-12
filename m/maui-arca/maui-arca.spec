%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-arca
Version: 1.0.2
Release: alt1

Summary: Archiver for compressed files based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/arca

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-karchive-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel
BuildRequires: libmauikit-archiver-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-archiver
Requires: libmauikit-documents
Requires: libmauikit-texteditor

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang arca

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/arca %buildroot%_bindir/org.kde.arca
sed -i "s|Exec=arca|Exec=org.kde.arca|" %buildroot%_desktopdir/org.kde.arca.desktop

%files -f arca.lang
%_bindir/org.kde.arca
%_desktopdir/org.kde.arca.desktop
%_iconsdir/hicolor/scalable/apps/arca.svg
%_datadir/metainfo/org.kde.arca.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
