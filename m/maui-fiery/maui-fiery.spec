%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-fiery
Version: 2.0.1
Release: alt1

Summary: Convergent web browser based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/fiery

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel

# no Qt6WebEngineCore
ExcludeArch: %ix86 riscv64

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libqt6-webenginequick

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang fiery

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/fiery %buildroot%_bindir/org.kde.fiery
sed -i "s|Exec=fiery|Exec=org.kde.fiery|" %buildroot%_desktopdir/org.kde.fiery.desktop

%files -f fiery.lang
%_bindir/org.kde.fiery
%_desktopdir/org.kde.fiery.desktop
%_iconsdir/hicolor/scalable/apps/fiery.svg
%_datadir/metainfo/org.kde.fiery.metainfo.xml

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
