Name: libfreeimage
Version: 3.12.0
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Multi-format image decoder library
License: GPL and FIPL (see the license-fi.txt)
Group: System/Libraries

URL: http://freeimage.sourceforge.net/
%define srcversion %(echo %version | tr -d .)
Source: http://downloads.sourceforge.net/freeimage/FreeImage%srcversion.zip
Patch0: freeimage-64bit-ftbfs.patch
Patch1: FreeImage-3.10.0-syslibs.patch

# Automatically added by buildreq on Tue Sep 08 2009
BuildRequires: gcc-c++ libjpeg-devel libmng-devel libpng-devel libtiff-devel openexr-devel unzip
BuildPreReq: rpm-macros-make

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
%patch1 -p1

subst 's/\r//g' gensrclist.sh

%build
# We build with system libraries instead of internal copies.
# Only internal OpenJPEG is used as this library is not yet in our repo.

# remove included libs to make sure these don't get used during compile
rm -r Source/LibTIFF Source/LibPNG Source/LibMNG Source/LibJPEG Source/ZLib Source/OpenEXR
#rm -r Source/Lib* Source/ZLib Source/OpenEXR

sh ./gensrclist.sh
%add_optflags %optflags_shared
%make_build_ext CXX="g++ -g -DPNG_iTXt_SUPPORTED `pkg-config --cflags OpenEXR`" LIBRARIES="-lstdc++ -lm -ltiff -lpng -lmng -lIlmImf"

%install
install -pD -m644 Dist/FreeImage.h %buildroot%_includedir/FreeImage.h
install -pD -m644 Dist/libfreeimage-%version.so %buildroot%_libdir/libfreeimage-%version.so
ln -sf libfreeimage-%version.so %buildroot%_libdir/libfreeimage.so

%files
%doc license-fi.txt
%_libdir/libfreeimage.so.*
%_libdir/libfreeimage-%version.so

%files devel
%_includedir/*
%_libdir/libfreeimage.so

%changelog
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
