%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-nota
Version: 4.0.2
Release: alt1

Summary: Multi-platform text editor based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/nota

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
BuildRequires: libmauikit-texteditor-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-texteditor
Requires: libmauikit-terminal

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang nota

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/nota %buildroot%_bindir/org.kde.nota
sed -i "s|Exec=nota|Exec=org.kde.nota|" %buildroot%_desktopdir/org.kde.nota.desktop

%files -f nota.lang
%_bindir/org.kde.nota
%_desktopdir/org.kde.nota.desktop
%_iconsdir/hicolor/scalable/apps/nota.svg
%_datadir/metainfo/org.kde.nota.metainfo.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
