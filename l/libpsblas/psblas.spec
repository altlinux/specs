%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define somver 0
%define sover %somver.2.4

Name: libpsblas
Version: 2.4.0.4
Release: alt2
Summary: Parallel Sparse Basic Linear Algebra Subroutines
License: BSD
Group: System/Libraries
Url: http://www.ce.uniroma2.it/psblas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: %mpiimpl-devel libblacs-devel liblapack-devel
BuildPreReq: libmetis-devel

%description
Most computationally intensive applications work on irregular and sparse domains
that complicate their implementation on parallel machines. The major goal of the
Parallel Sparse Basic Linear Algebra Subroutines (PSBLAS) project is to provide
a framework to enable easy, efficient and portable implementations of iterative
solvers for linear systems, while shielding the user from most details of their
parallelization. The interface is designed keeping in view a Single Program
Multiple Data programming model on distributed memory machines. 

%package doc
Summary: Documentation for Parallel Sparse Basic Linear Algebra Subroutines
Group: Development/Documentation
BuildArch: noarch

%description doc
Most computationally intensive applications work on irregular and sparse domains
that complicate their implementation on parallel machines. The major goal of the
Parallel Sparse Basic Linear Algebra Subroutines (PSBLAS) project is to provide
a framework to enable easy, efficient and portable implementations of iterative
solvers for linear systems, while shielding the user from most details of their
parallelization. The interface is designed keeping in view a Single Program
Multiple Data programming model on distributed memory machines. 

This package contains development documentation for PSBLAS.

%package devel
Summary: Development files of Parallel Sparse Basic Linear Algebra Subroutines
Group: Development/Other
Requires: %name = %version-%release

%description devel
Most computationally intensive applications work on irregular and sparse domains
that complicate their implementation on parallel machines. The major goal of the
Parallel Sparse Basic Linear Algebra Subroutines (PSBLAS) project is to provide
a framework to enable easy, efficient and portable implementations of iterative
solvers for linear systems, while shielding the user from most details of their
parallelization. The interface is designed keeping in view a Single Program
Multiple Data programming model on distributed memory machines. 

This package contains development files of PSBLAS.

%prep
%setup
sed -i 's|(BUILDROOT)|%buildroot|' Make.inc.in

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared -DHAVE_METIS
chmod +x autogen.sh
./autogen.sh

%configure \
	--with-ccopt="%optflags %optflags_shared" \
	--with-fcopt="%optflags %optflags_shared" \
	--with-f90copt="%optflags %optflags_shared" \
	--with-blas="-lgoto2" \
	--with-lapack="-llapack" \
	--with-blacs="-lblacs" \
	--with-metis="-lmetis -lm"
%make_build

%install
%makeinstall_std

mv %buildroot%prefix/Make.inc %buildroot%_includedir/

install -d %buildroot%_docdir/%name
mv %buildroot%prefix/docs/* %buildroot%_docdir/%name/

# shared libraries

source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

pushd %buildroot%_libdir
LIBS="psb_base psb_prec psb_krylov psb_util"
LINKS="-L$PWD"
mkdir tmp
pushd tmp
for i in $LIBS; do
	ar x ../lib$i.a
	mpif90 -shared -Wl,-soname,lib$i.so.%somver * -Wl,-rpath,%mpidir/lib \
		-o ../lib$i.so.%sover $LINKS -lmetis -llapack -lgoto2
	ln -s lib$i.so.%sover ../lib$i.so.%somver
	ln -s lib$i.so.%somver ../lib$i.so
	rm -f *
	export LINKS="$LINKS -l$i"
done
popd
rmdir tmp
popd

sed -i 's|%buildroot||g' %buildroot%_includedir/Make.inc
sed -i 's|^\(INSTALL_DOCSDIR\).*|\1=%_docdir/%name|' \
	%buildroot%_includedir/Make.inc

%files
%doc Changelog LICENSE README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files doc
%_docdir/%name
%doc test

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.4-alt2
- Rebuilt with OpenMPI 1.6

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.4-alt1
- Version 2.4.0-4

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.3-alt5
- Rebuilt with metis 5.0.1

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.3-alt4
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.3-alt3
- Rebuilt with metis 4.0.1-alt9

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.3-alt2
- Rebuilt for debuginfo

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.3-alt1
- Version 2.4.0-3

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.2-alt1
- Version 2.4.0-2

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.1-alt3
- Fixed overlinking of libraries

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.1-alt2
- Removed paths to buildroot

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.1-alt1
- Version 2.4.0-1
- Rebuilt with reformed Metis

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt2
- Enabled SCSRWS
- Enabled SCSRRWS (by upstream)

* Tue Jun 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added shared libraries
- Disabled scsrws

* Mon Jun 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

