%define cl_hpp_ver 2.0.10
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: opencl-headers
Version: 2024.05.08
Release: alt1
Epoch: 1

Summary: OpenCL (Open Computing Language) header files

License: MIT
Group: Development/C
Url: https://www.khronos.org/registry/cl/

#Source-git: https://github.com/KhronosGroup/OpenCL-Headers.git
# Source-url: https://github.com/KhronosGroup/OpenCL-Headers/archive/master.zip
Source: %name-%version.tar

Source1: https://github.com/KhronosGroup/OpenCL-CLHPP/releases/download/v%cl_hpp_ver/cl2.hpp
# OCL 1.2 compatibility
Source2: https://www.khronos.org/registry/cl/api/%version/cl.hpp

BuildRequires(pre): cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
%summary.

%prep
%setup
cp -p %SOURCE1 %SOURCE2 CL/
# We're not interested in Direct3D things
rm -vf CL/{cl_dx9_media_sharing*.h,cl_d3d10.h,cl_d3d11.h}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_includedir/CL
%_datadir/cmake/OpenCLHeaders
%_datadir/pkgconfig/OpenCL-Headers.pc

%changelog
* Thu May 23 2024 L.A. Kostis <lakostis@altlinux.ru> 1:2024.05.08-alt1
- v2024.05.08.

* Tue Feb 13 2024 L.A. Kostis <lakostis@altlinux.ru> 1:2023.12.14-alt1
- v2023.12.14.

* Thu Nov 16 2023 L.A. Kostis <lakostis@altlinux.ru> 1:2023.04.17-alt1
- Rebased to v2023.04.17.
- .spec: restructure.

* Thu Nov 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2.2-alt2
- Fix compile on ppc64le (upstream pull #38).

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version (2.2) with rpmgs script

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_2
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2
- initial fc import

