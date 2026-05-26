%define _unpackaged_files_terminate_build 1

%def_with check

Name:    protozero
Version: 1.8.1
Release: alt1

Summary: Minimalist protocol buffer decoder and encoder in C++
License: BSD-2-Clause
Group:   System/Libraries
URL:     https://github.com/mapbox/protozero
VCS:     https://github.com/mapbox/protozero

Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: ctest
%endif

%description
Minimalistic protocol buffer decoder and encoder in C++.

Designed for high performance. Suitable for writing zero copy parsers
and encoders with minimal need for run-time allocation of memory.

Low-level: this is designed to be a building block for writing a
very customized decoder for a stable protobuf schema. If your protobuf
schema is changing frequently or lazy decoding is not critical for your
application then this approach offers no value: just use the decoding
API available via the C++ API that can be generated via the Google
Protobufs protoc program.

%package devel
Group: Development/C++
Summary: Minimalist protocol buffer decoder and encoder in C++

%description devel
%{description %name}

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%_includedir/protozero

%changelog
* Mon May 25 2026 Alexey Volkov <qualimock@altlinux.org> 1.8.1-alt1
- Initial build for ALT
