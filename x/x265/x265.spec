%define soversion 199
Name: x265
Version: 3.5
Release: alt1
Summary: H.265/HEVC encoder
License: GPLv2
Group: Video
Url: http://x265.org
Requires: libx265-%soversion = %version-%release
Source: %name-%version-%release.tar
Patch0: x265-high-bit-depth-soname.patch
Patch1: x265-pic.patch
Patch2: x265-arm-cflags.patch
Patch3: x265-detect_cpu_armhfp.patch
BuildRequires: cmake gcc-c++ nasm libnuma-devel

%description
H.265/HEVC encoder

%package -n libx265-%soversion
Summary: H.265/HEVC encoder library
Group: System/Libraries
Obsoletes: libx265 = 2.5-alt1

%package -n libx265-devel
Summary: Development files of H.265/HEVC encoder library
Group: Development/C
Requires: libx265-%soversion = %version-%release

%description -n libx265-%soversion
H.265/HEVC encoder library

%description -n libx265-devel
Development files of H.265/HEVC encoder library

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i	-e '/X265_VERSION / s,unknown,%version,' \
	-e '/X265_LATEST_TAG / s,0\.0,%version,' \
	-e '/^#Find version control software.*/i return()' \
	source/cmake/Version.cmake

%build
%add_optflags %optflags_shared
build() {
%cmake -DCMAKE_CXX_FLAGS='%optflags' \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DLIB_INSTALL_DIR=%_lib \
	-DCMAKE_SKIP_RPATH:BOOL=YES \
	-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
	-DENABLE_PIC:BOOL=ON \
	-DENABLE_TESTS:BOOL=ON \
	-DCMAKE_ASM_NASM_FLAGS=-w-macro-params-legacy \
	-DENABLE_SHARED=ON \
	$* \
	../../source
%cmake_build
}

%ifarch x86_64 aarch64 ppc64 ppc64le
mkdir 10bit; pushd 10bit
    build \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DHIGH_BIT_DEPTH=ON
popd

mkdir 12bit; pushd 12bit
    build \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DHIGH_BIT_DEPTH=ON \
    -DMAIN12=ON
popd
%endif

# 8 bit base library + encoder
mkdir 8bit; pushd 8bit
    build -DENABLE_HDR10_PLUS=YES \
    %ifarch %ix86
    	  -DENABLE_ASSEMBLY=OFF \
    %endif
    #
popd

%install
for i in 8 10 12; do
    if [ -d ${i}bit ]; then
        pushd ${i}bit
            %cmakeinstall_std
            # Remove unversioned library, should not be linked to
            rm -f %buildroot%_libdir/libx265_main${i}.so
        popd
    fi
done

find %buildroot -name "*.a" -delete

%check
for i in 8 10 12; do
    if [ -d ${i}bit ]; then
        pushd ${i}bit/BUILD
            test/TestBench || :
        popd
    fi
done

%files
%_bindir/x265

%files -n libx265-%soversion
%_libdir/libx265.so.%soversion
%ifarch x86_64 aarch64 ppc64 ppc64le
%{_libdir}/libx265_main10.so.%soversion
%{_libdir}/libx265_main12.so.%soversion
%endif

%files -n libx265-devel
%_libdir/libx265.so
%_libdir/libhdr10plus.so
%_includedir/x265.h
%_includedir/hdr10plus.h
%_includedir/x265_config.h
%_pkgconfigdir/*

%changelog
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
