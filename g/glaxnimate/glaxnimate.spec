%define _metadir %_datadir/metainfo
%set_gcc_version 12

Name: glaxnimate
Version: 0.5.3
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
Patch2: glaxnimate-pybind11_fix_build.patch
License: GPLv2

BuildRequires: glibc-devel gcc12-c++
BuildRequires: libarchive-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libgcc
BuildRequires: libglvnd-devel
BuildRequires: libpotrace-devel
BuildRequires: python3-dev
BuildRequires: libstdc++12-devel
BuildRequires: libswscale-devel
BuildRequires: zlib-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: cmake rpm-macros-cmake
Requires: icon-theme-breeze

%description
A simple vector graphics animation program.


%prep
%setup

%patch0 -p1

%build
%cmake 
%make_build translations -C %_cmake__builddir
%install

%cmakeinstall_std

%files
%_bindir/glaxnimate
%_desktopdir/org.mattbas.Glaxnimate.desktop
%dir %_datadir/glaxnimate
%dir %_datadir/glaxnimate/glaxnimate
%_datadir/glaxnimate/glaxnimate/*
%_iconsdir/hicolor/*/apps/org.mattbas.Glaxnimate.png
%_iconsdir/hicolor/scalable/apps/org.mattbas.Glaxnimate.svg
%_metadir/org.mattbas.Glaxnimate.metainfo.xml
%doc *.md

%changelog
* Sat Jun 10 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.3-alt1
- update to new version

* Fri Mar 10 2023 Grigory Ustinov <grenka@altlinux.org> 0.5.1-alt2
- Fixed build with python3.11.

* Fri Mar 03 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.1-alt1
- initial build for ALT Sisyphus

* Mon Sep 12 2022 Silvan Calarco <silvan.calarco@mambasoft.it> 0.5.1-2mamba
- provide external libQtColorWidgets.so.2

* Mon Sep 12 2022 Silvan Calarco <silvan.calarco@mambasoft.it> 0.5.1-1mamba
- package created using the webbuild interface
