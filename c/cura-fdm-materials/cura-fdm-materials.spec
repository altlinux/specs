Name: cura-fdm-materials
Version: 5.4.0
Release: alt1
Summary: Cura FDM Material database
License: Public Domain
Group: Engineering
Url: https://github.com/Ultimaker/fdm_materials

# Source-url: https://github.com/Ultimaker/fdm_materials/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        CMakeLists.txt
Source3:        CPackConfig.cmake

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Cura material files.

These files are needed to work with printers like Ultimaker 2+ and Ultimaker 3.

%prep
%setup
rm CMakeLists.txt
cp %SOURCE2 %SOURCE3 .

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_datadir/cura
%dir %_datadir/cura/resources
%_datadir/cura/resources/materials

%changelog
* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Thu Apr 27 2023 Anton Midyukov <antohami@altlinux.org> 5.3.0-alt1
- new version (5.3.0) with rpmgs script

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 4.12.0-alt1
- new version (4.12.0) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- new version 4.8

* Fri Sep 18 2020 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt1
- new version 4.7.1

* Fri May 08 2020 Anton Midyukov <antohami@altlinux.org> 4.6.1-alt1
- new version 4.6.1

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 4.4.1-alt1
- new version 4.4.1

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 3.6.0-alt1
- new version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 3.5.1-alt1
- new version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Sisyphus.
