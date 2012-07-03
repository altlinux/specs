%define rev 7628
%define mtl2ver 2.1.2
Name: mtl4
Summary: The Matrix Template Library, Version 4
License: BSD-like
Group: Sciences/Mathematics
Version: 4.r%rev
Release: alt3.beta1
Url: http://www.osl.iu.edu/research/mtl/mtl4/

# https://simunova.zih.tu-dresden.de/svn/mtl4/trunk/
Source: %name-%version.tar.gz
Source1: http://www.osl.iu.edu/download/research/mtl//mtl-2.1.2-23.tentative.tar.gz
Source2: http://www.osl.iu.edu/download/research/mtl//mtl_reference.tar.gz
Source3: CMakeCache.txt
Source4: %name.pc

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: %name-tests = %version-%release
Requires: %name-examples = %version-%release
Requires: lib%name-devel-docs = %version-%release

BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++ gcc-fortran liblapack-devel doxygen
BuildRequires: boost-devel cmake python-devel
BuildPreReq: graphviz /usr/bin/dvips

%description
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

The MTL is a low level library in the sense that the user must be
conscious of the matrix type being used, and that all computationally
expensive operations are explicit. The MTL is not a C++ Matlab or
Mathematica. Nevertheless, the interface is designed to be simple and easy
to use.

The matrix types provided include compressed sparse row/column,
traditional row- and column-major dense, Morton-order, and block-recursive
matrices. All matrix types share a common and easy to use interface.

The algorithms consist of the traditional basic linear algebra
routines (from the BLAS level-1 to 3) which includes matrix and vector
arithmetic.

%package tests
Summary: Test suite for MTL4
Group: Sciences/Mathematics

%description tests
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

Thies package contains a test suite for MTL.

%package examples
Summary: Examples using MTL
Group: Sciences/Mathematics

%description examples
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

This package contains example binaries using MTL.

%package -n lib%name-devel-docs
Summary: Documentation for MTL
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

This package contains development documentation for MTL.

%package -n lib%name-devel
Summary: Development files of MTL v4
Group: Development/C++
Requires: boost-devel

%description -n lib%name-devel
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

This package contains development files of MTL v4.

%package -n libmtl2-%mtl2ver-devel
Summary: Development files for MTL v2
Group: Development/C++
Provides: libmtl2-devel = %version-%release
Conflicts: libmtl2-devel < %version-%release
Obsoletes: libmtl2-devel < %version-%release
BuildArch: noarch

%description -n libmtl2-%mtl2ver-devel
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

This package contains development files for MTL v2.

%package -n libmtl2-%mtl2ver-devel-doc
Summary: Reference guide for the Matrix Template Library, Version 2
License: BSD-like
Group: Development/Documentation
Provides: libmtl2-devel = %version-%release
Conflicts: libmtl2-devel < %version-%release
Obsoletes: libmtl2-devel < %version-%release
BuildArch: noarch

%description -n libmtl2-%mtl2ver-devel-doc
The Matrix Template Library is a C++ class library for basic linear
algebra. The MTL is designed for high-performance while at the same
time taking advantage of the generic programming paradigm (ala the
STL) to allow much greater flexibility and breadth of
functionality. Many new and advanced programming techniques were used
in the construction of this library.

The MTL is a low level library in the sense that the user must be
conscious of the matrix type being used, and that all computationally
expensive operations are explicit. The MTL is not a C++ Matlab or
Mathematica. Nevertheless, the interface is designed to be simple and easy
to use.

The matrix types provided include compressed sparse row/column,
traditional row- and column-major dense, Morton-order, and block-recursive
matrices. All matrix types share a common and easy to use interface.

The algorithms consist of the traditional basic linear algebra
routines (from the BLAS level-1 to 3) which includes matrix and vector
arithmetic.

This package contains reference guide for MTL, Version 2

%prep
%setup
tar -xzf %SOURCE1
tar -xzf %SOURCE2
install -m644 %SOURCE3 %SOURCE4 .

%build
pushd mtl
%add_optflags %optflags_shared -fpermissive
%autoreconf
%configure \
	--with-exceptions=yes \
	--with-matlab=no \
	--with-lapack="-llapack -lgoto2"
popd

export BOOST_ROOT=%prefix
#scons with-blas=1 opt=2 -u -I %python_sitelibdir \
#	add_optflag="%optflags %optflags_shared"
cmake \
	-DCMAKE_C_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags %optflags_shared" \
	.
#make_build VERBOSE=1
%make VERBOSE=1

pushd libs/numeric/mtl/build
gcc -g -pipe -Wall %optflags_shared -DNDEBUG -O3 -ffast-math \
	-fpermissive \
	-o xerbla.o -c xerbla.c
ar r libxerbla.a *.o
ranlib libxerbla.a
popd

pushd libs/numeric/mtl/test_with_optimization
for i in '' memory_block_ vector_
do
	g++ -g -O2 -fpermissive -o move_${i}test move_${i}test.cpp -I../../../..
done
popd

doxygen

%install
pushd mtl
%makeinstall includedir=%buildroot%_includedir/mtl
popd

install -d  %buildroot%_bindir
install -d  %buildroot%_libdir
install -d %buildroot%_docdir/%name/examples
install -d %buildroot%_includedir/boost/numeric

install -m644 libs/numeric/mtl/build/libxerbla.a %buildroot%_libdir
install -m755 libs/numeric/itl/test/*test \
	libs/numeric/mtl/test/*test \
	libs/numeric/mtl/test_with_optimization/*test \
	%buildroot%_bindir

mv libs/numeric/mtl/doc/html libs/numeric/mtl/doc/external/* \
	%buildroot%_docdir/%name/
pushd libs/numeric/mtl/examples
mv images nesting *.cpp CMakeLists.txt SConscript matrix_market *.hpp \
	%buildroot%_docdir/%name/examples
rm -fR CMakeFiles
rm -f *.o Makefile *.cmake *.html
mv dot mtl_dot
install -m755 * %buildroot%_bindir
popd

mv boost/numeric/* %buildroot%_includedir/boost/numeric/

sed -i 's|@VERSION@|%version|' %name.pc
install -d %buildroot%_pkgconfigdir
install -m644 %name.pc %buildroot%_pkgconfigdir

# MTL reference, Version 2

pushd mtl_reference
install -d %buildroot%_docdir/libmtl2-devel-doc
install -p -m644 * %buildroot%_docdir/libmtl2-devel-doc
popd

%files 
%doc README license*.txt

%files tests
%_bindir/*test

%files examples
%_bindir/*
%exclude %_bindir/*test

%files -n lib%name-devel-docs
%_docdir/%name
%exclude %_docdir/%name/html/*.aux
%exclude %_docdir/%name/html/*.dvi
%exclude %_docdir/%name/html/*.log

%files -n lib%name-devel
%_libdir/*.a
%_includedir/boost/numeric/*
%_pkgconfigdir/%name.pc

%files -n libmtl2-%mtl2ver-devel
%_includedir/mtl

%files  -n libmtl2-%mtl2ver-devel-doc
%_docdir/libmtl2-devel-doc

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.r7628-alt3.beta1
- Fixed build

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.r7628-alt2.beta1.2
- Built with GotoBLAS2 instead of ATLAS

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.r7628-alt2.beta1.1
- Rebuilt for debuginfo

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.r7628-alt2.beta1
- Rebuilt with Boost 1.46.1

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.r7628-alt1.beta1
- Version 4 beta-1-r7628

* Mon Aug 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r7299-alt1.beta1
- Version beta-1-r7299

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r7289-alt1.beta1.1
- Set li%name-devel-docs as noarch (thnx ldv@)

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r7289-alt1.beta1
- Version beta-1-r7289

* Sat Aug 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r6821.alpha-alt1
- New snapshot
- Tuned build for python2.5 and python2.6
- Rebuilt with cmake instead scons (build with scons is broken for python2.6)
- Added pkg-config file for MTL4

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r6668.alpha-alt4
- Rebuild with PIC

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r6668.alpha-alt3
- Avoided conflicts with empty and graphviz

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r6668.alpha-alt2
- Add MTL reference, Version 2

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.r6668.alpha-alt1
- Initial build for Sisyphus

