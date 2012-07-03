%define sover 0

Name: lti
Version: 1.9.16
Release: alt6
Summary: Library for image processing and computer vision
License: LGPL
Group: Development/C++
Url: http://ltilib.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: gcc-c++ liblapack-goto-devel libX11-devel /proc
BuildPreReq: valgrind-devel gcc-fortran libf2c-ng-devel libjpeg-devel
BuildPreReq: libpng-devel libICE-devel libXt-devel gtk+-devel
BuildPreReq: xorg-xextproto-devel libXext-devel

Source: http://freefr.dl.sourceforge.net/sourceforge/ltilib/051124_ltilib-1.9.16.tar.bz2
Source1: http://heanet.dl.sourceforge.net/sourceforge/ltilib/051124_ltilib-extras-1.9.16.tar.bz2
Source2: http://puzzle.dl.sourceforge.net/sourceforge/ltilib/051124_DevelopersGuide.pdf
#Patch: ltilib-1.9.15-alt-buildroot_gcc4.3.patch

%description
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

%package -n lib%name
Summary: Shared library of LTI-lib (release version)
Group: System/Legacy libraries

%description -n lib%name
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains shared library of LTI-lib (release version).

%package headers
Summary: Headers of LTI-lib
Group: Development/C++
BuildArch: noarch

%description headers
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains headers of LTI-lib.

%package -n lib%name-devel
Summary: Development files of LTI-lib (release version)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains development files of LTI-lib (release version).

%package -n lib%name-devel-static
Summary: Static library of LTI-lib (release version)
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains static library of LTI-lib (release version).

%package -n lib%name-debug
Summary: Shared library of LTI-lib (debug version)
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name-debug
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains shared library of LTI-lib (debug version).

%package -n lib%name-debug-devel
Summary: Development files of LTI-lib (debug version)
Group: Development/C++
Requires: lib%name-debug = %version-%release
Requires: %name-headers = %version-%release

%description -n lib%name-debug-devel
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains development files of LTI-lib (debug version).

%package -n lib%name-debug-devel-static
Summary: Static library of LTI-lib (debug version)
Group: Development/C++
Requires: lib%name-debug-devel = %version-%release

%description -n lib%name-debug-devel-static
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains a static library of LTI-lib (debug version).

%package -n lib%name-devel-doc
Summary: Development documentation for LTI-lib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for LTI-lib.

%prep
%setup -c %SOURCE0
tar -xjf %SOURCE1
#patch -p0
install -p -m644 %SOURCE2 ./
mv 051124_DevelopersGuide.pdf DevelopersGuide.pdf

sed -i 's|@echo|echo|g' linux/Makefile.in

%build
pushd linux
sed -i '6s|(DESTDIR)|%buildroot|' configure.in
DEFS="-U_USE_PHILIPS_TOUCAM -DHAVE_GTK=1"
%add_optflags $DEFS $(gtk-config --cflags)
%autoreconf
%make_build -f Makefile.cvs
%configure \
	--with-x \
	--with-gtk \
	--enable-gtk \
	--with-blas=goto2
sed -i 's|.*HAVE_GTK.*|#define HAVE_GTK 1|' ../src/basics/config.h
%make_build all-release
popd

%install
pushd linux
%make_install install
popd

pushd %buildroot%_libdir/ltilib-%version
for i in $(ls *.a); do
	LIB=$(echo $i|sed 's|\.a||')
	g++ -shared -Wl,--whole-archive $i -Wl,--no-whole-archive \
		-o ../$LIB.so.%sover -Wl,-soname,$LIB.so.%sover \
		%_libdir/libgdk-1.2.so.0 $(gtk-config --libs gthread) \
		-llapack -lgoto2 -lpng -ljpeg -lXext -lX11 -lz \
		-lpthread -z -Wl,-z,defs
	ln -s $LIB.so.%sover ../$LIB.so
done
popd

#brp_strip_none %_libdir/*d.so*

#filter_from_requires /^debug.*(liblapack\.so.*/s/^/liblapack-goto-debuginfo\t/

#files
#doc README LICENSE
#_bindir/*

#files headers
#_includedir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*d.so.*

#files -n lib%name-devel
#_libdir/*.so
#exclude %_libdir/*d.so

#files -n lib%name-debug
#_libdir/*d.so.*

#files -n lib%name-debug-devel
#_libdir/*d.so

#files -n lib%name-devel-static
#_libdir/%{name}lib-%version
#_libdir/%{name}lib
#exclude %_libdir/%{name}lib-%version/*d.a

#files -n lib%name-debug-devel-static
#dir %_libdir/%{name}lib-%version
#_libdir/%{name}lib-%version/*d.a

#files -n lib%name-devel-doc
#doc DevelopersGuide.pdf

%changelog
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt6
- Fixed build

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt5
- Moved into System/Legacy libraries

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt4
- Built with GotoBLAS2 instead of ATLAS
- Disabled debug and devel-static packages

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt3
- Rebuilt for debuginfo

* Mon Dec 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt2
- Added shared libraries
- Built with GTK+

* Mon Apr 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.16-alt1
- Version 1.9.16

* Sat Nov 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt3
- Rebuilt with libf2c-ng instead of libf2c

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt2
- Rebuild with gcc 4.4

* Thu Mar 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt1
- Initial build for Sisyphus

