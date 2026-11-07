%define _unpackaged_files_terminate_build 1
%def_with check

Name: dng-sdk
Version: 1.7.1.2768
Release: alt1

Summary: Adobe Digital Negative C++ software development kit
License: Adobe DNG SDK License Agreement
Group: Graphics
URL: https://helpx.adobe.com/camera-raw/digital-negative.html

Source: %name-%version.tar
Source1: DNG-CMakeLists.txt
Source2: dng-sdk.pc.in
Source3: check-dng-sdk.py
Patch: optional-xmp.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: zlib-devel
%if_with check
BuildRequires: python3-base
%endif

%description
The Adobe Digital Negative SDK reads, writes and processes DNG images.
This build includes JPEG and JPEG XL support using system libraries.
The optional XMP metadata integration is disabled.

%package -n libdng_sdk%version
Summary: Adobe DNG SDK shared library
Group: System/Libraries

%description -n libdng_sdk%version
The shared C++ library for the Adobe Digital Negative SDK.

%package -n libdng_sdk-devel
Summary: Adobe DNG SDK C++ development files
Group: Development/C++


%description -n libdng_sdk-devel
C++ headers, a shared library linker link and pkg-config metadata
for applications using the Digital Negative SDK.

%prep
%setup
%patch -p1
cp %SOURCE1 CMakeLists.txt
cp %SOURCE2 dng-sdk.pc.in

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_CXX_FLAGS="%optflags" \
    -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%if_with check
python3 %SOURCE3 %_cmake__builddir/dng_validate .
%endif

%files
%_bindir/dng_validate
%doc LICENSE.txt

%files -n libdng_sdk%version
%_libdir/libdng_sdk.so.%version

%files -n libdng_sdk-devel
%_includedir/dng-sdk
%_libdir/libdng_sdk.so
%_libdir/pkgconfig/dng-sdk.pc

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 1.7.1.2768-alt1
- Initial build for ALT.
