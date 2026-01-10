%define oname org.kde.drawy

Name: drawy
Version: 20260110
Release: alt1

Summary: Drawy is a work-in-progress infinite whiteboard tool
License: GPL-3.0-or-later
Group: Graphics

Url: https://apps.kde.org/drawy
Vcs: https://invent.kde.org/graphics/drawy

ExcludeArch: i586

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kcrash-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kwidgetsaddons-devel libzstd-devel
BuildRequires: qt6-tools-devel

%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++,
which aims to be a native-desktop alternative to the amazing web-based Excalidraw.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%files
%doc *.md LICENSES
%_bindir/%name
%_libdir/*.so.*
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/*/*.png
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/qlogging-categories?/%name.categories
%_datadir/locale/*/LC_MESSAGES/*.qm

%changelog
* Sat Jan 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260110-alt1
- Initial build for ALT Linux.
