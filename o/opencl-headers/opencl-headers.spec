%define cl_hpp_ver 2.0.10

Name: opencl-headers
Version: 2.2
Release: alt1

Summary: OpenCL (Open Computing Language) header files

License: MIT
Group: Development/C++
Url: https://www.khronos.org/registry/cl/

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-git: https://github.com/KhronosGroup/OpenCL-Headers.git
# Source-url: https://github.com/KhronosGroup/OpenCL-Headers/archive/master.zip
Source: %name-%version.tar

Source1: https://github.com/KhronosGroup/OpenCL-CLHPP/releases/download/v%cl_hpp_ver/cl2.hpp
# OCL 1.2 compatibility
Source2: https://www.khronos.org/registry/cl/api/%version/cl.hpp

BuildArch: noarch

%description
%summary.

%prep
%setup

cp -p %SOURCE1 %SOURCE2 opencl22/CL/
# We're not interested in Direct3D things
rm -vf opencl22/CL/{cl_dx9_media_sharing*.h,cl_d3d10.h,cl_d3d11.h}

%build
# Nothing to build

%install
mkdir -p %buildroot%_includedir/CL/
install -p -m 0644 opencl22/CL/* -t %buildroot%_includedir/CL/

%files
%dir %_includedir/CL/
%_includedir/CL/opencl.h
%_includedir/CL/cl_platform.h
%_includedir/CL/cl.h
%_includedir/CL/cl_ext.h
%_includedir/CL/cl_ext_intel.h
%_includedir/CL/cl_egl.h
%_includedir/CL/cl_gl.h
%_includedir/CL/cl_gl_ext.h
%_includedir/CL/cl_va_api_media_sharing_intel.h
%_includedir/CL/cl2.hpp
%_includedir/CL/cl.hpp

%changelog
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

