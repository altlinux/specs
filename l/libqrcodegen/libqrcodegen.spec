%global richname QR-Code-generator
%global cmakename qrcodegen-cmake
%global cmakesuffix cmake2

Name: libqrcodegen
Version: 1.8.0
Release: alt1

Summary: High-quality QR Code generator library

License: MIT
Group: System/Libraries
Url: https://github.com/nayuki/QR-Code-generator
VCS: https://github.com/nayuki/QR-Code-generator.git

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar
# Source1-url: https://github.com/EasyCoding/%cmakename/archive/v%version-%cmakesuffix/%cmakename-%version-%cmakesuffix.tar.gz
Source1: %cmakename-%version-%cmakesuffix.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: python3-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: ctest
BuildRequires: python3-module-setuptools
# for setuptools < 70.1.0
BuildRequires: python3-module-wheel

%description
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package devel
Group: Development/C
Summary: Development files for libqrcodegen
Requires: libqrcodegen = %EVR

%description devel
Development files and headers for high-quality QR Code generator library
(plain C version).

%package -n libqrcodegen-cpp
Group: System/Libraries
Summary: High-quality QR Code generator library (C++ version)

%description -n libqrcodegen-cpp
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen-cpp-devel
Group: Development/C++
Summary: Development files for libqrcodegencpp
Requires: libqrcodegen-cpp = %EVR

%description -n libqrcodegen-cpp-devel
Development files and headers for high-quality QR Code generator library
(C++ version).

%package -n python3-module-qrcodegen
Group: Development/Python
Summary: High-quality QR Code generator library (Python version)
BuildArch: noarch

%description -n python3-module-qrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%prep
%setup
# Unpacking CMake build script and assets...
tar -xf %SOURCE1 %cmakename-%version-%cmakesuffix/cmake \
	%cmakename-%version-%cmakesuffix/CMakeLists.txt --strip=1
 
%autopatch1 -p1

%build
# Building C and C++ versions...
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS=ON \
    -DBUILD_SHARED_LIBS=true

%cmake_build

# Building Python version...
pushd python
%pyproject_build
popd

%install
# Installing C and C++ versions...
%cmake_install

# Installing Python version...
pushd python
%pyproject_install
popd
	
# Installing a legacy symlink for compatibility...
ln -s qrcodegen.hpp %buildroot%_includedir/qrcodegencpp/QrCode.hpp

%files
%doc Readme.markdown
%_libdir/libqrcodegen.so.1*

%files devel
%_includedir/qrcodegen/
%_libdir/cmake/qrcodegen/
%_libdir/libqrcodegen.so
%_libdir/pkgconfig/qrcodegen.pc

%files -n libqrcodegen-cpp
%doc Readme.markdown
%_libdir/libqrcodegencpp.so.1*

%files -n libqrcodegen-cpp-devel
%_includedir/qrcodegencpp/
%_libdir/cmake/qrcodegencpp/
%_libdir/libqrcodegencpp.so
%_libdir/pkgconfig/qrcodegencpp.pc

%files -n python3-module-qrcodegen
%doc Readme.markdown
%python3_sitelibdir_noarch/qrcodegen.py
%python3_sitelibdir_noarch/__pycache__/*
%python3_sitelibdir_noarch/qrcodegen-%version.dist-info/

%changelog
* Mon Mar 3 2025 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- new version (1.8.0) with rpmgs script
- build with cmake

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1.git67c6246
- initial build for ALT Sisyphus

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1.20191014git67c6246
- Initial SPEC release.
