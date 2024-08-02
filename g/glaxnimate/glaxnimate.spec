%define _metadir %_datadir/metainfo

Name: glaxnimate
Version: 0.5.4
Release: alt1
Summary: A simple vector graphics animation program
Group: Graphics
Packager: Artyom Bystrov <arbars@altlinux.org>
Url: https://glaxnimate.mattbas.org/
Source: https://gitlab.com/mattbas/glaxnimate.git/%version/glaxnimate-%version.tar.bz2
Patch: glaxnimate-0.5.1-qt6.patch
License: BSD-2-Clause and CC-BY-SA-4.0 and CC0-1.0 and GPL-3.0-or-later and Unicode-TOU

BuildRequires: libarchive-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libglvnd-devel
BuildRequires: libpotrace-devel
BuildRequires: python3-dev
BuildRequires: libstdc++-devel
BuildRequires: libswscale-devel
BuildRequires: zlib-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel qt6-svg
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
%cmake_build
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
%_iconsdir/hicolor/512x512/apps/glaxnimate.png
%_iconsdir/hicolor/scalable/apps/org.mattbas.Glaxnimate.svg
%_iconsdir/hicolor/scalable/apps/glaxnimate.svg
%_metadir/org.mattbas.Glaxnimate.metainfo.xml
%doc *.md

%changelog
* Fri Aug  2 2024 Artyom Bystrov <arbars@altlinux.org> 0.5.4-alt1
- Update to new version
- Added russian translation

* Thu Aug 24 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.3-alt3
- Back to default version of libstdc++-devel
- Update patch for Qt6 support
- Temporary fixed bug with disappeared icons (https://bugzilla.altlinux.org/45664)
- Minor spec cleanup

* Fri Jul 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.3-alt2
- Fixed the package License: tag (GPLv2 -> BSD-2-Clause and CC-BY-SA-4.0 and
  CC0-1.0 and GPL-3.0 and Unicode-TOU).
- Switched to the default gcc version (from gcc 12 to gcc 13).
- Moved the build process from the %%install section to the %%build
  section.
- Removed unused patches.

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
