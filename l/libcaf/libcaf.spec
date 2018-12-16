Name: libcaf
Version: 0.16.2
Release: alt1

Summary: An Open Source Implementation of the Actor Model in C++

Group: Networking/Other
License: BSD / Boost
Url: http://www.actor-framework.org/

# Source-url: https://github.com/actor-framework/actor-framework/archive/%version.tar.gz
Source: %name-%version.tar
Patch: libcaf-0.16.2-fix-linking.patch

BuildRequires: gcc-c++ libcurl-devel libssl-devel ocl-icd-devel

BuildRequires: cmake

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
%patch -p1
# TODO: LIB_DESTINATION
%__subst "s|LIBRARY DESTINATION lib|LIBRARY DESTINATION %_lib|" */CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libcaf_core.so.%version
%_libdir/libcaf_io.so.%version
%_libdir/libcaf_opencl.so.%version
%_libdir/libcaf_openssl.so.%version

%files devel
%_includedir/caf/
%_libdir/libcaf_core.so
%_libdir/libcaf_io.so
%_libdir/libcaf_opencl.so
%_libdir/libcaf_openssl.so
%_datadir/caf/


%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 0.16.2-alt1
- initial build for ALT Sisyphus
