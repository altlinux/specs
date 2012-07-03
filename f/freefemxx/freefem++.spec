%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Name: freefemxx
Version: 3.18
Release: alt1
Summary: Implementation of a language dedicated to the finite element method
License: LGPL v2.1+
Group: Sciences/Mathematics
Url: http://www.freefem.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel libarpack-devel
BuildPreReq: liblapack-devel libfltk-devel libsuitesparse-devel
BuildPreReq: libX11-devel libGL-devel libGLU-devel libgsl-devel
BuildPreReq: libGLUT-devel flex libICE-devel libXpm-devel
BuildPreReq: libfftw3-mpi-devel libtetgen-devel libmumps-devel
BuildPreReq: libsuperlu-devel libblacs-devel libscalapack-devel
BuildPreReq: libscotch-devel libparmetis-devel chrpath libXext-devel
BuildPreReq: libsuperlu_dist-devel f2c libf2c-ng-devel libhypre-devel
BuildPreReq: libparms-devel libpastix-devel libXxf86vm-devel

Conflicts: bamg

%description
FreeFem++ is an implementation of a language dedicated to the finite
element method. It enables you to solve Partial Differential Equations
(PDE) easily.

Problems involving PDE from several branches of physics such as
fluid-structure interactions require interpolations of data on several
meshes and their manipulation within one program. FreeFem++ includes a
fast quadtree-based interpolation algorithm and a language for the
manipulation of data on multiple meshes (generated with bamg).

%package examples
Summary: Examples for FreeFem++
Group: Documentation
BuildArch: noarch

%description examples
FreeFem++ is an implementation of a language dedicated to the finite
element method. It enables you to solve Partial Differential Equations
(PDE) easily.

Problems involving PDE from several branches of physics such as
fluid-structure interactions require interpolations of data on several
meshes and their manipulation within one program. FreeFem++ includes a
fast quadtree-based interpolation algorithm and a language for the
manipulation of data on multiple meshes (generated with bamg).

This package contains examples for FreeFem++.

%package doc
Summary: Documentation for FreeFem++
Group: Documentation
BuildArch: noarch

%description doc
FreeFem++ is an implementation of a language dedicated to the finite
element method. It enables you to solve Partial Differential Equations
(PDE) easily.

Problems involving PDE from several branches of physics such as
fluid-structure interactions require interpolations of data on several
meshes and their manipulation within one program. FreeFem++ includes a
fast quadtree-based interpolation algorithm and a language for the
manipulation of data on multiple meshes (generated with bamg).

This package contains documentation for FreeFem++.

%prep
%setup

for i in arpack blacs blas f2c fftw fltk hypre metis mumps parmetis \
	parms pastix scalapack scotch superlu superludist tetgen umfpack
do
	rm download/$i -fR
done

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

INCS="-I%_includedir/suitesparse -I%mpidir/include"
INCS="$INCS -I%mpidir/include/metis -I%_includedir/fftw3-mpi"
%add_optflags $INCS -fno-strict-aliasing
%autoreconf
%configure \
%ifarch x86_64
	--enable-m64 \
%else
	--enable-m32 \
%endif
	--enable-optim \
	--with-x \
	--enable-opengl \
	--enable-default-fltk=yes \
	--with-mpi=mpic++ \
	--with-blas="-lgoto2" \
	--with-lapack="-llapack" \
	--with-arpack="-larpack_LINUX -L%mpidir/lib -lmpi_cxx" \
	--with-amd="-lamd" \
	--with-umfpack="-lumfpack" \
	--without-cadna
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std

chrpath -r %mpidir/lib %buildroot%_bindir/FreeFem++-mpi

%files
%doc AUTHORS BUGS ChangeLog COPYING HISTORY* INNOVATION TODO NEWS README
%_bindir/*

%files examples
%dir %_datadir/freefem++
%dir %_datadir/freefem++/%version
%_datadir/freefem++/%version/examples*
%_datadir/freefem++/%version/*.zip

%files doc
%doc DOC/*.pdf

%changelog
* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18-alt1
- Version 3.18

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.17-alt1
- Version 3.17

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14-alt1
- Version 3.14

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt4
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt3
- Rebuilt with shared libfftw3-mpi

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt2
- Fixed build

* Mon Feb 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt1
- Initial build for Sisyphus

