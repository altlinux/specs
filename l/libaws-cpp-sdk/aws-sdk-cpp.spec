%def_disable   check
%def_enable    devel
%define        oname aws-cpp-sdk
%if_enabled    devel
%define _unpackaged_files_terminate_build 1
%endif

Name:          lib%oname
Version:       1.11.909
Release:       alt1
Group:         Development/C++
Summary:       AWS SDK for C++
License:       Apache-2.0
Url:           https://github.com/aws/aws-sdk-cpp
Vcs:           https://github.com/aws/aws-sdk-cpp.git

%add_findreq_skiplist %_includedir/*

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(opentelemetry_common)
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-crt-cpp)

# error: cpio archive too big - 5121M
%define optflags_debug -g0

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface
for Amazon Web Services (AWS). It is meant to be performant and fully
functioning with low- and high-level SDKs, while minimizing dependencies and
providing platform portability (Windows, OSX, Linux, and mobile).

AWS SDK for C++ is in now in General Availability and recommended for production
use. We invite our customers to join the development efforts by submitting pull
requests and sending us feedback and ideas via GitHub Issues.


%package       devel
Group:         Development/Other
Summary:       AWS SDK for C++ development files
Requires:      %{name} = %EVR
Requires:      /proc
Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      python3-devel
Requires:      pkgconfig(zlib)
Requires:      pkgconfig(libssl)
Requires:      pkgconfig(libcurl)
Requires:      pkgconfig(opentelemetry_common)
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-crt-cpp)

%description   devel
AWS SDK for C++ development files.

The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface
for Amazon Web Services (AWS). It is meant to be performant and fully
functioning with low- and high-level SDKs, while minimizing dependencies and
providing platform portability (Windows, OSX, Linux, and mobile).

AWS SDK for C++ is in now in General Availability and recommended for production
use. We invite our customers to join the development efforts by submitting pull
requests and sending us feedback and ideas via GitHub Issues.


%prep
%setup

%build
%cmake \
   -Wno-dev \
   -DBUILD_DEPS=OFF \
   -DBUILD_BENCHMARKS=ON \
   -DMINIMIZE_SIZE=ON \
   -DUSE_TLS_V1_3=ON \
%if_enabled    check
   -DENABLE_TESTING=ON \
   -DAUTORUN_UNIT_TESTS=ON \
   -DENABLE_HTTP_CLIENT_TESTING=ON \
%else
   -DENABLE_TESTING=OFF \
   -DAUTORUN_UNIT_TESTS=OFF \
   -DENABLE_HTTP_CLIENT_TESTING=OFF \
%endif
   -DUSE_CRT_HTTP_CLIENT=ON \
   %nil
#   -DENABLE_ADDRESS_SANITIZER=ON \ # fails to build aws-cpp-sdk-polly-sample
#   -DENABLE_HTTP_CLIENT_TESTING=ON \ # NOTE fails to build aws-cpp-sdk-core-tests because of ThreadSanitizer
#   -DBUILD_OPTEL=ON \ #NOTE error in using libtelemetry
#   -DCUSTOM_MEMORY_MANAGEMENT=ON \ #NOTE makes too big RPM ~4Gb
#   -DREGENERATE_CLIENTS -DREGENERATE_DEFAULTS #NOTE goes to internet
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc README*
%_libdir/%{name}*.so

%files         devel
%doc README*
%_libdir/pkgconfig/*.pc
%_includedir/aws
%_includedir/smithy
%_libdir/cmake/%{oname}*
%_libdir/cmake/AWSSDK


%changelog
* Mon Oct 12 2026 Pavel Skrylev <majioa@altlinux.org> 1.11.909-alt1
- Initial build v1.11.909 for Sisyphus without powerpc arch tree
