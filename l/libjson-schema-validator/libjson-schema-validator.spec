%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: libjson-schema-validator
Version: 2.4.0
Release: alt1

Summary: JSON schema validator for JSON for Modern C++
License: MIT
Group: System/Libraries
Url: https://github.com/pboettch/json-schema-validator

Source: %name-%version.tar

# sync with version 2.4.0-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(nlohmann_json)

%if_with check
BuildRequires: ctest
%endif

%description
This is a C++ library for validating JSON documents based on a
JSON Schema which itself should validate with draft-7 of JSON Schema
Validation.

This package contains the shared library.

%package devel
Group: Development/C++
Summary: json schema validation library (development files)
Requires: %name = %{version}-%{release}

%description devel
This is a C++ library for validating JSON documents based on a
JSON Schema which itself should validate with draft-7 of JSON Schema
Validation.

This package is needed to compile programs against
libjson-schema-validator.

%prep
%setup
%patch -p1

%build
%cmake \
       -DBUILD_SHARED_LIBS=ON \
       -DJSON_VALIDATOR_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%check
%ifnarch aarch64 riscv64
%ctest
%else
%ctest -E "JSON-Suite::Optional::Format::idn-email"
%endif

%files
%doc LICENSE README.md
%_libdir/libnlohmann_json_schema_validator.so.*

%files devel
%doc example
%_libdir/libnlohmann_json_schema_validator.so
%dir %_includedir/nlohmann
%_includedir/nlohmann/json-schema.hpp
%dir %_libdir/cmake/nlohmann_json_schema_validator
%_libdir/cmake/nlohmann_json_schema_validator/*

%changelog
* Sat Jul 04 2026 Nikolay Strelkov <snk@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus
