%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname dolfin
%define scalar_type complex
%define ldir %_libdir/petsc-%scalar_type
Name: %oname-%scalar_type
Version: 1.0.0
Release: alt9.bzr20120511
Epoch: 1
Summary: C++/Python library for solving differential equations
License: LGPL v3+
Group: Sciences/Mathematics
Url: http://www.fenics.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.fenics.org/hg/dolfin
Source: %oname-%version.tar.gz
Source1: CMakeCache.txt

Requires: python-module-%name = %epoch:%version-%release
Requires: python-module-%{name}_utils = %epoch:%version-%release
Requires: gcc%__gcc_version_base-c++ ufc-devel
Requires: lib%name = %epoch:%version-%release
BuildPreReq: python-module-petsc-config
BuildPreReq: python-module-Pyro4 python-module-Scientific
BuildPreReq: python-module-fiat %mpiimpl-devel python-devel libcgal-devel
BuildPreReq: cmake swig libgts-devel libxml2-devel libnumpy-devel
BuildPreReq: boost-devel libvtk-python-devel vtk-python ufc-devel ffc
BuildPreReq: python-module-viper viper zlib-devel syfi libsyfi-devel
BuildPreReq: python-module-syfi sfc python-module-sfc
BuildPreReq: boost-filesystem-devel boost-program_options-devel
BuildPreReq: boost-math-devel boost-signals-devel boost-mpi-devel
BuildPreReq: libpetsc-%scalar_type-devel gcc-c++ libscotch-devel
BuildPreReq: libsuitesparse-devel libmtl4-devel libamesos10-devel
BuildPreReq: libparmetis-devel libgmp-devel
BuildPreReq: libgmpxx-devel libhdf5-mpi-devel cppunit-devel
BuildPreReq: libpytrilinos10-devel libtrilinos10-devel
BuildPreReq: python-module-PyTrilinos10 libmpfr-devel
BuildPreReq: libarmadillo-devel libhypre-devel libqd-devel
BuildPreReq: petsc-%scalar_type-sources python-module-sphinx-devel
#BuildPreReq: texlive-latex-extra ghostscript-utils
BuildPreReq: ghostscript-utils libhwloc-devel libzoltan10-devel
#BuildPreReq: libgomp-devel
BuildPreReq: libmumps-devel

%description
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

Features:

  * Simple, consistent and intuitive object-oriented API in C++ or Python
  * Automatic and efficient evaluation of finite element variational forms
  through FFC or SyFi
  * Automatic and efficient assembly of linear systems
  * General families of finite elements, including arbitrary order continuous
  and discontinuous Lagrange finite elements, BDM elements, RT elements, BDFM
  elements, Nedelec elements and Crouzeix-Raviart
  * Arbitrary mixed elements as combination of basic elements, including for
  example Taylor-Hood
  * Discontinuous Galerkin methods including jump terms, averages, and integrals
  over interior mesh facets
  * High-performance linear algebra through uBLAS, PETSc, Trilinos and MTL4
  (experimental) with simple C++ and Python wrappers
  * Experimental support for parallel assembly
  * Simplex meshes in 1D, 2D (triangles), and 3D (tetrahedra), including
  adaptive mesh refinement
  * Multi-adaptive mcG(q)/mdG(q) and mono-adaptive cG(q)/dG(q) ODE solvers
  * Support for a range of input/output formats, including DOLFIN XML, VTK,
  Octave, MATLAB, Diffpack, Exodus II

%package -n lib%name
Summary: Shared library of DOLFIN
Group: System/Libraries
Requires: python-module-ufc
Requires: libsuitesparse >= 3.4.0-alt1
Requires: zlib >= 1.2.5-alt1

%description -n lib%name
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains shared library of DOLFIN.

%package -n lib%name-devel
Summary: Development files of DOLFIN
Group: Development/Other
Requires: lib%name = %epoch:%version-%release
Requires: %oname-devel-common = %version-%release
Requires: libsyfi-devel ufc-devel zlib-devel
Requires: libparmetis-devel >= 3.1.1-alt5
Requires: libsuitesparse-devel >= 3.4.0-alt1
Requires: gcc%__gcc_version_base-c++
Conflicts: %oname-devel-common < %epoch:%version-%release

%description -n lib%name-devel
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains development files of DOLFIN.

%package -n %oname-doc
Summary: Documentation for DOLFIN
Group: Documentation
BuildArch: noarch
Conflicts: %oname-real-doc
Obsoletes: %oname-real-doc

%description -n %oname-doc
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains documentation for DOLFIN.

%package -n %oname-examples
Summary: Examples for DOLFIN
Group: Documentation
BuildArch: noarch
%add_python_req_skip solution_dual mayavi stability_factors solution
%add_python_req_skip solution_1 solution_2 solution_3 solution_4
%add_python_req_skip solution_5 solution_6 solution_7 solution_8
%add_python_req_skip solution_9

%description -n %oname-examples
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains examples for DOLFIN.

%package -n %oname-example-data
Summary: Example data for DOLFIN
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %oname-example-data
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains example data for DOLFIN.

%package -n python-module-%name
Summary: Python module of DOLFIN
Group: Development/Python
%add_python_lib_path %ldir/python
Requires: libpetsc-%scalar_type >= 3.0.0_p7-alt3
Requires: lib%name-devel = %epoch:%version-%release
Requires: viper
%setup_python_module %oname
%py_provides %oname
%py_requires viper multiprocessing
Provides: python-module-%oname = %epoch:%version-%release

%description -n python-module-%name
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains Python module of DOLFIN.

%package -n python-module-%{name}_utils
Summary: Utils Python module of DOLFIN
Group: Development/Python
%add_python_lib_path %ldir/python
Requires: libpetsc-%scalar_type >= 3.0.0_p7-alt3
Requires: lib%name = %epoch:%version-%release
%setup_python_module %{oname}_utils
%py_provides %{oname}_utils
Provides: python-module-%{oname}_utils = %epoch:%version-%release

%description -n python-module-%{name}_utils
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains utils Python module of DOLFIN.

%package -n %oname-tests
Summary: Tests and benchmarks for DOLFIN
Group: Development/Other
BuildArch: noarch

%description -n %oname-tests
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains tests and benchmarks for DOLFIN.

%package -n %oname-devel-common
Summary: Scalar type independent development files of DOLFIN
Group: Development/Other
Conflicts: lib%name-devel < %epoch:%version-%release
Requires: python-module-numpy >= 1.4.0-alt1.svn20090822
Requires: zlib-devel >= 1.2.5-alt1

%description -n %oname-devel-common
DOLFIN is the C++/Python interface of FEniCS, providing a consistent PSE
(Problem Solving Environment) for ordinary and partial differential equations.

This package contains Scalar type independent development files of DOLFIN.

%prep
%setup

mkdir BUILD
pushd BUILD
install -p -m644 %SOURCE1 .
sed -i 's|@SCALAR_TYPE@|%scalar_type|g' CMakeCache.txt \
	../site-packages/dolfin/compilemodules/__init__.py
sed -i 's|@LIBDIR@|%_libdir|g' CMakeCache.txt
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" CMakeCache.txt
#	test/memory/dolfin_valgrind.supp
popd

cp -f %oname/scons/pkgconfig/gmp.pc \
	%_pkgconfigdir/mtl4.pc %_pkgconfigdir/zlib.pc \
	pkgconfig/
sed -i 's|2\.1\.1|4.2.4|g' pkgconfig/mtl4.pc

%build
mpi-selector --set %mpiimpl
source /usr/bin/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

LDFLAGS="-L%mpidir/lib -Wl,-rpath,%mpidir/lib"
export LDFLAGS="$LDFLAGS -L$PETSC_DIR/lib -Wl,-rpath,$PETSC_DIR/lib"
export LIBDIR=%_libdir

mkdir -p CMakeFiles/cmTryCompileExec.dir
pushd BUILD
cmake -DCMAKE_INSTALL_PREFIX:PATH=$PETSC_DIR ..
sed -i \
	's|^\(GMP_LIBRARIES.*\)|\1;%_libdir/libgmpxx.so;%_libdir/libmpfr.so|' \
	CMakeCache.txt
%make_build
popd

%install
source /usr/bin/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd BUILD
%makeinstall_std

install -d %buildroot%ldir/lib
install -d %buildroot%ldir/include
install -d %buildroot%ldir/python
install -d %buildroot%_datadir/%oname
install -d %buildroot%_pkgconfigdir
install -d %buildroot%_bindir

mv %buildroot$PETSC_DIR/share/%oname/demo %buildroot%_datadir/%oname/examples
mv %buildroot$PETSC_DIR/share/%oname/data %buildroot%_datadir/%oname/
#rm -f examples/pde/nonlinear-poisson/cpp/plot.py* \
#	examples/ode/stiff/cpp/plot.py* \
#	$(egrep -R 'solution\ import' examples |awk -F : '{print $1}')
cp -fR ../bench test %buildroot%_datadir/%oname/
popd
for i in $(egrep -R '@PKG_NAME@' %buildroot%_datadir/%oname/|awk -F : '{print $1}')
do
	sed -i 's|@PKG_NAME@|%name|g' $i
done

mv %buildroot$PETSC_DIR/bin/* %buildroot%_bindir/
rmdir %buildroot$PETSC_DIR/bin
mv %buildroot$PETSC_DIR/share/man %buildroot%_datadir/
rm -fR %buildroot$PETSC_DIR/share/man
%if "%scalar_type" == "complex"
pushd %buildroot%_bindir
mv dolfin-convert dolfin-convert-complex
mv dolfin-order dolfin-order-complex
popd
pushd %buildroot%_man1dir
mv dolfin-convert.1.gz dolfin-convert-complex.1.gz
mv dolfin-order.1.gz dolfin-order-complex.1.gz
popd
%endif

cp %_includedir/ufc.h %buildroot%ldir/include/%oname/
cp %_includedir/swig/ufc.i %buildroot%ldir/include/%oname/swig/

rm -f pkgconfig/zlib.pc pkgconfig/mtl4.pc
BOOST_VERSION=$(rpm -q --qf "%{VERSION}" boost-devel)
sed -i "s|^\(Version:\).*|\1 $BOOST_VERSION|" \
	pkgconfig/boost*.pc
cp -f pkgconfig/*.pc %buildroot%_pkgconfigdir
mv %buildroot$PETSC_DIR/lib/pkgconfig/%oname.pc \
	%buildroot%_pkgconfigdir/%name.pc

mv %buildroot$PETSC_DIR/%_lib/python%_python_version/site-packages/* \
	%buildroot%ldir/python/
rm -fR %buildroot$PETSC_DIR/%_lib/python%_python_version
%ifarch x86_64
mv %buildroot$PETSC_DIR/lib/python%_python_version/site-packages/* \
	%buildroot%ldir/python/
rm -fR %buildroot$PETSC_DIR/lib/python%_python_version
%endif

ln -s %_includedir/swig %buildroot$PETSC_DIR/include/

# fix bug in pkgconfig file
sed -i 's|debug optimized||' %buildroot%_pkgconfigdir/%name.pc

%files
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/*
%_man1dir/*

%files -n lib%name
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%ldir/include/*
%ldir/share/%oname
%_pkgconfigdir/%name.pc

%if "%scalar_type" == "real"
%files -n %oname-devel-common
%_pkgconfigdir/*
%exclude %_pkgconfigdir/%name.pc

#files -n %oname-doc
#doc %dir %_docdir/%oname
#doc %_docdir/%oname

%files -n %oname-examples
%dir %_datadir/%oname
%_datadir/%oname/examples

%files -n %oname-tests
%dir %_datadir/%oname
%_datadir/%oname/test
%_datadir/%oname/bench

%files -n %oname-example-data
%dir %_datadir/%oname
%_datadir/%oname/data
%endif

%files -n python-module-%name
%dir %ldir/python
%ldir/python/%oname

%files -n python-module-%{name}_utils
%dir %ldir/python
%ldir/python/%{oname}_utils

%changelog
* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt9.bzr20120511
- Changed native directory: %%_libexecdir/%name -> %%_libdir/%name

* Thu Jun 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt8.bzr20120511
- Rebuilt with OpenMPI 1.6

* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt7.bzr20120511
- Rebuilt

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt6.bzr20120511
- Rebuilt with new GMP

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt5.bzr20120511
- Fixed build

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt4.bzr20120511
- New snapshot

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt4.bzr20120116
- Rebuilt with Boost 1.49.0

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt3.bzr20120116
- Rebuilt with Trilinos 10.10.0

* Tue Feb 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt2.bzr20120116
- Rebuilt with CGAL 4.0-beta1

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.bzr20120116
- Version 1.0.0

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.rc2-alt1.bzr20111205
- Rebuilt with PETSc 3.2

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt2.bzr20110728
- Rebuilt with Trilinos 10.8.1

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.11-alt1.bzr20110728.4.1
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.bzr20110728.4
- Rebuilt with updated NumPy

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.bzr20110728.3
- Rebuilt with parmetis 4.0

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.bzr20110728.2
- Rebuilt with swig 2.0.4

* Thu Aug 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.bzr20110728.1
- Rebuilt with CGAL 3.9-beta1

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.bzr20110728
- Version 0.9.11

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110413.2
- Rebuilt with Boost 1.47.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110413.1
- Rebuilt with CGAL 3.8

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110413
- Version 0.9.10

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101201.4
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101201.3
- Fixed pkgconfig file

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101201.2
- Rebuilt with Boost 1.46.1

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101201.1
- Rebuilt for debuginfo

* Thu Dec 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101201
- New snapshot

* Fri Nov 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101122.1
- Fixed
  + pkg-config file
  + linking of main library

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20101122
- Version 0.9.9

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.8
- Restored pkgconfig file on i586

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.7
- Rebuilt with zlib 1.2.5-alt1

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.6
- Rebuilt with Trilinos 10.6.1

* Thu Nov 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.5
- Rebuilt with SWIG 2.0.1

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.4
- Rebuilt with CGAL 3.7

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.3
- Fixed linking of libraries
- Avoid --no-as-needed

* Thu Aug 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.2
- Built with MTL4 2-r7299-beta1

* Wed Aug 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809.1
- Disabled MTL4

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.bzr20100809
- Version 0.9.8
- Enabled SLEPc

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.bzr20100615.3
- Rebuilt with PETSc 3.1
- Disabled SLEPc

* Thu Jul 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.bzr20100615.2
- Added requirement on gcc-c++

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.bzr20100615.1
- Linked with mpfr

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.bzr20100615
- Version 0.9.7

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207.5
- Rebuilt with CGAL 3.6

* Thu Jun 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207.4
- Rebuilt with NumPy 2.0.0

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207.3
- Rebuilt with new SWIG

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207.2
- Rebuilt without python-module-Numeric

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207.1
- Rebuilt with CGAL

* Tue Dec 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.bzr20091207
- Version 0.9.5

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090831.4
- Rebuilt with Trilinos v10

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090831.3
- Rebuilt with python 2.6 (bootstrap)

* Wed Nov 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090831.2
- Rebuilt with texlive instead of tetex

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090831.1
- Rebuilt without udapl support

* Sat Sep 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090831
- Snapshot 20090831
- Rebuilt with shared libraries of requirements instead of static

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090819.1
- Moved pkg-config files for CHOLMOD and UMFPACK into SuiteSparse package

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt5.hg20090819
- Reformed pkgconfig settings (except boost*, zlib and suitesparse's libs,
  because this packages haven't pkg-config files now)

* Sat Jul 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt4
- Renamed scalar type's independent packages

* Sat Jul 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3
- Fixed finding of Scotch and Cholmod for x86_64

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2.1
- Added links for UFC headers
- Install python modules into %ldir/python
	instead %python_sitelibdir

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Reformed for support real and complex scalars

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus
