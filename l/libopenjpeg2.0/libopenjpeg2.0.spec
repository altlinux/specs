%def_disable snapshot

%define _name openjpeg
%define ver_major 2.1
%define api_ver 2.0
%define libname libopenjp2

Name: lib%_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: JPEG 2000 codec library (API version 2.0)
License: BSD
Group: System/Libraries
Url: http://www.openjpeg.org/

%if_enabled snapshot
# VCS: https://github.com/uclouvain/openjpeg.git
Source: %_name-%version-%rev.tar
%else
#Source: https://github.com/uclouvain/%_name/archive/%_name-%version.tar.gz
Source: http://www.openjpeg.org/%_name-%version.tar.gz
%endif

BuildRequires: cmake libstdc++-devel libtiff-devel liblcms2-devel libpng-devel zlib-devel
BuildRequires: doxygen

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

%prep
%setup -n %_name-%version

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DOPENJPEG_INSTALL_LIB_DIR=%_lib \
	-DBUILD_THIRDPARTY:BOOL=OFF \
	-DBUILD_DOC:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

# to avoid conflict with libopenjpeg-1.x
for file in %buildroot%_bindir/opj_*; do
    mv $file ${file/opj_/opj2_}
done
mv %buildroot%_man1dir/opj_compress.1 %buildroot%_man1dir/opj2_compress.1
mv %buildroot%_man1dir/opj_decompress.1 %buildroot%_man1dir/opj2_decompress.1
mv %buildroot%_man1dir/opj_dump.1 %buildroot%_man1dir/opj2_dump.1

%files
%_libdir/%libname.so.*
%doc AUTHORS* LICENSE NEWS* README* CHANGELOG*

%files devel
%_includedir/%_name-%ver_major/
%_libdir/%_name-%ver_major/
%_libdir/%libname.so
%_pkgconfigdir/%libname.pc
%_man3dir/%libname.3.*

%files -n openjpeg-tools%api_ver
%_bindir/opj2_compress
%_bindir/opj2_decompress
%_bindir/opj2_dump
%_man1dir/*

%exclude %_datadir/doc/%_name-%ver_major/
%exclude %_datadir/doc/html/

%changelog
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

