%define _unpackaged_files_terminate_build 1
%define abiversion 119

Name: libSkiaSharp
Version: 3.119.4
Release: alt1

Summary: Native SkiaSharp graphics library for Skia milestone 119

License: BSD-3-Clause AND MIT
Group: System/Libraries
URL: https://github.com/mono/SkiaSharp
VCS: https://github.com/mono/skia.git
# mono/skia commit pinned by SkiaSharp v3.119.4, not current main.
# Source-url: https://github.com/mono/skia/archive/7dbfc07dd33181f84e0958afb7ee805c6c769f0b.tar.gz
Source: %name-%version.tar
Source1: libSkiaSharp.map
Source2: build-native.py
Source3: check-native.py
Source4: native-symbols.txt
Patch: system-libraries.patch
Patch1: dng-sdk-api.patch

BuildRequires: gcc-c++ gn ninja-build python3-base pkg-config
BuildRequires: fontconfig-devel libfreetype-devel libexpat-devel
BuildRequires: libjpeg-devel libpng-devel libwebp-devel zlib-devel
BuildRequires: libglvnd-devel libvulkan-devel vulkan-headers
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: pkgconfig(dng-sdk) pkgconfig(piex) pkgconfig(wuffs)

%description
SkiaSharp is a 2D graphics API for .NET. This package provides its native
C API from the mono/skia fork, compatible with the SkiaSharp 3.119 line.
The native library is built from source using system graphics, font and
image libraries.

%package -n libSkiaSharp-devel
Summary: C headers and linker symlink for the SkiaSharp native library
Group: Development/C

%description -n libSkiaSharp-devel
C API headers and linker symlink for the milestone 119 native library.

%prep
%setup
%patch -p1
%patch1 -p1
cp %SOURCE1 libSkiaSharp.map

%build
python3 %SOURCE2 --jobs %__nprocs --optflags="%optflags"

%install
install -Dm755 out/RPM/libSkiaSharp.so.%abiversion.0.0 \
    %buildroot%_libdir/libSkiaSharp.so.%abiversion.0.0
ln -s libSkiaSharp.so.%abiversion.0.0 %buildroot%_libdir/libSkiaSharp.so
mkdir -p %buildroot%_includedir/SkiaSharp/include
cp -a include/c %buildroot%_includedir/SkiaSharp/include/

%check
python3 %SOURCE3 ./out/RPM/libSkiaSharp.so.%abiversion.0.0 %SOURCE4

%files
%_libdir/libSkiaSharp.so.%abiversion.0.0
%doc LICENSE

%files -n libSkiaSharp-devel
%_includedir/SkiaSharp
%_libdir/libSkiaSharp.so

%changelog
* Fri Nov 13 2026 Vitaly Lipatov <lav@altlinux.ru> 3.119.4-alt1
- initial build for Sisyphus.

