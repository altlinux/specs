%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with check

%define soversion 0.12

Name: libcbor
Version: %soversion.0
Release: alt1

Summary: A C library for parsing and generating CBOR
License: MIT
Group: System/Libraries
Url: https://github.com/pjk/libcbor
Vcs: https://github.com/pjk/libcbor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: sphinx
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-breathe
BuildRequires: doxygen
%if_with check
BuildRequires: ctest
BuildRequires: libcmocka-devel
%endif

%description
libcbor is a C library for parsing and generating CBOR,
the general-purpose schema-less binary data format.
See more information: https://datatracker.ietf.org/doc/html/rfc7049.

%package -n %name%soversion
Summary: Shared library for libcbor C library
Group: System/Libraries

%description -n %name%soversion
Shared libraries files for libcbor - a C library for parsing and
generating CBOR, the general-purpose schema-less binary data format.

%package devel
Summary: Development header files for libcbor C library
Group: Development/C
Requires: %name%soversion = %EVR

%description devel
Development header file for libcbor - a C library for parsing and
generating CBOR, the general-purpose schema-less binary data format.

%prep
%setup

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_EXAMPLES=ON \
%if_with check
    -DWITH_TESTS=ON \
%endif
    %nil
%cmake_build

make SPHINXBUILD="sphinx-build-3" BUILDDIR=. -C doc man

%install
%cmake_install

install -pD -m0644 doc/man/libcbor.3 %buildroot/%_man3dir/libcbor.3

%check
%ctest

%files -n %name%soversion
%_libdir/libcbor.so.%soversion
%_libdir/libcbor.so.%soversion.*

%files devel
%doc CHANGELOG.md LICENSE.md README.md
%_includedir/cbor.h
%_includedir/cbor/
%_libdir/libcbor.so
%_pkgconfigdir/libcbor.pc
%_cmakedir/libcbor/
%_man3dir/libcbor.3*

%changelog
* Fri Mar 28 2025 Anton Zhukharev <ancieg@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0.
- Enabled check during building.
- Followed Shared Libs policy.

* Wed Feb 21 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Updated 0.11.0.

* Sat Mar 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt1
- 0.10.1 -> 0.10.2.

* Sat Jan 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- 0.10.1
- follow sharedlib policy
- fix url in description

* Sat Aug 27 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt2
- add strict ELF verification

* Wed May 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus
