%define _unpackaged_files_terminate_build 1
%def_with check

Name: skia
Version: 157
Release: alt1

Summary: Skia graphics and text shaping C++ development kit
License: BSD-3-Clause AND Apache-2.0
Group: Development/C++
URL: https://github.com/JetBrains/skia
VCS: https://github.com/JetBrains/skia.git

Source: %name-%version.tar
Source1: build-sdk.py
Source2: skia.pc.in
Patch: system-libraries.patch
Patch1: fp-contract.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: gn
BuildRequires: ninja-build
BuildRequires: pkg-config
BuildRequires: python3-base
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libicu-devel
BuildRequires: libexpat-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel
BuildRequires: zlib-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel
BuildRequires: libvulkan-devel
BuildRequires: vulkan-headers
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: pkgconfig(dng-sdk)
BuildRequires: pkgconfig(piex)
BuildRequires: pkgconfig(wuffs)
BuildRequires: libspirv-tools-devel
%if_with check
BuildRequires: fonts-ttf-dejavu
BuildRequires: libGLU-devel
%endif

%description
Skia is a graphics library for raster drawing, images, fonts and text
shaping. The complete Linux SDK includes SkParagraph, SkShaper, SkUnicode,
Skottie, SVG and their supporting modules.

%package -n libskia%version
Summary: Skia shared graphics and text shaping libraries
Group: System/Libraries

%description -n libskia%version
Shared Skia libraries and all SDK modules for this upstream milestone.

%package -n libskia-devel
Summary: Skia C++ development files
Group: Development/C++

%description -n libskia-devel
Skia C++ headers, shared library linker links and pkg-config metadata.

%prep
%setup
%patch -p1
%patch1 -p1
cp %SOURCE2 skia.pc.in

%build
python3 %SOURCE1 build --version %version --jobs %__nprocs \
    --optflags="%optflags"
%if_with check
python3 %SOURCE1 build-tests --jobs %__nprocs --optflags="%optflags"
%endif

%install
python3 %SOURCE1 install --destdir %buildroot --prefix %_prefix \
    --libdir %_libdir --includedir %_includedir \
    --docdir %_docdir/%name-%version

%check
%if_with check
python3 %SOURCE1 check --jobs %__nprocs
%endif

%files -n libskia%version
%_libdir/libskia*.so.%version
%doc %_docdir/%name-%version

%files -n libskia-devel
%_includedir/skia
%_libdir/libskia*.so
%_libdir/pkgconfig/skia.pc

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 157-alt1
- Initial build for ALT.
