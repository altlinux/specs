# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: capnproto
Version: 0.10.2
Release: alt1
Summary: A data interchange format and capability-based RPC system
Group: Development/C
License: MIT
Url: https://capnproto.org
Vcs: https://github.com/capnproto/capnproto

Source: %name-%version.tar
Patch2000: %name-e2k.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: zlib-devel

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
%add_optflags %(getconf LFS_CFLAGS)
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
# AsyncIo/AncillaryMessageHandler test will fail on older kernels (such as
# 4.9.56-std-def-alt1.1), but is not important and could be ignored, for
# details look at https://github.com/capnproto/capnproto/issues/1349
subst '/TEST(AsyncIo, AncillaryMessageHandler)/,/^}/s/^/\/\//' src/kj/async-io-test.c++
%make_build check

%files
%_bindir/cap*

%files libs
%doc LICENSE CONTRIBUTORS README.md
%_libdir/*-%version.so

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/cmake/CapnProto
%exclude %_libdir/*-%version.so
%_libdir/lib*.so

%changelog
* Wed Aug 31 2022 Vitaly Chikunov <vt@altlinux.org> 0.10.2-alt1
- Update to v0.10.2 (2022-06-29).

* Fri Oct 01 2021 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Update to v0.9.1 (2021-09-22).

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

