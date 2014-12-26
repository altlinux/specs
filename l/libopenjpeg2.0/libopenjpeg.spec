%define _name openjpeg
%define ver_major 2
%define api_ver 2.0
%define rev 2987

Name: lib%_name%api_ver
Version: %ver_major.1.0
Release: alt1

Summary: JPEG 2000 codec library (API version 2.0)
License: BSD
Group: System/Libraries
Url: http://www.openjpeg.org/

%if %rev
# Snapshots taken from stable release branch:
#   svn co http://openjpeg.googlecode.com/svn/branches/openjpeg-2.0 openjpeg-2.0.0
#   find openjpeg-2.0.0 -name ".svn" -print0| xargs -r0 rm -rf -- \;
#   tar -cf openjpeg-2.0.0-%rev.tar.gz openjpeg-2.0.0
Source: %_name-%version-%rev.tar.gz
%else
Source: http://www.openjpeg.org/%_name-%version.tar.gz
%endif

BuildRequires: cmake libstdc++-devel libtiff-devel liblcms2-devel libpng-devel zlib-devel

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
	-DBUILD_THIRDPARTY:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

# to avoid conflict with libopenjpeg-1.x
for file in %buildroot%_bindir/opj_*; do
    mv $file ${file/opj_/opj2_}
done
mv %buildroot%_man1dir/opj_compress.1 %buildroot%_mandir/man1/opj2_compress.1
mv %buildroot%_man1dir/opj_decompress.1 %buildroot%_mandir/man1/opj2_decompress.1
mv %buildroot%_man1dir/opj_dump.1 %buildroot%_mandir/man1/opj2_dump.1

%files
%_libdir/libopenjp%ver_major.so.*
%doc AUTHORS LICENSE NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver/
%_libdir/libopenjp%ver_major.so
%_pkgconfigdir/libopenjp%ver_major.pc
%_man3dir/libopenjp%ver_major.3.*

%files -n openjpeg-tools%api_ver
%_bindir/opj2_compress
%_bindir/opj2_decompress
%_bindir/opj2_dump
%_man1dir/*

%exclude %_datadir/doc/%_name-%api_ver/

%changelog
* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0 snapshot (rev2987)

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- after 2.0.0 snapshot (rev2875)

