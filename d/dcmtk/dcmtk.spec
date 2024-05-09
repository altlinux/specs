%add_optflags %optflags_shared
%define soname 18

Name: dcmtk
Version: 3.6.8
Release: alt2

Summary: DCMTK - DICOM Toolkit
License: MIT
Group: Graphics

Url: http://dcmtk.org/dcmtk.php.en
VCS: https://github.com/DCMTK/dcmtk
Source: %name-%version.tar

Requires: lib%name%soname = %EVR
BuildRequires: gcc-c++, zlib-devel, libpng-devel, libtiff-devel
BuildRequires: libxml2-devel, libssl-devel, cmake
BuildRequires: libjpeg-devel

%description
DCMTK is a collection of libraries and applications implementing large parts
the DICOM standard. It includes software for examining, constructing and
converting DICOM image files, handling offline media, sending and receiving
images over a network connection, as well as demonstrative image storage
and worklist servers.

Contains patches against latest stable version from
http://gna.org/projects/pdcmtk

%package -n lib%name%soname
Summary: %name shared libraries
Group: System/Libraries

%description -n lib%name%soname
%name shared libraries

%package -n lib%name-devel
Summary: Headers for building software that uses %name
Group: Development/C
Requires: lib%name%soname = %EVR
Requires: %name = %EVR
Requires: libxml2-devel

%description -n lib%name-devel
Headers for building software that uses %name.
%ifarch %e2k

NB: a project using tuples from this library will fail to build
    as va_arg is intermixed with C++ constructor there.
%endif

%prep
%setup
%ifarch %e2k
sed -i '/"fenv.h" HAVE_FENV_H/d' CMake/GenerateDCMTKConfigure.cmake
# unportable magic with va_args
sed -i 's/ttuple.cc//' ofstd/tests/CMakeLists.txt
sed -i '/ofstd_tuple/d' ofstd/tests/tests.cc
%endif

%build
%add_optflags -fPIC
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
	-DDCMTK_INSTALL_LIBDIR=%_lib \
	-DDCMTK_INSTALL_CMKDIR=%_libdir/cmake/dcmtk \
	-DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
	-DDCMTK_DEFAULT_CONFIGURATION_DIR=%_sysconfdir/dcmtk \
	-DDCMTK_WITH_OPENSSL:BOOL=ON \
	-DDCMTK_ENABLE_PRIVATE_TAGS:BOOL=ON \
	-DDCMTK_WITH_XML:BOOL=ON \
	-DDCMTK_WITH_TIFF:BOOL=ON \
	-DDCMTK_WITH_ZLIB:BOOL=ON \
	-DDCMTK_WITH_ICONV:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DDCMTK_INSTALL_DATDIC:STRING=share/libdcmtk12 \
	-DDCMTK_USE_CXX11_STL:BOOL=ON \
	-DDCMTK_ENABLE_CXX11:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_datadir/dcmtk-%version/
%_docdir/*
%_man1dir/*
%config(noreplace) %_sysconfdir/*

%files -n lib%name%soname
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n lib%name-devel
%_pkgconfigdir/dcmtk.pc
%_includedir/dcmtk/
%_libdir/*.so
%_libdir/cmake/dcmtk/*.cmake

%changelog
* Thu May 09 2024 Anton Farygin <rider@altlinux.ru> 3.6.8-alt2
- added lost dependencies to the devel package (closes: #50075)

* Mon Apr 08 2024 Michael Shigorin <mike@altlinux.org> 3.6.8-alt1.2
- E2K: tuple-related note regarding devel subpackage
- minor spec cleanup

* Fri Apr 05 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.8-alt1.1
- Fixed build for Elbrus.

* Tue Jan 30 2024 Anton Farygin <rider@altlinux.ru> 3.6.8-alt1
- 3.6.8

* Fri Apr 07 2023 Anton Farygin <rider@altlinux.ru> 3.6.7-alt1
- 3.6.7

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 3.6.6-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue Apr 20 2021 Anton Farygin <rider@altlinux.ru> 3.6.6-alt1
- 3.6.6

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 3.6.5-alt1
- 3.6.5

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 3.6.4-alt1
- 3.6.4
- added soname version to libdcmtk package name

* Tue Sep 18 2018 Anton Farygin <rider@altlinux.ru> 3.6.3-alt1
- 3.6.3
- disabled libwrap support

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.6.2-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Nov 01 2017 Anton Farygin <rider@altlinux.ru> 3.6.2-alt1
- new version
- enabled build shared libraries

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.4-alt3.3
- Fixed build with gcc 4.7

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.4-alt3.2
- Rebuilt with libpng15

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 3.5.4-alt3.1
- Fixed build with openssl-1.0.

* Fri Feb 05 2010 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt3
- added dcmtk headers

* Wed Nov 25 2009 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt2
- %_sysconfdir/* in spec changed to %%config %_sysconfdir/*

* Fri Nov 13 2009 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt1
- initial build
