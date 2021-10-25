%ifarch ppc64le %e2k
%def_without opencv
%else
%def_with opencv
%endif

Name: libcaf
Version: 0.18.5
Release: alt1

Summary: An Open Source Implementation of the Actor Model in C++

License: BSD / Boost
Group: Networking/Other
Url: http://www.actor-framework.org/

# Source-url: https://github.com/actor-framework/actor-framework/archive/%version.tar.gz
Source: %name-%version.tar
Patch: libcaf-0.16.2-fix-linking.patch

BuildRequires: gcc-c++ libcurl-devel libssl-devel
%{?_with_opencv:BuildRequires: ocl-icd-devel}

BuildRequires(pre): cmake

%description
CAF is an open source C++11 actor model implementation
featuring lightweight & fast actor implementations,
pattern matching for messages, network transparent messaging, and more.

%package devel
Summary: Development file for %name
Requires: %name = %EVR
Group: Networking/Other

%description devel
This package contains the header files for %name.


%prep
%setup
#patch -p1
# TODO: LIB_DESTINATION
sed -i "s|LIBRARY DESTINATION lib|LIBRARY DESTINATION %_lib|" */CMakeLists.txt

%build
%cmake %{?_with_opencv:-DCAF_NO_OPENCL:BOOL=yes}
%cmake_build

%install
%cmakeinstall_std
# TODO: pack tools?
rm -rv %buildroot%_datadir/caf/

%files
%_libdir/libcaf_*.so.*

%files devel
%_includedir/caf/
%_libdir/libcaf_*.so
%_libdir/cmake/CAF/
#%_datadir/caf/


%changelog
* Sat Sep 25 2021 Vitaly Lipatov <lav@altlinux.ru> 0.18.5-alt1
- new version 0.18.5 (with rpmrb script)

* Fri Oct 11 2019 Michael Shigorin <mike@altlinux.org> 0.16.2-alt3
- move to opencv knob (on by default except for ppc64le, %%e2k)
- minor spec cleanup

* Tue Oct 08 2019 Alexey Shabalin <shaba@altlinux.org> 0.16.2-alt2
- disable build with opencl support for ppc64le

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 0.16.2-alt1
- initial build for ALT Sisyphus
