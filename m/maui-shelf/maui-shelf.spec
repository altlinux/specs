%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-shelf
Version: 4.0.2
Release: alt1

Summary: Document and EBook collection manager based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/shelf

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel
BuildRequires: libmauikit-documents-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-documents
Requires: libmauikit-texteditor

%description
%summary.

%prep
%setup
sed -i "s|Categories=Qt;KDE;Graphics;Office;Viewer;|Categories=Qt;KDE;Office;Viewer;|" org.kde.shelf.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang shelf

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/shelf %buildroot%_bindir/org.kde.shelf
sed -i "s|Exec=shelf|Exec=org.kde.shelf|" %buildroot%_desktopdir/org.kde.shelf.desktop

%files -f shelf.lang
%_bindir/org.kde.shelf
%_desktopdir/org.kde.shelf.desktop
%_iconsdir/hicolor/scalable/apps/shelf.svg
%_datadir/metainfo/org.kde.shelf.metainfo.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
