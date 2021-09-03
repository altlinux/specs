# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: capnproto
Version: 0.8.0
Release: alt3
Summary: A data interchange format and capability-based RPC system
License: MIT
Url: https://capnproto.org
Source: %name-%version.tar
Patch2000: %name-e2k.patch
Group: Development/C

BuildRequires: cmake >= 3.1.0 rpm-macros-cmake ctest
BuildRequires: gcc-c++

%description
Cap'n Proto is data interchange format and capability-based RPC system.
Think JSON, except binary. Or think Protocol Buffers, except faster.

This package contains the schema compiler and command-line encoder and
decoder tools.

%package libs
Summary: Libraries for %name
Group: System/Libraries

%description libs
The %name-libs package contains the libraries for using %name
in applications.

%package devel
Summary: Development files for %name
Requires: %name-libs = %version-%release
Requires: %name = %version-%release
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
# because of "multiple definition of typeinfo" errors at linking
%define typeinfo_fix() \
  sed -i "1i #define TransformPromiseNode TransformPromiseNode_$(echo %1 | tr "-" "_")" c++/src/capnp/%1.c++
%typeinfo_fix ez-rpc
%typeinfo_fix any-test
%typeinfo_fix capability-test
%typeinfo_fix membrane-test
%typeinfo_fix rpc-test
%typeinfo_fix rpc-twoparty-test
%typeinfo_fix ez-rpc-test
%endif

%build
%ifarch %e2k
# too many warnings of this type on tests
%add_optflags -Wno-unused-variable
%endif
%add_optflags %(getconf LFS_CFLAGS) -pthread
cd c++
%autoreconf
%configure --disable-static
%make_build

%install
cd c++
%makeinstall_std

%check
cd c++
# disable networking test
subst '/TEST(AsyncIo, SimpleNetwork)/,/^}/s/^/\/\//' src/kj/async-io-test.c++
%make_build check

%files
%_bindir/cap*

%files libs
%doc LICENSE CONTRIBUTORS README.md
%_libdir/*.so*

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/cmake/CapnProto/

%changelog
* Fri Sep 03 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.8.0-alt3
- Added patch for Elbrus

* Fri Aug 27 2021 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt2
- Do not package static library (fixes build with LTO).
- spec: Fix linking libkj with pthread library.
- spec: Fix use of non-LFS functions on 32-bit arches.

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1
- Updated to upstream version 0.8.0.

* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 0.6.1-alt1
- Initial build of capnproto for ALT.

