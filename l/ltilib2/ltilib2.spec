%define sover 2

Name: ltilib2
Version: 2.120208
Release: alt1
Summary: Algorithms and data structures frequently used in image processing and computer vision
License: BSD
Group: Sciences/Mathematics
Url: http://www.ie.itcr.ac.cr/palvarado/ltilib-2/homepage/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ liblapack-devel libX11-devel /proc
BuildPreReq: valgrind-devel gcc-fortran libf2c-ng-devel libjpeg-devel
BuildPreReq: libpng-devel libICE-devel libXt-devel gtk+2-devel
BuildPreReq: xorg-xextproto-devel libXext-devel libfftw3-devel
BuildPreReq: libdc1394-devel libraw1394-devel rpm-macros-make
BuildPreReq: texlive-latex-recommended

Requires: lib%name-devel = %version-%release

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
Summary: Shared libraries of LTI-Lib 2
Group: System/Libraries

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

This package contains shared libraries of LTI-Lib 2.

%package -n lib%name-devel
Summary: Development files of LTI-Lib 2
Group: Development/C++
Requires: lib%name = %version-%release
Provides: liblti-devel = %version-%release
Conflicts: liblti-devel < %version-%release
Obsoletes: liblti-devel < %version-%release

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

This package contains development files of LTI-Lib 2.

%package -n lib%name-devel-doc
Summary: Documentation for LTI-Lib 2
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains development documentation for LTI-Lib 2.

%package examples
Summary: Demo for LTI-Lib 2
Group: Development/Documentation
BuildArch: noarch

%description examples
The LTI-Lib is an object oriented library with algorithms and data structures
frequently used in image processing and computer vision. It has been developed
at the Chair of Technical Computer Science (Lehrstuhl fuer Technische
Informatik) LTI at the Aachen University of Technology, as part of many
research projects in computer vision dealing with robotics, object recognition
and sing language and gesture recognition.

The main goal of the LTI-Lib is to provide an object oriented library in C++,
which simplifies the code sharing and maintenance, but still providing fast
algorithms that can be used in real applications.

This package contains examples for LTI-Lib 2.

%prep
%setup

sed -i 's|@echo|echo|g' linux/Makefile.in
sed -i \
	"s|@GTKLIBS@|`pkg-config gdk-2.0 --libs` `pkg-config gtk+-2.0 --libs`|g" \
	linux/Makefile.in

%build
pushd linux

DEFS="-U_USE_PHILIPS_TOUCAM -DHAVE_GTK=1"
%add_optflags -fno-strict-aliasing $DEFS $(pkg-config gtk+-2.0 --cflags)
%autoreconf
%make_build_ext -f Makefile.cvs

%configure \
	--enable-debug=no \
	--with-x \
	--with-gtk \
	--enable-gtk \
	--with-blas=goto2 \
	--with-lapack-lib=lapack \
	--with-lapack-path-lib=lapack
sed -i 's|.*HAVE_GTK.*|#define HAVE_GTK 1|' ../src/basics/config.h
sed -i 's|\(\-O3\)|-g -fno-strict-aliasing \1|g' \
	$(find ./ -name Makefile)
%make_build all-release

popd

%make -C doc/styleguide/en pdf

%install
%makeinstall_std -C linux

pushd %buildroot%_libdir/ltilib-2.0.0
for i in $(ls *.a|sort -r); do
	LIB=$(echo $i|sed 's|\.a||')
	g++ -shared -Wl,--whole-archive $i -Wl,--no-whole-archive \
		-o ../$LIB.so.%sover -Wl,-soname,$LIB.so.%sover $ADDLIBS \
		$(pkg-config gdk-2.0 --libs) $(pkg-config gtk+-2.0 --libs) \
		-llapack -lgoto2 -lpng -ljpeg -lXext -lX11 -ldc1394 -lz \
		-lpthread -z -Wl,-z,defs
	ln -s $LIB.so.%sover ../$LIB.so
	ADDLIBS="$ADDLIBS $PWD/../$LIB.so"
done
popd

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/*
%_libdir/*.so
%_includedir/*
#_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc doc/homepage doc/html doc/src doc/styleguide/en/*.pdf

%files examples
%doc data/* examples/*

%changelog
* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.120208-alt1
- Version 2.120208

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.111122-alt1
- Version 2.111122

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.110907-alt1
- Version 2.110907

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.110410-alt1
- Initial build for Sisyphus

