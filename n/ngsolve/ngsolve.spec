%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: ngsolve
Version: 4.9.14
Release: alt4.svn20120228
Summary: NGSolve Finite Element Library
License: GPL or LGPL
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/ngsolve/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel libnetgen-devel tcl-devel libscalapack-devel
BuildPreReq: libmumps-devel liblapack-devel libsuperlu-devel chrpath
BuildPreReq: libscotch-devel libparmetis-devel
BuildPreReq: doxygen texlive-latex-recommended

%description
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

%package -n lib%name
Summary: Shared libraries of NGSolve
Group: System/Libraries

%description -n lib%name
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains shared libraries of NGSolve.

%package -n lib%name-devel
Summary: Development files of NGSolve
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains development files of NGSolve.

%package demos
Summary: Demos for NGSolve
Group: Development/Documentation
Requires: lib%name = %version-%release

%description demos
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains demos for NGSolve.

%package docs
Summary: Documentation for NGSolve
Group: Development/Documentation
BuildArch: noarch

%description docs
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains development documentation for NGSolve.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -DPARALLEL
%autoreconf
%configure \
	--enable-parallel \
	--enable-mpi-threads \
	--enable-mumps \
	--with-netgen=%prefix \
	--with-lapack="-llapack -lgoto2" \
	-with-superlu=-I%_includedir \
	CXX=mpic++
%make_build
%make -C linalg clean
%make LIBPARALLEL=$PWD/parallel/libparallel.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la LIBNGCOMP=$PWD/comp/libngcomp.la
%make -C comp clean
%make LIBPARALLEL=$PWD/parallel/libparallel.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la \
	LIBNGLA=$PWD/linalg/libngla.la
%make -C multigrid clean
%make LIBPARALLEL=$PWD/parallel/libparallel.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la LIBNGCOMP=$PWD/comp/libngcomp.la \
	LIBNGLA=$PWD/linalg/libngla.la

doxygen
pushd doc
latex -output-format=pdf ngsolve.tex
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_libdir
install -m644 parallel/.libs/*.so solve/.libs/*.so linalg/.libs/*.so \
	multigrid/.libs/*.so \
	%buildroot%_libdir
make install DESTDIR=%buildroot \
	LIBPARALLEL=$PWD/parallel/libparallel.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la LIBNGCOMP=$PWD/comp/libngcomp.la \
	LIBNGLA=$PWD/linalg/libngla.la

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h* %buildroot%_includedir/%name/

#for i in %buildroot%_libdir/*.so; do
#	chrpath -r %mpidir/lib $i
#done

pushd programming_demos
rm -f demo_bla demo_comp demo_fem demo_std *.o
popd

%files
%_bindir/ngsolve.tcl

%files -n lib%name
%_libdir/libngsolve.so.*
%_libdir/*.so
%exclude %_libdir/libngsolve.so

%files -n lib%name-devel
%_includedir/*
%_libdir/libngsolve.so

%files demos
%doc programming_demos/*
%_bindir/*
%exclude %_bindir/ngsolve.tcl

%files docs
%doc doxy/html doc/*.pdf doc/quickstart/*.pdf
%doc %_datadir/%name

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt4.svn20120228
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt3.svn20120228
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20120228
- New snapshot

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111116
- Moved non-versioned libraries from lib%name-devel into lib%name

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt1.svn20111116
- Initial build for Sisyphus

