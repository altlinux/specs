%define nameU org.kde.transistor

Name: transistor
Version: 1.1
Release: alt1

Summary: Internet radio player for KDE
License: BSD-3-Clause and BSD-2-Clause and GPL-2.0-or-later
Group: Sound

URL: https://invent.kde.org/saurov/transistor
Vcs: https://invent.kde.org/saurov/transistor

Source: %name-%version.tar

BuildRequires(Pre): rpm-build-kf6
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: qt6-multimedia-devel qt6-svg-devel
BuildRequires: kf6-kirigami-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel
BuildRequires: kf6-kcolorscheme-devel kf6-kiconthemes-devel
BuildRequires: kf6-knotifications-devel

%description
Internet radio player that provides access to a station database
with over 50,000 stations.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%files
%_bindir/%name
%_datadir/applications/%nameU.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/knotifications?/%name.*
%_datadir/metainfo/%nameU.metainfo.xml
%doc *.md

%changelog
* Fri Oct 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.1-alt1
- Initial build for ALT Linux.

