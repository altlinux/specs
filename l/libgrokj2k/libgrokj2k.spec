%define oname grok

Name: libgrokj2k
Version: 20.4.20
Release: alt1

Summary: World's Leading Open Source JPEG 2000 Codec
License: AGPL-3.0
Group: System/Libraries

Url: https://github.com/GrokImageCompression/grok

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/GrokImageCompression/grok/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# spdlog 2.0.0 used as git submodule src/include/spdlog
# from https://github.com/gabime/spdlog/tree/ce0424bb375805955c0c5482a32ddb821708eb47
Source2: spdlog-2.0.0.tar
Patch0: grok-use-system-highway.patch
Patch1: grok-tests-mapped-offset-64bit.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: perl-base perl-devel perl-Image-ExifTool
BuildRequires: zlib-devel libpng-devel libtiff-devel liblcms2-devel libjpeg-devel
BuildRequires: libwebp-devel libzstd-devel liblzma-devel libdeflate-devel cli11-devel
BuildRequires: libfmt-devel highway-devel libtaskflow-devel >= 4.1.0-alt2

BuildRequires: rpm-build-cmake ctest gcc-c++

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
* grk_transcode

%prep
%setup -a2
%patch0 -p1
%patch1 -p1
%ifarch %e2k
sed -i 's|set(CMAKE_CXX_STANDARD 20)|string(APPEND CMAKE_CXX_FLAGS " -std=gnu++2a")|' CMakeLists.txt
sed -i 's|CMAKE_CXX_COMPILER_VERSION|12.0|' CMakeLists.txt
%add_optflags -mno-sse
%endif
%ifarch ppc64le
%add_optflags -DNO_WARN_X86_INTRINSICS
%endif

rm -rv thirdparty/liblcms2
rm -rf thirdparty/libpng
rm -rf thirdparty/libtiff
rm -rf thirdparty/libz

%build
%cmake_insource \
        -DBUILD_STATIC_LIBS=OFF \
        -DGRK_BUILD_LIBPNG=OFF \
        -DGRK_BUILD_LIBTIFF=OFF \
        -DGRK_BUILD_LCMS2=OFF \
        -DGRK_BUILD_JPEG=OFF \
        -DBUILD_TESTING=ON \
        -DGRK_USE_SYSTEM_HIGHWAY=ON \
        -DSPDLOG_FMT_EXTERNAL=ON \
        %nil
%make_build

%install
%makeinstall_std

%check
# NR-* (nonregression) and ETS-* (conformance) tests need the separate
# grok-test-data repository, so only self-contained tests are run
exclude='^(NR|ETS)-'
# re-executes itself via /proc/self/exe, which needs /proc
[ -e /proc/self/exe ] || exclude="$exclude|^grk_region_component_memory_test$"
ctest --output-on-failure -j%__nprocs -E "$exclude"

%files
%doc README.md
%_libdir/%name.so.1
%_libdir/%name.so.%version
%_libdir/%{name}codec.so.1
%_libdir/%{name}codec.so.%version

%files -n grokj2k-tools
%_bindir/grk_compress
%_bindir/grk_decompress
%_bindir/grk_dump
%_bindir/grk_transcode

%files devel
%_libdir/%name.so
%_libdir/%{name}codec.so
%_includedir/grok-*/
%_libdir/cmake/grok-*/
%_pkgconfigdir/libgrokj2k.pc
%_pkgconfigdir/libgrokj2kcodec.pc

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 20.4.20-alt1
- update to 20.4.20.
- make the Highway library choice configurable.

* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 20.4.16-alt1
- new version 20.4.16
- build with system highway
- pack spdlog 2.x (git submodule of upstream) as source
- pack grk_transcode tool
- build tests and run them in %%check
- build the mmap interposer test on 64-bit only (fix i586 build)
- build with system taskflow

* Sun May 25 2025 Vitaly Lipatov <lav@altlinux.ru> 15.0.0-alt1
- new version 15.0.0 (with rpmrb script)

* Sat Jan 25 2025 Vitaly Lipatov <lav@altlinux.ru> 14.3.0-alt1
- new version 14.3.0 (with rpmrb script)
- add BR: cli11-devel

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 11.0.0-alt1
- new version 11.0.0 (with rpmrb script)

* Sun Aug 06 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.0.8-alt1.1
- fixed build for Elbrus

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 10.0.8-alt1
- new version 10.0.8 (with rpmrb script)
- return to build with default gcc

* Thu Jul 27 2023 Artyom Bystrov <arbars@altlinux.org> 9.5.0-alt2
- Add handle to fix build

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 9.5.0-alt1
- new version 9.5.0 (with rpmrb script)
- add BR: libdeflate-devel
- add -DNO_WARN_X86_INTRINSICS for ppc64le

* Tue Sep 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.2.0-alt2
- fixed build for Elbrus

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 9.2.0-alt1
- initial build for ALT Sisyphus

