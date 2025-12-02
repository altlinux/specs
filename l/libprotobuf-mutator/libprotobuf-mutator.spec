%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name: libprotobuf-mutator
Version: 1.5
Release: alt1

Summary: Library for structured fuzzing with protobuffers
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/google/libprotobuf-mutator
Vcs: https://github.com/google/libprotobuf-mutator.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libexpat-devel
BuildRequires: libxml2-devel
BuildRequires: gcc-c++
BuildRequires: cmake-modules
BuildRequires: libprotobuf-devel
BuildRequires: liblzma-devel
BuildRequires: libgtest-devel
BuildRequires: ctest

%description
Libprotobuf-mutator is a library for structured fuzzing with Protocol Buffers.
It allows generating random protobuf messages for fuzzing purposes and mutating
them to improve code coverage. This library is particularly useful for fuzzing
applications that use protobuf for data serialization.

%package -n libprotobuf-mutator%abiversion
Summary: Core library for structured fuzzing with Protocol Buffers
Group: Development/Tools

%description -n libprotobuf-mutator%abiversion
Core shared library for libprotobuf-mutator.

%package libfuzzer%abiversion
Summary: LibFuzzer integration for libprotobuf-mutator
Group: Development/Tools

%description libfuzzer%abiversion
This package contains the LibFuzzer integration library for
libprotobuf-mutator.  It provides mutators for use with LibFuzzer and other
fuzzing engines.

%package devel
Summary: Development files for libprotobuf-mutator
Group: Development/C++

%description devel
This package contains header files and development tools for
libprotobuf-mutator, a library for structured fuzzing with Protocol Buffers.
Install this package if you want to develop applications using
libprotobuf-mutator.

%prep
%setup
%autopatch -p1

%cmake \
  -DCMAKE_CXX_FLAGS:STRING="%optflags -frecord-gcc-switches -flto=auto -ffat-lto-objects" \
  -DProtobuf_IMPORT_DIRS=%_includedir \
  -DPKG_CONFIG_PATH=%_pkgconfigdir \
  -DBUILD_SHARED_LIBS=ON \
  #

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libprotobuf-mutator%abiversion
%_libdir/libprotobuf-mutator.so.%abiversion

%files libfuzzer%abiversion
%_libdir/libprotobuf-mutator-libfuzzer.so.%abiversion

%files devel
%_libdir/libprotobuf-mutator.so
%_libdir/libprotobuf-mutator-libfuzzer.so
%_includedir/libprotobuf-mutator
%_libexecdir/cmake/libprotobuf-mutator
%_pkgconfigdir/libprotobuf-mutator.pc

%changelog
* Tue Dec 02 2025 Ivan Khanas <xeno@altlinux.org> 1.5-alt1
- First build for ALT.
