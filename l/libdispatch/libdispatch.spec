%def_without check

Name: libdispatch
Version: 5.7.2
Release: alt1

Summary: Apple's Grand Central Dispatch library

License: ASL 2.0
Group: Development/C
Url: https://github.com/apple/swift-corelibs-libdispatch

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define reltag %version-RELEASE

# Source-url: https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%reltag.tar.gz
Source: %name-%version.tar

Patch0: noerrors.patch

BuildRequires: llvm

BuildRequires: clang libstdc++-devel
BuildRequires: libbsd-devel
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: chrpath

%if_with check
BuildRequires: ctest
%endif

# [armh]     clang: error: unable to execute command: Segmentation fault
ExcludeArch: armh ppc64le

Provides:      libBlocksRuntime = %EVR
Obsoletes:     libBlocksRuntime < 7.0.0

# due Block.h
Conflicts: libgnustep-objc2-devel < 2.1-alt3

#define optflags_lto -flto=thin

%description
Grand Central Dispatch (GCD or libdispatch) provides
comprehensive support for concurrent code execution on
multicore hardware.

libdispatch is currently available on all Darwin platforms.
This project aims to make a modern version of libdispatch
available on all other Swift platforms. To do this, we will
implement as much of the portable subset of the API as
possible, using the existing open source C implementation.

libdispatch on Darwin is a combination of logic in the xnu
kernel alongside the user-space Library. The kernel has the
most information available to balance workload across the
entire system. As a first step, however, we believe it is
useful to bring up the basic functionality of the library
using user-space pthread primitives on Linux. Eventually, a
Linux kernel module could be developed to support more
informed thread scheduling.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/C
Provides: libBlocksRuntime-devel = %EVR
Obsoletes: libBlocksRuntime-devel < 7.0.0

%description devel
Development files for %name.

%prep
%setup
%patch0 -p0

%build
export CXX=clang++
export CC=clang
%cmake -G Ninja
%cmake_build

%install
%cmake_install
chrpath --delete %buildroot%_libdir/libdispatch.so

%check
%cmake_build --target test

%files
%doc LICENSE
%_libdir/libBlocksRuntime.so
%_libdir/libdispatch.so
%_man3dir/*

%files devel
%_includedir/Block.h
%_includedir/dispatch/
%_includedir/os/

%changelog
* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 5.7.2-alt1
- new version 5.7.2 (with rpmrb script)

* Fri Jul 22 2022 Vitaly Lipatov <lav@altlinux.ru> 5.6.2-alt1
- new version 5.6.2 (with rpmrb script)

* Wed Apr 20 2022 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt3
- add Conflicts: libgnustep-objc2-devel

* Mon Apr 18 2022 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt2
- build for all Telegram arches

* Fri Apr 15 2022 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- initial build for ALT Sisyphus

* Wed Mar 23 2022 Ron Olson <tachoknight@gmail.com> 5.6.0-2
- Added patch to allow for building on EPEL-8
* Tue Mar 22 2022 Ron Olson <tachoknight@gmail.com> 5.6.0-1
- Updated to 5.6.0-RELEASE
* Tue Dec 14 2021 Ron Olson <tachoknight@gmail.com> 5.5.2-1
- Updated to 5.5.2-RELEASE
* Fri Oct 29 2021 Ron Olson <tachoknight@gmail.com> 5.5.1-1
- Updated to 5.5.1-RELEASE
* Tue Jun 01 2021 Ron Olson <tachoknight@gmail.com> 5.4.1-1
- Updated to 5.4.1-RELEASE
* Sat May 01 2021 Ron Olson <tachoknight@gmail.com> 5.4-1
- Updated to 5.4-RELEASE also added explicit CMake step
  for EPEL8
* Wed Feb 03 2021 Ron Olson <tachoknight@gmail.com> 5.3.3-1
- Initial version based on version 5.3.3-RELEASE
