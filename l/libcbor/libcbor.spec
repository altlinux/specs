%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libcbor
Version: 0.10.2
Release: alt1

Summary: libcbor is a C library for parsing and generating CBOR
License: MIT
Group: System/Libraries
Url: https://github.com/pjk/libcbor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: sphinx
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-breathe
BuildRequires: doxygen

%description
libcbor is a C library for parsing and generating CBOR (see more
information: https://datatracker.ietf.org/doc/html/rfc7049),
the general-purpose schema-less binary data format.

%package devel
Summary: Development header files for libcbor C library
Group: Development/C
Requires: %name = %EVR

%description devel
Development header file for libcbor - a C library for parsing and generating
CBOR, the general-purpose schema-less binary data format.

%prep
%setup

%build
%cmake -DCBOR_CUSTOM_ALLOC=ON -DBUILD_SHARED_LIBS=ON
%cmake_build

make SPHINXBUILD="sphinx-build-3" BUILDDIR=. -C doc man

%install
%cmake_install

install -pD -m0644 doc/man/libcbor.3 %buildroot/%_man3dir/libcbor.3

%files
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.md README.md
%_libdir/%name.so.*

%files devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.md README.md
%_includedir/cbor*
%_libdir/%name.so
%_libdir/pkgconfig/*
%_man3dir/*

%changelog
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
