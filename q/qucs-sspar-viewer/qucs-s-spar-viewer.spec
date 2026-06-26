#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qucs-sspar-viewer
Version: 2026.05.12
Release: alt1
Summary: Qucs-S S-parameter and RF Circuit Synthesis Tool

Group: Engineering
License: GPL-3.0-or-later

URL: https://andresmmera.github.io/qucs-s-spar-viewer/
VCS: https://github.com/andresmmera/qucs-s-spar-viewer

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires(pre): rpm-macros-cmake
Buildrequires: rpm-build-cmake
Buildrequires: gcc-c++
Buildrequires: qt6-base-devel
Buildrequires: libcups-devel

%description
A S-parameter data viewer with tools to RF circuit design.
This tool is part of the Qucs-S project.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_desktopdir/
install -m 0644 qucs-s-spar-viewer.desktop %buildroot%_desktopdir/
mkdir -p %buildroot%_liconsdir/
install -m 0644 qucs-s-spar-viewer.png %buildroot%_liconsdir/
mkdir -p %buildroot%_man1dir/
install -m 0644 qucs-s-spar-viewer.1 %buildroot%_man1dir/
rm -rf docs/help/source

%files
%doc LICENSE VERSION docs
%_man1dir/*.1.*
%_bindir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_liconsdir/*.png

%changelog
* Fri Jun 26 2026 Polina Poidenko <polipoki@altlinux.org> 2026.05.12-alt1
- New version 2026.05.12.

* Wed Apr 29 2026 Polina Poidenko <polipoki@altlinux.org> 2026.04.14-alt1
- New version 2026.04.14.

* Fri Apr 10 2026 Polina Poidenko <polipoki@altlinux.org> 2026.04.10-alt1
- Initial build for Sisyphus.

