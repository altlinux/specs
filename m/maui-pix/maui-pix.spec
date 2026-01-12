%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-pix
Version: 4.0.2
Release: alt1

Summary: Image gallery application based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/pix

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Positioning)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kio-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel
BuildRequires: libmauikit-imagetools-devel

# no libmauikit-imagetools-devel
ExcludeArch: %ix86 riscv64

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-imagetools

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang pix

# prevent file conflict with other packages
mv -v %buildroot%_bindir/pix %buildroot%_bindir/org.kde.pix
sed -i "s|Exec=pix|Exec=org.kde.pix|" %buildroot%_desktopdir/org.kde.pix.desktop

%files -f pix.lang
%doc README.md
%_bindir/org.kde.pix
%_desktopdir/org.kde.pix.desktop
%_iconsdir/hicolor/scalable/apps/pix.svg
%_datadir/metainfo/org.kde.pix.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
