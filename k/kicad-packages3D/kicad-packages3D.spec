# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-packages3D
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Version: 10.0.4
Release: alt1
Source: %name-%version.tar
License: GPL-2.0-or-later
Group: Engineering
URL: https://gitlab.com/kicad/libraries/kicad-packages3D
VCS: https://gitlab.com/kicad/libraries/kicad-packages3D

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

Requires: kicad-common >= 10.0

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит 3D-модели для kicad.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_datadir/kicad/3dmodels

%changelog
* Sat Jun 20 2026 Anton Midyukov <antohami@altlinux.org> 10.0.4-alt1
- New version 10.0.4.

* Thu May 14 2026 Anton Midyukov <antohami@altlinux.org> 10.0.3-alt1
- New version 10.0.3.

* Thu Apr 16 2026 Anton Midyukov <antohami@altlinux.org> 10.0.1-alt1
- New version 10.0.1.

* Tue Mar 31 2026 Anton Midyukov <antohami@altlinux.org> 10.0.0-alt1
- New version 10.0.0 (Closes: 58452).

* Sun May 08 2022 Anton Midyukov <antohami@altlinux.org> 6.0.5-alt1
- new version 6.0.5

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 6.0.2-alt1
- new version 6.0.2

* Thu Jan 06 2022 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- new version 6.0.0

* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 5.1.6-alt1
- new version 5.1.6

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.4-alt1
- new version 5.1.4

* Fri Apr 26 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- New version 5.1.2

* Sat Mar 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.0-alt1
- New version 5.1.0

* Sat Jan 05 2019 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- New version 5.0.2

* Thu Nov 22 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- New version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
