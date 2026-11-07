%define _unpackaged_files_terminate_build 1
%def_with check

Name: piex
Version: 0.27
Release: alt1

Summary: RAW preview image extractor C++ development kit
License: Apache-2.0
Group: Development/C++
URL: https://github.com/google/piex
VCS: https://github.com/google/piex.git

Source: %name-%version.tar
Source1: PIEX-CMakeLists.txt
Source2: piex.pc.in
Source3: piex-test.cc
Patch: cstring.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: pkg-config
%if_with check
BuildRequires: ctest
%endif

%description
PIEX finds JPEG preview images and image metadata in digital camera RAW
files. The source builds the shared library and C++ development files.

%package -n libpiex%version
Summary: Preview Image Extractor shared library
Group: System/Libraries

%description -n libpiex%version
The shared C++ library for extracting previews from camera RAW files.

%package -n lib%name-devel
Summary: Preview Image Extractor C++ development files
Group: Development/C++

%description -n lib%name-devel
C++ headers, shared library linker link and pkg-config metadata for PIEX.

%prep
%setup
%patch -p1
cp %SOURCE1 CMakeLists.txt
cp %SOURCE2 piex.pc.in
cp %SOURCE3 piex-test.cc

%build
%if_with check
piex_build_testing=ON
%else
piex_build_testing=OFF
%endif
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_CXX_FLAGS="%optflags" \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING="$piex_build_testing"
%cmake_build

%install
%cmake_install

%check
%if_with check
%ctest --no-tests=error
%endif

%files -n libpiex%version
%_libdir/libpiex.so.%version
%doc LICENSE

%files -n lib%name-devel
%_includedir/piex
%_libdir/libpiex.so
%_libdir/pkgconfig/piex.pc

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.27-alt1
- Initial build for ALT.
