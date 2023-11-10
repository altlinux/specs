Name:     zxing-cpp
Version:  2.1.0
Release:  alt1.1

Summary:  C++ port of ZXing
License:  Apache-2.0 and LGPL-2.0 with exceptions
Group:    System/Libraries
Url:      https://github.com/nu-book/zxing-cpp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libfmt-devel
BuildRequires: libstb-devel
BuildRequires: libopencv-devel

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
%ifarch %e2k
# error #1587: cannot deduce "auto" type
sed -i '/{PointI{/s/, {/, PointI{/g;/{PointF{/s/, {/, PointF{/g' \
	core/src/ConcentricFinder.{h,cpp} \
	core/src/{aztec/AZ,qrcode/QR,datamatrix/DM}Detector.cpp
sed -E -i '/std::pair\(tl/s/\{(..), \{/std::pair{\1, PointI{/g' core/src/qrcode/QRDetector.cpp
sed -i '1i #define preferred_separator preferred_separator_zxing' test/blackbox/ZXFilesystem.h
%endif

%build
%cmake -GNinja
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc README.md example
%_libdir/libZXing.so.*

%files -n lib%name-devel
%_libdir/libZXing.so
%_includedir/ZXing/
%_libdir/cmake/ZXing/
%_libdir/pkgconfig/zxing.pc

%changelog
* Fri Nov 11 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.0-alt1.1
- Fixed build for Elbrus.

* Fri Jul 07 2023 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Fri Jan 06 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Jul 08 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Tue May 03 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Thu Feb 17 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.2.0-alt1.1
- Fixed build for Elbrus

* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
