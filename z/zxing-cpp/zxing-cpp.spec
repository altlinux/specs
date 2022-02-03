Name:     zxing-cpp
Version:  1.2.0
Release:  alt1

Summary:  C++ port of ZXing
License:  Apache-2.0 and LGPL-2.0 with exceptions
Group:    System/Libraries
Url:      https://github.com/nu-book/zxing-cpp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
# Update stb_image/stb_image_write
# https://github.com/nu-book/zxing-cpp/pull/269
# Fixes CVE-2021-28021, CVE-2021-42715, and CVE-2021-42716, and adds a patch
# file for zxing-cpp-specific changes
Patch1: 269.patch
Patch2: 0001-Add-a-mode-to-build-against-system-versions-of-depen.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libfmt-devel

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode
image processing library implemented in C++. It was originally ported from the
Java ZXing Library but has been developed further and now includes many
improvements in terms of quality and performance. It can both read and write
barcodes in a number of formats.

%package -n lib%name
Summary: C++ port of ZXing
Group: System/Libraries

%description -n lib%name
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode
image processing library implemented in C++. It was originally ported from the
Java ZXing Library but has been developed further and now includes many
improvements in terms of quality and performance. It can both read and write
barcodes in a number of formats.

%package -n lib%name-devel
Summary: C++ port of ZXing (development files)
Group: Development/C++

%description -n lib%name-devel
Development files for lib%name.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake -GNinja
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS.ZXing LGPL_EXCEPTION.Qt LICENSE* NOTICE README.md
%_libdir/libZXing.so.*

%files -n lib%name-devel
%_libdir/libZXing.so
%_includedir/ZXing/
%_libdir/cmake/ZXing/
%_libdir/pkgconfig/zxing.pc

%changelog
* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
