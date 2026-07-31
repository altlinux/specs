%define _unpackaged_files_terminate_build 1
%define sover 0

%def_enable check

Name: tinycbor
Version: 7.0
Release: alt1

Summary: A tiny CBOR encoder and decoder library
License: MIT
Group: System/Libraries
URL: https://github.com/intel/tinycbor
VCS: https://github.com/intel/tinycbor.git

Source: %name-%version.tar
# upstream c2c569fbef704685ce62d45fb7b20a804f45e9f3
Patch1: %name-%version-json2cbor-install.patch
# ALT
Patch2: %name-%version-pkgconfig-abs-paths.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcjson-devel
%if_enabled check
BuildRequires: ctest
BuildRequires: qt6-base-devel
%endif

%description
TinyCBOR is a Concise Binary Object Representation (CBOR, RFC 7049) encoder
and decoder library with a small footprint, suitable for constrained
environments. It provides a streaming API that requires no dynamic memory
allocation, and optional conversion between CBOR and JSON.

%package -n libtinycbor%sover
Summary: A tiny CBOR encoder and decoder library
Group: System/Libraries

%description -n libtinycbor%sover
TinyCBOR is a Concise Binary Object Representation (CBOR, RFC 7049) encoder
and decoder library with a small footprint.

This package contains the runtime library needed to run software using
TinyCBOR.

%package -n libtinycbor-devel
Summary: Development files for TinyCBOR
Group: Development/C
Requires: libtinycbor%sover = %EVR

%description -n libtinycbor-devel
This package contains the header files, the pkg-config description and the
cmake package configuration needed to build software using TinyCBOR.

%package tools
Summary: Command-line tools for CBOR data
Group: Development/Tools
Requires: libtinycbor%sover = %EVR

%description tools
Utilities built on top of TinyCBOR: cbordump converts CBOR to a human-readable
form, json2cbor converts JSON documents to CBOR.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=%{?_enable_check:ON}%{?!_enable_check:OFF} \
    -DBUILD_TOOLS=ON \
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libtinycbor%sover
%doc README LICENSE
%_libdir/libtinycbor.so.%sover
%_libdir/libtinycbor.so.%sover.*

%files -n libtinycbor-devel
%_includedir/tinycbor/
%_libdir/libtinycbor.so
%_pkgconfigdir/tinycbor.pc
%_cmakedir/tinycbor/

%files tools
%_bindir/cbordump
%_bindir/json2cbor

%changelog
* Fri Jul 31 2026 Aleksandr Voyt <sobue@altlinux.org> 7.0-alt1
- Initial build.
