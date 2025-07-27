%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qzxing
Version: 3.3.0
Release: alt1

Summary: QZXing library
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/ftylitak/qzxing

Source: %name-%version.tar

# sync with version 3.3.0+dfsg-7 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: ctest

%description
Qt/QML wrapper library for the ZXing bar-code image processing library.

%package -n lib%{name}
Group: System/Libraries
Summary: QZXing library

%description -n lib%{name}
Qt wrapper for the ZXing 1D/2D barcode image decoder.

Supports barcode decoding for the following types:

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- ITF
- Code 39
- Code 93
- Code 128 (GS1)
- Codabar
- QR Code
- Data Matrix
- Aztec (beta)
- PDF 417

Supports barcode encoding for the following types:

- QR Code

This package contains the shared library files.

%package -n lib%{name}-devel
Group: Development/KDE and QT
Summary: QZXing library (development headers)
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Qt wrapper for the ZXing 1D/2D barcode image decoder.

Supports barcode decoding for the following types:

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- ITF
- Code 39
- Code 93
- Code 128 (GS1)
- Codabar
- QR Code
- Data Matrix
- Aztec (beta)
- PDF 417

Supports barcode encoding for the following types:

- QR Code

This package contains the development header files of the QZXing shared
library.

%prep
%setup
%patch -p1

%build
%cmake ./src \
       -DBUILD_SHARED=ON \
       -DQZXING_MULTIMEDIA=ON \
       -DQZXING_USE_QML=ON \
       -DQZXING_USE_ENCODER=ON \
       -DQZXING_MULTIMEDIA=ON \
       -DQZXING_USE_QML=ON \
       -DQZXING_USE_ENCODER=ON \
       -DQZXING_USE_DECODER_QR_CODE=ON \
       -DQZXING_USE_DECODER_1D_BARCODES=ON \
       -DQZXING_USE_DECODER_DATA_MATRIX=ON \
       -DQZXING_USE_DECODER_AZTEC=ON \
       -DQZXING_USE_DECODER_PDF17=ON \
       -DQZXING_USE_DECODER_1D_BARCODES=ON
%cmake_build

%install
%cmake_install

%files -n lib%{name}
%doc LICENSE README.md examples
%_libdir/libqzxing.so.3*

%files -n lib%{name}-devel
%dir %_includedir/qzxing/
%_includedir/qzxing/QZXing.h
%_includedir/qzxing/QZXing_global.h
%_includedir/qzxing/QZXingFilter.h
%_includedir/qzxing/QZXingImageProvider.h
%_libdir/pkgconfig/QZXing.pc
%_libdir/libqzxing.so

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus
