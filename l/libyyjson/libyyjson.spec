%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soversion 0

%def_with check

Name: libyyjson
Version: 0.9.0
Release: alt1

Summary: A high performance JSON library written in ANSI C
License: MIT
Group: System/Libraries
Url: https://github.com/ibireme/yyjson
Vcs: https://github.com/ibireme/yyjson

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
%if_with check
BuildRequires: ctest
%endif

%description
A high performance JSON library written in ANSI C.
Features
- Fast: can read or write gigabytes per second JSON data on modern CPUs.
- Portable: complies with ANSI C (C89) for cross-platform compatibility.
- Strict: complies with RFC 8259 JSON standard, ensuring strict number format
and UTF-8 validation.
- Extendable: offers options to allow comments, trailing commas, NaN/Inf, and
custom memory allocator.
- Accuracy: can accurately read and write int64, uint64, and double numbers.
- Flexible: supports unlimited JSON nesting levels, \u0000 characters, and non
null-terminated strings.
- Manipulation: supports querying and modifying using JSON Pointer, JSON Patch
and JSON Merge Patch.
- Developer-Friendly: easy integration with only one h and one c file.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soversion = %EVR

%description devel
The %name-devel package contains development files for %name.

%package -n %name%soversion
Summary: A high performance JSON library written in ANSI C
Group: System/Libraries

%description -n %name%soversion
A high performance JSON library written in ANSI C.
Features
- Fast: can read or write gigabytes per second JSON data on modern CPUs.
- Portable: complies with ANSI C (C89) for cross-platform compatibility.
- Strict: complies with RFC 8259 JSON standard, ensuring strict number format
and UTF-8 validation.
- Extendable: offers options to allow comments, trailing commas, NaN/Inf, and
custom memory allocator.
- Accuracy: can accurately read and write int64, uint64, and double numbers.
- Flexible: supports unlimited JSON nesting levels, \u0000 characters, and non
null-terminated strings.
- Manipulation: supports querying and modifying using JSON Pointer, JSON Patch
and JSON Merge Patch.
- Developer-Friendly: easy integration with only one h and one c file.

%prep
%setup

%build
%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
%if_with check
    -DYYJSON_BUILD_TESTS=ON \
%endif
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %name%soversion
%doc README.* LICENSE
%_libdir/libyyjson.so.*

%files devel
%_includedir/yyjson.h
%_libdir/libyyjson.so
%_libdir/cmake/yyjson/
%_pkgconfigdir/yyjson.pc

%changelog
* Thu May 02 2024 Denis Rastyogin <gerben@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus.
