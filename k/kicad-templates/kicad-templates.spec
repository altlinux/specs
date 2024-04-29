# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-templates
Summary: Templates projects for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): Примеры проектов для kicad (разработка печатных плат)
Version: 8.0.2
Release: alt1
License: GPL-3.0-or-later
Group: Engineering
Url: https://gitlab.com/kicad/libraries/%name
# Source-url: https://gitlab.com/kicad/libraries/%name/-/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

Requires: kicad-common >= %version

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of templates projects by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-%name содержит примеры проектов для kicad.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_datadir/kicad/template/*

%changelog
* Mon Apr 29 2024 Anton Midyukov <antohami@altlinux.org> 8.0.2-alt1
- new version (8.0.2) with rpmgs script

* Sun Mar 03 2024 Anton Midyukov <antohami@altlinux.org> 8.0.0-alt1
- new version (8.0.0) with rpmgs script

* Fri Dec 29 2023 Anton Midyukov <antohami@altlinux.org> 7.0.10-alt1
- new version (7.0.10) with rpmgs script

* Mon Oct 02 2023 Anton Midyukov <antohami@altlinux.org> 7.0.8-alt1
- new version (7.0.8) with rpmgs script

* Fri Apr 14 2023 Anton Midyukov <antohami@altlinux.org> 7.0.2-alt1
- new version (7.0.2) with rpmgs script

* Sun Feb 12 2023 Anton Midyukov <antohami@altlinux.org> 7.0.0-alt1
- new version (7.0.0) with rpmgs script

* Wed Jun 22 2022 Anton Midyukov <antohami@altlinux.org> 6.0.6-alt1
- new version (6.0.6) with rpmgs script

* Sun May 08 2022 Anton Midyukov <antohami@altlinux.org> 6.0.5-alt1
- new version (6.0.5) with rpmgs script

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 6.0.2-alt1
- new version (6.0.2) with rpmgs script

* Tue Jan 04 2022 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- new version (6.0.0) with rpmgs script

* Sat Feb 13 2021 Anton Midyukov <antohami@altlinux.org> 5.1.9-alt1
- new version (5.1.9) with rpmgs script
- Update URL

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.4-alt1
- new version (5.1.4) with rpmgs script

* Fri Apr 26 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- new version 5.1.2

* Sat Mar 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- new version 5.0.2

* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
