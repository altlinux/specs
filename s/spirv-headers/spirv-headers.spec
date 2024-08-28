%define git 2acb319

Name: spirv-headers
Version: 1.5.5
Release: alt14.g%{git}
Epoch: 2

Summary: machine-readable files for the SPIR-V Registry
Group: Development/C++
License: BSD

BuildArch: noarch

URL: https://github.com/KhronosGroup/SPIRV-Headers
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
This repository contains machine-readable files for the SPIR-V Registry. This
includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction set and the
  extended instruction sets.
* The XML registry file.
* A tool to build the headers from the JSON grammar.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build
%cmake_install

%files
%doc *.md
%dir %_includedir/spirv
%dir %_datadir/cmake/SPIRV-Headers
%_includedir/spirv/*
%_datadir/cmake/SPIRV-Headers/*
%_datadir/pkgconfig/*.pc

%changelog
* Wed Aug 28 2024 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt14.g2acb319
- Updated to GIT g2acb319 (for sdk-1.3.290.0)

* Thu May 30 2024 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt13.g4f7b471
- Updated to GIT g4f7b471 (for sdk-1.3.283.0).

* Sat Mar 09 2024 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt12.gb73e168
- Updated to GIT b73e168 (incorporate changes from Intel).

* Thu Mar 07 2024 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt11.g1c6bb27
- Updated to GIT 1c6bb27 (for sdk-1.2.275.0).

* Wed Nov 08 2023 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt10.g4183b26
- Updated to GIT 4183b26 (as required by clspv).

* Thu Sep 14 2023 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt9.g124a966
- Updated to GIT 124a966 (for sdk-1.3.261.1).

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt8.g268a061
- Updated to GIT 268a061 (for sdk-1.3.250).
- Don't pack examples (moved to separate library).

* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt7.g1feaf44
- Updated to GIT 1feaf44 (for sdk-1.3.243).

* Fri Mar 03 2023 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt6.gd13b522
- Updated to GIT d13b522 (for sdk-1.3.239).

* Tue Dec 13 2022 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt5.g1d31a10
- Updated to GIT 1d31a10 (for sdk-1.3.236).

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt4.g85a1ed2
- Updated to GIT 85a1ed2 (for spirv-tools 2022.4).

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt3.g0bcc624
- Updated to GIT 0bcc624 (as required by shaderc).
- Remove cmake hacks.

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 2:1.5.5-alt2.gb2a156e
- Updated to GIT b2a156e (tag sdk-1.3.224.1).
- Downgrade version again (as 1.6.0 is not here yet).

* Sat Apr 09 2022 L.A. Kostis <lakostis@altlinux.ru> 1:1.6.0-alt1.g4995a2f
- Updated to GIT 4995a2f (tag sdk-1.3.211).

* Sat Nov 13 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.5-alt1.g814e728
- Updated to GIT 814e728 (as required by SPIRV-Tools).

* Wed Nov 03 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt3.g449bc98
- Updated to GIT 449bc98 (as required by vulkan SDK).

* Sun Jun 27 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt2.g07f259e
- Updated to GIT 07f259e (as required by vulkan SDK).

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt1.gbcf5521
- Update to GIT bcf5521 (as required by SPIRV-Tools).

* Mon Feb 15 2021 L.A. Kostis <lakostis@altlinux.ru> 1:1.5.4-alt1
- Update to 1.5.4.raytracing.fixed.

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 1:1.5.3-alt0.3
- Rollback to 1.5.3-alt0.2 (ALT #39671)

* Fri Feb 05 2021 Nazarov Denis <nenderus@altlinux.org> 1.5.4-alt0.1
- Update to 1.5.4.raytracing.fixed

* Tue Sep 08 2020 L.A. Kostis <lakostis@altlinux.ru> 1.5.3-alt0.2
- Update to 1.5.3.reservations1.

* Thu Jun 04 2020 L.A. Kostis <lakostis@altlinux.ru> 1.5.3-alt0.1
- Updated to 1.5.3.
- Added cmake files.

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt0.1.g059a495
- Updated to GIT 059a495.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.3.7-alt0.1.g2434b89
- Initial build for Sisyphus.
