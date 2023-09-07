# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: capnproto
Version: 1.0.1
Release: alt1
Summary: A data interchange format and capability-based RPC system
Group: Development/C
License: MIT
Url: https://capnproto.org
Vcs: https://github.com/capnproto/capnproto
Requires: libcapnp = %EVR

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

%package -n libcapnp
Summary: Shared libraries for %name
Group: System/Libraries
Obsoletes: capnproto-libs < %EVR

%description -n libcapnp
The libcapnp package contains the libraries for using Cap'n Proto
in applications.

# Two step rename to libcapnp-devel because of BR and unmets at the same time.
# When there is capnproto-devel and libcapnp-devel at the same time apt will
# install capnproto-devel.
%package devel
Summary: Development files for %name
Group: Development/C
Provides: libcapnp-devel = %EVR
Requires: capnproto = %EVR
Requires: libcapnp = %EVR

%description devel
This package contains libraries and header files for developing applications
that use Cap'n Proto.

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
# Disable LTO: https://github.com/capnproto/capnproto/issues/1660
%define optflags_lto %nil
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

%files -n libcapnp
%doc LICENSE CONTRIBUTORS README.md
%_libdir/*-%version.so

%files devel
%doc c++/LICENSE.txt c++/README.txt doc/*md kjdoc/tour.md
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/cmake/CapnProto
%exclude %_libdir/*-%version.so
%_libdir/lib*.so

%changelog
* Thu Sep 07 2023 Vitaly Chikunov <vt@altlinux.org> 1.0.1-alt1
- Update to v1.0.1 (2023-08-22).

* Tue Aug 01 2023 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- Update to v1.0.0 (2023-07-28).
- New package names: capnproto-libs -> libcapnp, capnproto-devel =
  libcapnp-devel.

* Tue Apr 18 2023 Vitaly Chikunov <vt@altlinux.org> 0.10.4-alt1
- Update to v0.10.4 (2023-04-13).
- spec: Disable LTO build (issues/1660).

* Thu Dec 01 2022 Vitaly Chikunov <vt@altlinux.org> 0.10.3-alt1
- Update to v0.10.3 (2022-11-29).

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

