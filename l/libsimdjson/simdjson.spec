# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libsimdjson
Version: 3.9.2
Release: alt1
Summary: Parsing gigabytes of JSON per second
License: Apache-2.0
Group: System/Libraries
Url: https://simdjson.org/
Vcs: https://github.com/simdjson/simdjson

Source: %name-%version.tar
Patch: simdjson-loongarch-link-flags.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available SIMD
instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
%summary

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
grep -P '^#define\s+SIMDJSON_VERSION\s+"\Q%version\E"' %buildroot%_includedir/simdjson.h
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir
c++ -Iinclude examples/quickstart/quickstart.cpp -L%_cmake__builddir -lsimdjson
cd jsonexamples
../a.out

%files
%doc LICENSE
%_libdir/libsimdjson.so.*

%files devel
%doc AUTHORS CONTRIBUTORS *.md
%_includedir/simdjson.h
%_libdir/libsimdjson.so
%_libdir/cmake/simdjson
%_pkgconfigdir/simdjson.pc

%changelog
* Wed May 29 2024 Vitaly Chikunov <vt@altlinux.org> 3.9.2-alt1
- Update to v3.9.2 (2024-05-07).

* Sat Apr 13 2024 Ivan A. Melnikov <iv@altlinux.org> 3.9.1-alt1.1
- NMU: Fix FTBFS on loongarch64.

* Fri Apr 12 2024 Vitaly Chikunov <vt@altlinux.org> 3.9.1-alt1
- Update to v3.9.1 (2024-04-05).

* Sat Feb 10 2024 Vitaly Chikunov <vt@altlinux.org> 3.6.4-alt1
- Update to v3.6.4 (2024-01-29).

* Sun Dec 24 2023 Vitaly Chikunov <vt@altlinux.org> 3.6.3-alt1
- Update to v3.6.3 (2023-12-08).

* Sat Dec 02 2023 Vitaly Chikunov <vt@altlinux.org> 3.6.2-alt1
- Update to v3.6.2 (2023-12-01).

* Sun Oct 29 2023 Vitaly Chikunov <vt@altlinux.org> 3.5.0-alt1
- Update to v3.5.0 (2023-10-27).

* Thu Sep 21 2023 Vitaly Chikunov <vt@altlinux.org> 3.3.0-alt1
- Update to v3.3.0 (2023-09-20).

* Sat Aug 26 2023 Vitaly Chikunov <vt@altlinux.org> 3.2.3-alt1
- Update to v3.2.3 (2023-08-22).

* Mon Aug 07 2023 Vitaly Chikunov <vt@altlinux.org> 3.2.2-alt1
- Update to v3.2.2 (2023-08-02).

* Sun Jul 09 2023 Vitaly Chikunov <vt@altlinux.org> 3.2.1-alt1
- Update to v3.2.1 (2023-07-06).

* Fri Jun 16 2023 Vitaly Chikunov <vt@altlinux.org> 3.2.0-alt1
- Update to v3.2.0 (2023-06-15).

* Sun May 28 2023 Vitaly Chikunov <vt@altlinux.org> 3.1.8-alt1
- Update to v3.1.8 (2023-05-14).

* Tue May 09 2023 Vitaly Chikunov <vt@altlinux.org> 3.1.7-alt1
- First import v3.1.7 (2023-04-08).
