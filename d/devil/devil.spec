%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

%define realname DevIL

Name: devil
Version: 1.8.0
Release: alt1
Summary: Cross-platform image loading and manipulation toolkit
Group: System/Libraries
License: LGPLv2+
Url: http://openil.sourceforge.net

Source: %name-%version.tar

Patch0: devil-1.8.0-rosa-e2k-fix-lcc-with-lcc-confusion.patch
Patch1: devil-1.8.0-rosa-jasper.patch
Patch2: devil-1.8.0-rosa-devel-jasper3.patch
Patch3: devil-1.8.0-openmandriva-sonames.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libSDL-devel liballegro-devel libjpeg-devel
BuildRequires: liblcms2-devel libmng-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libGL-devel libGLU-devel libGLUT-devel libX11-devel
BuildRequires: openexr-devel libjasper-devel libICE-devel libXext-devel
BuildRequires: libXrender-devel libSM-devel libXmu-devel libXi-devel
BuildRequires: libsquish-devel

%description
Developer's Image Library (DevIL) is an Open Source image library
whose distribution is done under the terms of the GNU LGPL license.
DevIL offers you a simple way to implement loading, manipulating, filtering,
converting, displaying, saving from/to several different image formats in your
own project.

%package -n lib%name
Summary: Libraries needed for programs using DevIL.
Group: System/Libraries

%description -n lib%name
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax.
DevIL can load, save, convert, manipulate, filter and display a wide
variety of image formats.

%package -n lib%name-devel
Summary: DevIL development files.
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. This package contains development files.

%package -n lib%name-doc
Summary: DevIL documentation
Group: Development/Documentation

%description -n lib%name-doc
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. This package contains documentation

%package utils
# version 1.8.0 use cmake for build, ilur not builded (ilur source presents in src)
# pkg reserved for next release!
Summary:	Tools provided by DevIL
Group:		System/Libraries
Provides:	%name = %EVR

%description utils
This package contains tools provided by DevIL.

%prep
%setup

%autopatch -p2
%ifarch %ix86
%patch2 -R -p2
%endif

sed -i \
    -e 's|lib$|%_libdir|g' \
    src-IL/CMakeLists.txt src-ILU/CMakeLists.txt src-ILUT/CMakeLists.txt
sed -i \
    -e 's|lib\/|%_libdir\/|g' \
    src-IL/CMakeLists.txt src-ILU/CMakeLists.txt src-ILUT/CMakeLists.txt
sed -i \
    -e 's/@VERSION@/%version/' -e 's!/lib$!%_libdir!' \
    src-IL/pkgconfig/IL.pc.cmake.in src-ILU/pkgconfig/ILU.pc.cmake.in src-ILUT/pkgconfig/ILUT.pc.cmake.in

%build
%add_optflags -D_FILE_OFFSET_BITS=64 -Wno-error=incompatible-pointer-types

%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/IL
%_pkgconfigdir/*

%files -n lib%name-doc
%doc README.md Libraries.txt CREDITS AUTHORS

%files utils
%_bindir/ilur

%changelog
* Mon Apr 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Apr 11 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.7.8-alt6
- NMU: fix FTBFS

* Tue May 23 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.8-alt5
- NMU: fix FTBFS

* Mon Sep 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.8-alt4
- Fixed build with LTO.

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.8-alt3
- NMU: fixed build with new libjasper.

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 1.7.8-alt2.qa4
- NMU: rebuild with new libmng

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7.8-alt1.qa4
- NMU: imported patches from Debian to fix FTBFS.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.3
- Rebuilt with libpng15

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.2
- Removed bad RPATH

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.1
- Rebuilt with liballegro4.4

* Sun Jun 07 2009 Maxim Ivanov <redbaron at altlinux.org> 1.7.8-alt1
- New version

* Thu Sep 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.8-alt5.rc2
- 1.6.8 RC2.
- Some spec cleanup.
- Added patch1 to fix include problems.

* Tue May 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.8-alt4.RC1
- New version.
- Added libmesa-devel and libX11-devel to buildreqs.

* Sun Jan 08 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt3
- Fixed building on current Sisyphus.

* Tue Oct 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt2
- Fixed textrel error.

* Fri Aug 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt1
- Initial build.
