%def_without doc

Name: libmmtf
Version: 1.0.0
Release: alt3

Summary: The pure C++ implementation of the MMTF API, decoder and encoder

License: MIT/X11
Group: System/Libraries
Url: https://github.com/rcsb/mmtf-cpp/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rcsb/mmtf-cpp/archive/v%version.tar.gz
Source: %name-%version.tar

ExcludeArch: armh

%if_with doc
BuildRequires: doxygen
%endif

#BuildRequires(pre): 
BuildRequires: gcc-c++ cmake
BuildRequires: libmsgpack-devel >= 2.1.5

BuildRequires: ctest catch2-devel
BuildRequires: mmtf_spec >= 1.0

%add_optflags -I%_includedir/catch2

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
# Catch have no lib
%__subst "s|Catch ||" tests/CMakeLists.txt
# fix working dir for tests
%__subst "s| COMMAND mmtf_tests|/tests COMMAND mmtf_tests|" tests/CMakeLists.txt
# use specs from package mmtf_spec
rm -rfv mmtf_spec && ln -sv %_datadir/mmtf_spec mmtf_spec

%build
%cmake_insource -DBUILD_TESTS:BOOL=ON
%make_build

%if_with doc
doxygen
%endif

%install
%makeinstall_std

%check
make test

%files devel
%doc README.md
%if_with doc
%doc doc/html
%endif
%dir %_includedir/mmtf/
%_includedir/mmtf/*.hpp
%_includedir/mmtf.hpp

%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- switch to catch2

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- ExcludeArch: armh (due libmsgpack)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

