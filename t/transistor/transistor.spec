%define nameU ru.transistor_radio.transistor

Name: transistor
Version: 1.5
Release: alt1

Summary: Internet radio player for KDE
License: LGPL-3.0-only and GPL-3.0-or-later
Group: Sound

URL: https://gitlab.com/driglu4it/transistor
Vcs: https://gitlab.com/driglu4it/transistor

Source: %name-%version.tar

BuildRequires(Pre): rpm-build-kf6
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: qt6-multimedia-devel qt6-svg-devel
BuildRequires: kf6-kirigami-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel
BuildRequires: kf6-kcolorscheme-devel kf6-kiconthemes-devel
BuildRequires: kf6-knotifications-devel kf6-kdbusaddons-devel

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

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%nameU.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/knotifications?/%name.*
%_datadir/metainfo/%nameU.metainfo.xml
%doc *.md

%changelog
* Thu Mar 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5-alt1
- 1.3 -> 1.5 (git.a1eaf2d3bf)
- chenged url && vcs
- chenged license

* Wed Jan 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3-alt1
- 1.1 -> 1.3

* Fri Oct 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.1-alt1
- Initial build for ALT Linux.

