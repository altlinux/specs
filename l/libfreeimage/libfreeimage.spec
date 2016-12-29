Name: libfreeimage
Version: 3.17.0
Release: alt2

Summary: Multi-format image decoder library
License: GPL and FIPL (see the license-fi.txt)
Group: System/Libraries
URL: http://freeimage.sourceforge.net/

%define srcversion %(echo %version | tr -d .)
Source: http://downloads.sourceforge.net/freeimage/FreeImage%srcversion.zip
Patch: FreeImage-3.17.0-syslibs.patch
Patch1: FreeImage-3.17.0_CVE-2015-0852.patch

BuildRequires: gcc-c++ libgomp-devel libmng-devel libpng-devel openexr-devel unzip
BuildPreReq: rpm-macros-make libraw-devel zlib-devel libwebp-devel
BuildPreReq: libtiff-devel libopenjpeg2.0-devel libjxr-devel
BuildRequires: dos2unix

%description
FreeImage is a library project for developers who would like to support
popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by
multimedia applications. FreeImage is easy to use, fast, multithreading, safe.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n FreeImage
%patch -p1
%patch1 -p1

# remove bundled libraries
rm -r Source/Lib* Source/ZLib Source/OpenEXR
# fix line endings
find ./ -type f -print0| xargs -r0 dos2unix --
# fix Makefile
subst 's|\-o root -g root ||g' Makefile.*
# we can't built due to dependencies on private headers
# see syslibs patch
> Source/FreeImage/PluginG3.cpp
> Source/FreeImageToolkit/JPEGTransform.cpp

%build
sh ./gensrclist.sh
sh ./genfipsrclist.sh
%add_optflags %optflags_shared -fvisibility=hidden
%make_build -f Makefile.gnu
%make_build -f Makefile.fip

%install
%makeinstall_std INSTALLDIR=%buildroot%_libdir

%files
%_libdir/libfreeimage.so.*
%_libdir/libfreeimage-%version.so
%doc license-fi.txt Whatsnew.txt README.linux

%files devel
%_includedir/*
%_libdir/libfreeimage.so

%changelog
* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt2
- rebuilt against libraw.so.16

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt1.1
- small spec cleanup

* Thu Feb 04 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt1
- 3.17.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2.2
- rebuilt against libraw.so.15

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 01 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt2
- Rebuilt with -fvisibility=hidden (ALT#30891).

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt1
- Version 3.16.0 (ALT #26750)

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.4-alt2
- Rebuilt with new libraw

* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.4-alt1
- Version 3.15.4

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt3
- Rebuilt with libpng15

* Mon Sep 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt2
- Rebuilt with internal libtiff

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt1
- Version 3.15.3

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Rebuilt for debuginfo

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.12.0-alt1.1
- rebuild for set:provides by request of mithraen

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 3.12.0-alt1
- 3.12.0
- Build with system libraries instead of internal copies.

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 3.11.0-alt2
- Remove obsolete ldconfig calls.

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 3.11.0-alt1
- 3.11.0

* Wed Jul 02 2008 Victor Forsyuk <force@altlinux.org> 3.10.0-alt2
- Fix FTBFS on 64 bit arch.

* Tue Jul 01 2008 Victor Forsyuk <force@altlinux.org> 3.10.0-alt1
- Initial build.
