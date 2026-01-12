%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-paleta
Version: 1.0.0
Release: alt1.git.f1922e21

Summary: Color utilities based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/paleta

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: libmauikit-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing

%description
%summary.

%prep
%setup
sed -i "s|Categories=Qt;KDE;Utility;|Categories=Qt;KDE;Publishing;Graphics;|" data/org.kde.paleta.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang paleta

# prevent file conflict with other packages
mv -v %buildroot%_bindir/paleta %buildroot%_bindir/org.kde.paleta
sed -i "s|Exec=paleta|Exec=org.kde.paleta|" %buildroot%_desktopdir/org.kde.paleta.desktop

%files -f paleta.lang
%_bindir/org.kde.paleta
%_desktopdir/org.kde.paleta.desktop
%_iconsdir/hicolor/scalable/apps/paleta.svg
%_datadir/metainfo/org.kde.paleta.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1.git.f1922e21
- Initial build for Sisyphus
