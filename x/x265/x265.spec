%define soversion 216
Name: x265
Version: 4.2
Release: alt1
Summary: H.265/HEVC encoder
License: GPLv2
Group: Video
Url: https://www.x265.org/
VCS: https://bitbucket.org/multicoreware/x265_git.git
Source: %name-%version.tar
BuildRequires: cmake gcc-c++ nasm libnuma-devel
BuildRequires: /proc

%description
H.265/HEVC encoder

%package -n libx265-%soversion
Summary: H.265/HEVC encoder library
Group: System/Libraries
Obsoletes: libx265 = 2.5-alt1

%package -n libx265-devel
Summary: Development files of H.265/HEVC encoder library
Group: Development/C
Requires: libx265-%soversion = %EVR

%description -n libx265-%soversion
H.265/HEVC encoder library

%description -n libx265-devel
Development files of H.265/HEVC encoder library

%prep
%setup

sed -i	-e '/X265_VERSION / s,unknown,%version,' \
	-e '/X265_LATEST_TAG / s,0\.0,%version,' \
	-e '/^#Find version control software.*/i return()' \
	source/cmake/Version.cmake

%build
%add_optflags %optflags_shared
%define _cmake__builddir $builddir
build() {
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DLIB_INSTALL_DIR=%_lib \
        -DHIGH_BIT_DEPTH=ON \
	-DCMAKE_SKIP_RPATH:BOOL=YES \
	-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
	-DENABLE_PIC:BOOL=ON \
	-DENABLE_TESTS:BOOL=ON \
	-DCMAKE_ASM_NASM_FLAGS=-w-macro-params-legacy \
	$* \
	-S source
%cmake_build
}

%ifarch x86_64 aarch64
builddir=10bit
    build \
    -DMAIN10=ON \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DEXPORT_C_API=OFF \
    -DENABLE_SHARED=OFF \
    -DHIGH_BIT_DEPTH=ON

builddir=12bit
    build \
    -DHIGH_BIT_DEPTH=ON \
    -DENABLE_SHARED=OFF \
    -DEXPORT_C_API=OFF \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DMAIN12=ON
%endif

%ifarch x86_64 aarch64
mkdir 8bit
ln -s ../12bit/libx265.a 8bit/libx265_main12.a
ln -s ../10bit/libx265.a 8bit/libx265_main10.a
%endif

# 8 bit base library + encoder
builddir=8bit 
    build \
    -DENABLE_SHARED=ON \
    -DHIGH_BIT_DEPTH=OFF \
%ifarch x86_64 aarch64
    -D EXTRA_LIB='x265_main10.a;x265_main12.a' \
    -D EXTRA_LINK_FLAGS='-L.' \
    -DLINKED_10BIT=ON \
    -DLINKED_12BIT=ON \
%endif
%ifarch %ix86
      -DENABLE_ASSEMBLY=OFF \
%endif
    #

%install
%define _cmake__builddir 8bit
%cmake_install

find %buildroot -name "*.a" -delete

%check
pushd 8bit
test/TestBench || :

%files
%_bindir/x265

%files -n libx265-%soversion
%_libdir/libx265.so.%soversion

%files -n libx265-devel
%_libdir/libx265.so
%_includedir/x265.h
%_includedir/x265_config.h
%_pkgconfigdir/*

%changelog
* Sun Apr 26 2026 Anton Farygin <rider@altlinux.org> 4.2-alt1
- 4.1 -> 4.2

* Thu Jun 19 2025 Anton Farygin <rider@altlinux.com> 4.1-alt2
- built libx265 with 8-bit depth as default
- disabled HDR10+ headers and shared libs

* Thu May 29 2025 Anton Farygin <rider@altlinux.com> 4.1-alt1
- 3.5 -> 4.1
- shipped a single libx265.so that now includes 8-/10-/12-bit support
- removed libx265_main10/12

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 3.5-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Apr 21 2021 Anton Farygin <rider@altlinux.ru> 3.5-alt1
- 3.5
- 10 and 12bit variants are built by analogy with x265 from the fedora fusion
- enabled tests

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 3.4-alt1
- 3.4

* Mon Dec 09 2019 Anton Farygin <rider@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 2.8-alt1
- 2.8 

* Fri Feb 16 2018 Anton Farygin <rider@altlinux.ru> 2.5-alt2
- renamed libx265 to libx265-130

* Fri Oct 06 2017 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- 2.5 release

* Thu May 25 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- 2.4 release

* Sat Jun 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7-alt1
- 1.7 release

* Wed Apr 29 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6-alt1
- 1.6 release

* Tue Dec 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 release
