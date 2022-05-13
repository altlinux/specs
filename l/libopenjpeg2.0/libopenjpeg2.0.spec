%def_disable snapshot

%define _name openjpeg
%define ver_major 2.5
%define api_ver 2.0
%define libname libopenjp2

%def_enable docs
#x86_64: 99%% tests passed, 2 tests failed out of 1541
%def_disable check

Name: lib%_name%api_ver
Version: %ver_major.0
Release: alt1

Summary: JPEG 2000 codec library (API version 2.0)
License: BSD-2-Clause
Group: System/Libraries
Url: https://www.openjpeg.org/

%if_enabled snapshot
Vcs: https://github.com/uclouvain/openjpeg.git
Source: %_name-%version.tar
%else
Source: https://github.com/uclouvain/%_name/archive/v%version/%_name-%version.tar.gz
#Source: %url%_name-%version.tar.gz
%endif
# https://github.com/uclouvain/openjpeg-data.git
# 679840K
%{?_enable_check:Source1: %_name-data-cd724fb.tar}

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libtiff-devel libjpeg-devel libwebp-devel
BuildRequires: liblcms2-devel libpng-devel libjbig-devel
BuildRequires: zlib-devel libdeflate-devel liblzma-devel libzstd-devel
%{?_enable_docs:BuildRequires: doxygen graphviz}
%{?_enable_check:BuildRequires: ctest}

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. This package contains
runtime libraries for applications that use OpenJPEG.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%package -n openjpeg-tools%api_ver
Summary: JPEG 2000 command line tools
Group: Graphics

%description -n openjpeg-tools%api_ver
OpenJPEG is an open-source JPEG 2000 codec written in C.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
#BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
The %name-devel-doc package includes documentation necessary for
developing with %name library.

%prep
%setup -n %_name-%version
%{?_enable_check:mkdir data && tar -xf %SOURCE1 --strip-components=1 -C data/}

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DOPENJPEG_INSTALL_LIB_DIR=%_lib \
	-DBUILD_THIRDPARTY:BOOL=OFF \
	%{?_enable_docs:-DBUILD_DOC:BOOL=ON} \
	%{?_enable_check:-DBUILD_TESTING=ON \
	 -DBUILD_UNIT_TESTS=ON \
	 -DOPJ_DATA_ROOT=${PWD}/data}
%nil
%cmake_build

%install
%cmake_install

# to avoid conflict with libopenjpeg-1.x
for file in %buildroot%_bindir/opj_*; do
    mv $file ${file/opj_/opj2_}
done
%if_enabled docs
mv %buildroot%_man1dir/opj_compress.1 %buildroot%_man1dir/opj2_compress.1
mv %buildroot%_man1dir/opj_decompress.1 %buildroot%_man1dir/opj2_decompress.1
mv %buildroot%_man1dir/opj_dump.1 %buildroot%_man1dir/opj2_dump.1
%endif
# and fix cmake-files
subst 's|opj_\([compess,decompess,dump]\)|opj2_\1|g' %buildroot%_libdir/%_name-%ver_major/*.cmake

%check
%cmake_build -t test

%files
%_libdir/%libname.so.*
%doc AUTHORS* LICENSE NEWS* README* CHANGELOG*

%files devel
%_includedir/%_name-%ver_major/
%_libdir/%_name-%ver_major/
%_libdir/%libname.so
%_pkgconfigdir/%libname.pc
%{?_enable_docs:%_man3dir/%libname.3.*}

%files -n openjpeg-tools%api_ver
%_bindir/opj2_compress
%_bindir/opj2_decompress
%_bindir/opj2_dump
%{?_enable_docs:%_man1dir/*}

%if_enabled docs
%files devel-doc
%_datadir/doc/%_name-%ver_major/
%endif

%changelog
* Fri May 13 2022 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0 (fixed CVE-2013-4289, CVE-2013-4290, CVE-2019-6988, 
  CVE-2018-20846, CVE-2018-16376, CVE-2021-29338)

* Sat Jul 17 2021 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt3
- updated BR for docs

* Sat Apr 17 2021 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt2
- improved "docs" knob
- prepared %%check

* Tue Dec 29 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- updated to v2.4.0-2-gb897e2cb (fixed CVE-2020-8112, CVE-2020-6851
  CVE-2019-6988, CVE-2019-12973)
- new -devel-doc subpackage
- fixed License tag

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1 (fixed CVE-2017-14041, CVE-2018-6616, CVE-2018-5785, CVE-2018-14423)

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- use -DBUILD_STATIC_LIBS=OFF (ALT #35586)
- fixed .cmake-files (ALT#35585)
- applied upstream fix for CVE-2018-5785

* Sat Oct 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sat Oct 01 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Sat Jul 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu May 28 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2
- updated to 2.1.0-rev3004

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0 snapshot (rev2987)

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- after 2.0.0 snapshot (rev2875)

