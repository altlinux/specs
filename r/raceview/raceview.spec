%define _unpackaged_files_terminate_build 1

Name: raceview
Version: 0.99.4
Release: alt1

Summary: Multi-track synchronized video player built with Qt6 + libmpv
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/r0ck3r/RaceView

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(mpv)

%description
Multi-track synchronized video player built with Qt6 and libmpv.

RaceView plays several video files side by side and keeps them in sync
against a single master track. It is designed for reviewing the same event
from multiple sources (for example, an F1 race broadcast together with
onboard / data-channel feeds) with per-track audio selection, offset,
and volume.

%prep
%setup
sed -i "s/^GenericName=/GenericName=Multi-Track Synchronized Video Player/" raceview.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%files -f %{name}.lang
%doc README.md
%_bindir/raceview
%_desktopdir/raceview.desktop
%_iconsdir/hicolor/scalable/apps/raceview.svg

%changelog
* Thu Oct 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.99.4-alt1
- Initial build for Sisyphus
