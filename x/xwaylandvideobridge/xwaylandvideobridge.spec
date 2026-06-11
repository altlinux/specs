%define _unpackaged_files_terminate_build 1

Name: xwaylandvideobridge
Version: 0.5.0
Release: alt2

Summary: Utility to allow streaming Wayland windows to X applications
License: (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
Group: System/X11
Url: https://invent.kde.org/system/xwaylandvideobridge

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-event)
BuildRequires: plasma6-kpipewire-devel
BuildRequires: kf6-kstatusnotifieritem-devel

%description
By design, X11 applications can't access window or screen contents for
wayland clients. This is fine in principle, but it breaks screen sharing
in tools like Discord, MS Teams, Skype, etc and more.

This tool allows us to share specific windows to X11 clients, but within
the control of the user at all times.

%prep
%setup
%patch -p1

%build
%K6build \
         -DQT_MAJOR_VERSION=6

%install
%K6install
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files -f %name.lang
%doc README.md LICENSES/*
%_K6bin/*
%_K6xdgapp/*.desktop
%_K6icon/hicolor/*/apps/*
%_datadir/metainfo/*.xml
%_K6start/*
%_K6data/qlogging-categories6/*.*categories

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt2
- Updated license tag.

* Mon May 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Fri Feb 06 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt2
- Fixed FTBFS with Qt 6.10.

* Sat May 24 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
