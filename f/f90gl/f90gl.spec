%define somver 1
%define sover %somver.2.5

Name: f90gl
Summary: Fortran 90 bindings for OpenGL and GLU
Version: 1.2.15
Release: alt7
Group: Development/Tools
License: GPLv2
URL: http://math.nist.gov/f90gl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://math.nist.gov/f90gl/f90gl-1.2.15.tar.gz
Source1: http://math.nist.gov/~WMitchell/papers/nistir6134.pdf
Source2: glopt.h
Source3: fpprinc.h

Requires: lib%name = %version-%release

BuildPreReq: libGLUT-devel libGL-devel libGLU-devel libX11-devel
BuildPreReq: libXext-devel libXaw-devel libXi-devel gcc-fortran
BuildPreReq: libXmu-devel

%description
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

%package doc
Summary: Documentation for f90gl
Group: Development/Documentation
BuildArch: noarch

%description doc
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

This package contains development documentation for f90gl.

%package examples
Summary: Examples of f90gl
Group: Development/Documentation
BuildArch: noarch

%description examples
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

This package contains examples of f90gl.

%package -n lib%name
Summary: Shared libraries of f90gl
Group: System/Libraries
Requires: libGLUT >= 7.10-alt2
Conflicts: libfreeglut

%description -n lib%name
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

This package contains shared libraries of f90gl.

%package -n lib%name-devel
Summary: Development files of f90gl
Group: Development/Other
Requires: libGL-devel libGLU-devel libGLUT-devel

%description -n lib%name-devel
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

This package contains development files of f90gl.

%package -n lib%name-devel-static
Summary: Static libraries of f90gl
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
f90gl is a public domain implementation of the official Fortran 90 bindings
for OpenGL and GLU, and the application of those bindings to GLUT.

This package contains development files of f90gl.

%prep
%setup
install -p -m644 %SOURCE2 %SOURCE3 util

%build
mkdir -p include/GL lib
%make_build -f mf8lum2 MESAHOME=%prefix

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/GL
install -d %buildroot%_docdir/%name-%version
install -d %buildroot%_libdir/%name-examples

install -p -m644 lib/* %buildroot%_libdir
install -p -m644 include/GL/* %buildroot%_includedir/GL
install -p -m644 README USRGUIDE %SOURCE1 \
	%buildroot%_docdir/%name-%version

# shared libraries

pushd %buildroot%_libdir
LINKS="-L$PWD"
LIBS="$(ls *.a |sed 's/lib\(.*\)\.a/\1/g')"
mkdir tmp
pushd tmp
for i in $LIBS; do
	ar x ../lib$i.a
	f95 -shared * -Wl,-soname,lib$i.so.%somver \
		-o ../lib$i.so.%sover $LINKS -lGL -lGLU -lglut
	ln -s lib$i.so.%sover ../lib$i.so.%somver
	ln -s lib$i.so.%somver ../lib$i.so
	LINKS="$LINKS -l$i"
	rm -f *
done
popd
rmdir tmp
popd

%filter_from_requires /^debug.*(libglut\.so.*/s/^/libGLUT-debuginfo\t/

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%exclude %_docdir/%name-%version/README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/GL/*

%files -n lib%name-devel-static
%_libdir/*.a

%files examples
%doc examples

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt7
- Rebuilt

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt6
- Added -g into compiler flags

* Wed Feb 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt5
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt4
- Added libXmu-devel into build requirements

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt3
- Rebuilt for soname set-versions

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt2
- Added shared library

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.15-alt1
- Version 1.2.15

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.14-alt2
- Removed dummy functions from glut/cwrapglt.c

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.14-alt1
- Initial build for Sisyphus

