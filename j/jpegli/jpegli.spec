%define abiversion 0.12
%define commit 031a0077f5799a6041004267fc12b956c1f52a20

Name: jpegli
Version: 0.12.0
Release: alt1

Summary: Improved JPEG encoder and decoder

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/google/jpegli
# Source-url: https://github.com/google/jpegli/archive/%commit.tar.gz
Source: %name-%version.tar
Patch0: jpegli-system-shared.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++ pkgconfig(libhwy) pkgconfig(libjpeg) pkgconfig(lcms2)
BuildRequires: /usr/bin/python3

%description
Jpegli is an improved JPEG encoder and decoder with adaptive quantization.

%package -n libjpegli%abiversion
Summary: Shared JPEG encoding and decoding library
Group: System/Libraries

%description -n libjpegli%abiversion
Jpegli provides JPEG encoding and decoding with adaptive quantization.

%package -n libjpegli-devel
Summary: Development files for jpegli
Group: Development/C++

%description -n libjpegli-devel
Headers and library for developing applications that use jpegli.

%prep
%setup
%patch0 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DJPEGLI_ENABLE_TOOLS=OFF \
    -DJPEGLI_ENABLE_DEVTOOLS=OFF \
    -DJPEGLI_ENABLE_JPEGLI_LIBJPEG=OFF \
    -DJPEGLI_ENABLE_DOXYGEN=OFF \
    -DJPEGLI_ENABLE_MANPAGES=OFF \
    -DJPEGLI_ENABLE_BENCHMARK=OFF \
    -DJPEGLI_ENABLE_JNI=OFF \
    -DJPEGLI_ENABLE_SJPEG=OFF \
    -DJPEGLI_ENABLE_OPENEXR=OFF \
    -DJPEGLI_ENABLE_TCMALLOC=OFF \
    -DJPEGLI_ENABLE_SKCMS=OFF \
    -DJPEGLI_FORCE_SYSTEM_HWY=ON \
    -DJPEGLI_FORCE_SYSTEM_LCMS2=ON \
    -DJPEGLI_LIBJPEG_LIBRARY_SOVERSION=8
%cmake_build --target jpegli

%install
%cmake_install --component native

%files -n libjpegli%abiversion
%doc LICENSE PATENTS README.md
%_libdir/libjpegli.so.%abiversion
%_libdir/libjpegli.so.%version

%files -n libjpegli-devel
%_includedir/jpegli/
%_libdir/libjpegli.so
%_pkgconfigdir/libjpegli.pc

%changelog
* Fri Nov 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- initial build for ALT Linux (git 031a0077, 2026-06-01).

