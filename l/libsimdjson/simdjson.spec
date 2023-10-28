# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libsimdjson
Version: 3.5.0
Release: alt1
Summary: Parsing gigabytes of JSON per second
License: Apache-2.0
Group: System/Libraries
Url: https://simdjson.org/
Vcs: https://github.com/simdjson/simdjson

Source: %name-%version.tar
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

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
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
