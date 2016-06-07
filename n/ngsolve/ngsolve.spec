# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev.git20150323.qa1.1
%set_automake_version 1.11

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: ngsolve
Version: 6.1
#Release: alt1.dev.git20150323.qa1
Summary: NGSolve Finite Element Library
License: GPL or LGPL
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/ngsolve/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.code.sf.net/p/ngsolve/git
Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel libnetgen-devel tcl-devel libscalapack-devel
BuildPreReq: libmumps-devel liblapack-devel libsuperlu-devel chrpath
BuildPreReq: libscotch-devel libparmetis-devel python-devel
BuildPreReq: libgomp-devel boost-python-devel
BuildPreReq: doxygen texlive-latex-recommended

%description
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

%package -n lib%name
Summary: Shared libraries of NGSolve
Group: System/Libraries
%py_provides ngslib

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
BuildArch: noarch

%description -n lib%name-devel
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains development files of NGSolve.

%package -n python-module-%name
Summary: Python module of NGSolve
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
NGSolve is a general purpose Finite Element Library on top of Netgen.
With the basic library one can solve heat flow equations, Maxwell
equations, and solid mechanical problems. Several add-ons are available
for particular application classes.

This package contains Python module of NGSolve.

%package demos
Summary: Demos for NGSolve
Group: Development/Documentation
Requires: lib%name = %version-%release
%add_python_req_skip fem

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

sed -i 's|@PYVER@|%_python_version|' configure.ac

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -DPARALLEL -fpermissive
%autoreconf
%configure \
	--enable-parallel \
	--enable-mpi-threads \
	--enable-mumps \
	--enable-python \
	--with-netgen=%prefix \
	--with-lapack="-llapack -lopenblas" \
	--with-superlu=-I%_includedir \
	CXX=mpic++
%make_build -C ngstd libngstd.la
%make_build -C basiclinalg libngbla.la
%make_build -C fem libngfem.la
%make_build -C parallel libparallel.la
%make_build -C multigrid libngmg.la
%make_build -C comp libngcomp.la
%make_build -C linalg libngla.la
%make_build -C solve libngsolve.la
%make_build -C comp clean
%make_build -C comp libngcomp.la LIBNGLA=$PWD/linalg/libngla.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la
%make_build -C parallel clean
%make_build -C parallel libparallel.la LIBNGLA=$PWD/linalg/libngla.la
%make_build -C linalg clean
%make_build -C linalg LIBNGSOLVE=$PWD/solve/libngsolve.la
%make_build

doxygen
pushd doc
latex -output-format=pdf ngsolve.tex
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_libdir
install -m644 solve/.libs/*.so linalg/.libs/*.so \
	%buildroot%_libdir
make install DESTDIR=%buildroot \
	LIBPARALLEL=$PWD/parallel/libparallel.la \
	LIBNGSOLVE=$PWD/solve/libngsolve.la LIBNGCOMP=$PWD/comp/libngcomp.la \
	LIBNGLA=$PWD/linalg/libngla.la
install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h* %buildroot%_includedir/%name/

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

ln -s %_libdir/ngslib.so %buildroot%python_sitelibdir/

%files
%_bindir/ngsolve.tcl
%_datadir/%name

%files -n lib%name
%_libdir/*.so

%files -n lib%name-devel
%_includedir/*

%files demos
#doc programming_demos/*
%_bindir/*
%exclude %_bindir/ngsolve.tcl

%files docs
%doc doc/*.pdf doxy/html doc/quickstart/*.pdf
#doc %_datadir/%name

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.1-alt1.dev.git20150323.qa1.1
- (AUTO) subst_x86_64.

* Fri Apr 08 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.1-alt1.dev.git20150323.qa1
- NMU: rebuilt with rebuilt netgen.

* Fri Mar 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt1.dev.git20150323
- Version 6.1-dev
- Added Python module

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140704
- New snapshot

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140618
- Version 5.3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt3
- Fixed build

* Thu Sep 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- 5.1 released

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130203
- Version 5.1

* Wed Aug 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.svn20120821
- Version 5.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt5.svn20120228
- Built with OpenBLAS instead of GotoBLAS2

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

