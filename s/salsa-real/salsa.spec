%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define scalar_type real
%define oname salsa
%define somver 0
%define sover %somver.2.0
Name: %oname-%scalar_type
Version: 2.01
Release: alt4.svn20100714
Summary: Self-Adapting Large-scale Solver Architecture (%scalar_type scalars)
License: LGPL
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/salsa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://salsa.svn.sourceforge.net/svnroot/salsa
Source: %oname-%version.tar.gz

Requires: lib%name-devel = %version-%release
Requires: slepc-%scalar_type

BuildPreReq: libpetsc-%scalar_type-devel libslepc-%scalar_type-devel
BuildPreReq: petsc-%scalar_type-sources libmysqlclient-devel
BuildPreReq: doxygen graphviz ghostscript-utils chrpath
BuildPreReq: libhdf5-mpi-devel libtrilinos10-devel
BuildPreReq: /usr/bin/latex texlive-extra-utils

%description
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

%package tests
Summary: Testings of SALSA
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description tests
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains testings of SALSA.

%package -n lib%name
Summary: Shared libraries of SALSA
Group: System/Libraries
Requires: libslepc-%scalar_type

%description -n lib%name
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains shared libraries of SALSA.

%package -n lib%name-devel
Summary: Development files of SALSA
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: libslepc-%scalar_type-devel

%description -n lib%name-devel
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains development files of SALSA.

%package -n lib%name-devel-static
Summary: Static libraries of SALSA
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains static libraries of SALSA.

%package -n lib%oname-devel-doc-html
Summary: Documentation for SALSA in HTML
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc-html
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains development documentation for SALSA in HTML.

%package -n lib%oname-devel-doc-pdf
Summary: Documentation for SALSA in PDF
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc-pdf
SALSA is a Self-Adapting Large-scale Solver Architecture: system for
picking numerical algorithms (linear system solving) based on
statistical modeling and machine learning.

This package contains development documentation for SALSA in PDF.

%prep
%setup

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

for i in */Make* */dox.conf* */testing/Makefile
do
	sed -i "s|@TOPDIR@|$PWD|g" $i
	sed -i "s|@BUILDLIBS@|%buildroot$PETSC_DIR/lib|g" $i
	sed -i "s|@SOMVER@|%somver|g" $i
	sed -i "s|@SOVER@|%sover|g" $i
done

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

install -d %buildroot$PETSC_DIR/lib

DEFFLAGS="%optflags %optflags_shared -DPETSC_USE_EXTERN_CXX"
DEFFLAGS="$DEFFLAGS -I$PETSC_DIR/include -I%mpidir/include"

export ANAMOD_LIB_DIR=%buildroot$PETSC_DIR/lib
for i in nmd anamod syspro
do
	pushd $i
	mkdir -p doc
	%make_build lib
%if "%scalar_type" == "real"
	%make_build documentation
%endif
	pushd testing
	ln -s ../Make.inc .
	%make_build unittests
	popd
	popd
done

#################
#      INSTALLING
#################

# install headers

for i in anamod nmd syspro
do
	install -d %buildroot$PETSC_DIR/include/$i
	install -p -m644 $i/*.h %buildroot$PETSC_DIR/include/$i
done

# install tests

for i in anamod nmd syspro
do
	install -d %buildroot$PETSC_DIR/testing/$i
	cp -fR $i/testing/* %buildroot$PETSC_DIR/testing/$i/
	rm -f %buildroot$PETSC_DIR/testing/$i/*.o \
		%buildroot$PETSC_DIR/testing/$i/Make*
done

# install docs

%if "%scalar_type" == "real"
for i in anamod nmd syspro
do
	install -d %buildroot%_docdir/lib%oname-devel/html/$i
	install -d %buildroot%_docdir/lib%oname-devel/pdf/$i
	install -m644 $i/doc/html/* \
		%buildroot%_docdir/lib%oname-devel/html/$i
	install -m644 $i/doc/latex/*.pdf \
		%buildroot%_docdir/lib%oname-devel/pdf/$i
done
%endif

# fix rpath

pushd %buildroot$PETSC_DIR

pushd lib
for i in $(ls *.so); do
	chrpath -r $PETSC_DIR/lib:%mpidir/lib $i
done
popd
popd

for i in %buildroot$PETSC_DIR/testing/*/*
do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib $i ||:
done

for i in $(find %buildroot%_docdir -name '*.html'); do
	sed -i 's|%buildroot||g' $i
done

%files -n lib%name
%_libexecdir/petsc-%scalar_type/lib/*.so.*

%files -n lib%name-devel
%_libexecdir/petsc-%scalar_type/lib/*.so
%_libexecdir/petsc-%scalar_type/include/*

%files -n lib%name-devel-static
%_libexecdir/petsc-%scalar_type/lib/*.a

%files tests
%dir %_libexecdir/petsc-%scalar_type/testing
%_libexecdir/petsc-%scalar_type/testing/*

%if "%scalar_type" == "real"
%files -n lib%oname-devel-doc-html
%dir %_docdir/lib%oname-devel
%_docdir/lib%oname-devel/html

%files -n lib%oname-devel-doc-pdf
%dir %_docdir/lib%oname-devel
%_docdir/lib%oname-devel/pdf
%endif

%changelog
* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt4.svn20100714
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt3.svn20100714
- Fixed RPATH

* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt2.svn20100714
- Rebuilt with PETSc 3.2

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt1.svn20100714.4
- Rebuilt with libhdf5-7-mpi

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt1.svn20100714.3
- Built with GotoBLAS2 instead of ATLAS

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt1.svn20100714.2
- Rebuilt for debuginfo

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt1.svn20100714.1
- Rebuilt

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.01-alt1.svn20100714
- Version 2.01

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt8
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt7
- Fixed linking of libraries

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt6
- Rebuilt with libmysqlclient.so.16

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt5
- Removed paths to buildroot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt4
- Set devel package as noarch

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Rebuilt with PETSc 3.1

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Rebuilt with Trilinos v10

* Sun Oct 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

