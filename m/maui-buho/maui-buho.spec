%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-buho
Version: 4.0.2
Release: alt1

Summary: Task and Note Keeper based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/buho

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
BuildRequires: libmauikit-accounts-devel
BuildRequires: libmauikit-texteditor-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-accounts
Requires: libmauikit-texteditor

%description
%summary.

Buho allows you to save links, write quick notes and organize pages as
books. Buho works on desktops, Android and Plasma Mobile.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang buho

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/buho %buildroot%_bindir/org.kde.buho
sed -i "s|Exec=buho|Exec=org.kde.buho|" %buildroot%_desktopdir/org.kde.buho.desktop

%files -f buho.lang
%doc README.md
%_bindir/org.kde.buho
%_desktopdir/org.kde.buho.desktop
%_iconsdir/hicolor/scalable/apps/buho.svg
%_datadir/metainfo/org.kde.buho.metainfo.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
