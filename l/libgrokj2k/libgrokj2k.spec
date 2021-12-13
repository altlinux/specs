# TODO: enable tests (they forget pack tests in the tarball)
%define oname grok

Name: libgrokj2k
Version: 9.5.0
Release: alt1

Summary: World's Leading Open Source JPEG 2000 Codec
License: AGPL-3.0
Group: System/Libraries

Url: https://github.com/GrokImageCompression/grok

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/GrokImageCompression/grok/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: perl-base perl-devel perl-Image-ExifTool
BuildRequires: zlib-devel libpng-devel libtiff-devel liblcms2-devel libjpeg-devel
# don't checked by cmake??
BuildRequires: libwebp-devel libzstd-devel liblzma-devel libjbig-devel libdeflate-devel

BuildRequires: cmake gcc-c++
BuildRequires(pre): rpm-macros-cmake

%description
World's Leading Open Source JPEG 2000 Codec:
support for new High Throughput JPEG 2000 (HTJ2K) standard
fast random-access sub-image decoding using TLM and PLT markers
full encode/decode support for ICC colour profiles
full encode/decode support for XML,IPTC, XMP and EXIF meta-data
full encode/decode support for monochrome, sRGB, palette, YCC, extended YCC, CIELab and CMYK colour spaces
full encode/decode support for JPEG,PNG,BMP,TIFF,RAW,PNM and PAM image formats
full encode/decode support for 1-16 bit precision images


%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Header files for %name.

%package -n grokj2k-tools
Summary: Tools for %name
Group: File tools
Requires: %name = %EVR

%description -n grokj2k-tools
Compress and decompress tools for grokj2k:
* grk_compress
* grk_decompress

%prep
%setup
%ifarch %e2k
sed -i 's|set(CMAKE_CXX_STANDARD 20)|string(APPEND CMAKE_CXX_FLAGS " -std=gnu++2a")|' src/{bin,lib}/jp2/CMakeLists.txt
%add_optflags -mno-sse
%endif
%ifarch ppc64le
%add_optflags -DNO_WARN_X86_INTRINSICS
%endif

%build
%cmake_insource \
        -DBUILD_STATIC_LIBS=OFF \
        -DGRK_USE_LIBJPEG=ON \
        -DHWY_SYSTEM_GTEST=ON \
        -DBUILD_TESTING=OFF \
        %nil
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_libdir/lib*.so.*

%files -n grokj2k-tools
%_bindir/grk_compress
%_bindir/grk_decompress
%_bindir/grk_dump

%files devel
%_libdir/lib*.so
%_includedir/*/
%_libdir/cmake/*/
%_pkgconfigdir/*

%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 9.5.0-alt1
- new version 9.5.0 (with rpmrb script)
- add BR: libdeflate-devel
- add -DNO_WARN_X86_INTRINSICS for ppc64le

* Tue Sep 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.2.0-alt2
- fixed build for Elbrus

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 9.2.0-alt1
- initial build for ALT Sisyphus

