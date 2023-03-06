Name: glaxnimate
Version: 0.5.1
Release: alt1
Summary: A simple vector graphics animation program
Group: Graphics
Vendor: openmamba
Distribution: openmamba
Packager: Artyom Bystrov <arbars@altlinux.org>
Url: https://glaxnimate.mattbas.org/
Source: https://gitlab.com/mattbas/glaxnimate.git/%version/glaxnimate-%version.tar.bz2
Patch: glaxnimate-0.5.1-qt6.patch
Patch1: glaxnimate-0.5.1-cmake-install-libdir.patch
License: GPLv2

BuildRequires: glibc-devel
BuildRequires: libarchive-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libgcc
BuildRequires: libglvnd-devel
BuildRequires: libpotrace-devel
BuildRequires: python3-dev
BuildRequires: libstdc++-devel
BuildRequires: libswscale-devel
BuildRequires: zlib-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: cmake rpm-macros-cmake

%description
A simple vector graphics animation program.


%prep
%setup

%patch0 -p1
%ifarch x86_64 aarch64
%patch1 -p1
%endif

%build
%cmake
%cmake_build
%install

%cmakeinstall_std

%files
%_bindir/glaxnimate
%_desktopdir/glaxnimate.desktop
%dir %_datadir/glaxnimate
%dir %_datadir/glaxnimate/glaxnimate
%_datadir/glaxnimate/glaxnimate/*
%_iconsdir/hicolor/*/apps/glaxnimate.png
%_iconsdir/hicolor/scalable/apps/glaxnimate.svg
%doc COPYING

%changelog
* Fri Mar 03 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.1-alt1
- initial build for ALT Sisyphus

* Mon Sep 12 2022 Silvan Calarco <silvan.calarco@mambasoft.it> 0.5.1-2mamba
- provide external libQtColorWidgets.so.2

* Mon Sep 12 2022 Silvan Calarco <silvan.calarco@mambasoft.it> 0.5.1-1mamba
- package created using the webbuild interface
