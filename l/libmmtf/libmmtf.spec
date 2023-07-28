%def_without doc

Name: libmmtf
Version: 1.1.0
Release: alt1

Summary: The pure C++ implementation of the MMTF API, decoder and encoder

License: MIT
Group: System/Libraries
Url: https://github.com/rcsb/mmtf-cpp/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rcsb/mmtf-cpp/archive/v%version.tar.gz
Source: %name-%version.tar

ExcludeArch: armh

%if_with doc
BuildRequires: doxygen
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake

BuildRequires: msgpack-cxx-devel

BuildRequires: ctest catch2-devel
BuildRequires: mmtf_spec >= 1.0

%description
The pure C++ implementation of the MMTF API, decoder and encoder.
The macromolecular transmission format (MMTF) is a binary encoding of biological structures.

%package devel
Summary: Header files for the %name library
Group: Development/C++

%description devel
Header files for the %name library.

%prep
%setup
%__subst "s|.*INTERFACE msgpackc.*||" CMakeLists.txt
%__subst "s|Catch msgpackc | |" tests/CMakeLists.txt
%__subst 's|#include "catch.hpp"|#include <catch2/catch.hpp>|' tests/mmtf_tests.cpp
# fix working dir for tests
#__subst "s| COMMAND mmtf_tests|/tests COMMAND mmtf_tests|" tests/CMakeLists.txt
# use specs from package mmtf_spec
rm -rfv submodules/mmtf_spec && ln -sv %_datadir/mmtf_spec submodules/mmtf_spec

%build
%cmake_insource \
    -DBUILD_TESTS:BOOL=ON
%make_build

%if_with doc
doxygen
%endif

%install
%makeinstall_std

%check
#make test
cd tests
./mmtf_tests
./multi_cpp_test

%files devel
%doc README.md
%if_with doc
%doc doc/html
%endif
%dir %_includedir/mmtf/
%_includedir/mmtf/*.hpp
%_includedir/mmtf.hpp

%changelog
* Thu Jul 27 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)
- fix build with catch2-devel
- build with msgpack-cxx-devel

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- switch to catch2

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- ExcludeArch: armh (due libmsgpack)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

