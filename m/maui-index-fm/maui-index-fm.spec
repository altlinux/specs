%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-index-fm
Version: 4.0.2
Release: alt1

Summary: Multi-platform file manager based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/index-fm

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
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kio-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-filebrowsing-devel

Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libmauikit-archiver
Requires: libqt6-multimediaquick
Requires: libmauikit-terminal
Requires: libmauikit-documents

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang index-fm

# prevent file conflict with other packages
mv -v %buildroot%_bindir/index %buildroot%_bindir/org.kde.index
sed -i "s|Exec=index|Exec=org.kde.index|" %buildroot%_desktopdir/org.kde.index.desktop

%files -f index-fm.lang
%doc README.md screenshots
%_bindir/org.kde.index
%_desktopdir/org.kde.index.desktop
%_iconsdir/hicolor/scalable/apps/index.svg
%_datadir/knotifications6/org.kde.index.notifyrc
%_datadir/metainfo/org.kde.index.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
