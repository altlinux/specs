BuildRequires(pre): rpm-build-python

%define dirs DerApproximator FuncDesigner OpenOpt SpaceFuncs

Name: OOSuite
Version: 0.37
Release: alt2.svn20120206
Summary: OpenOpt Suite
License: BSD
Group: Sciences/Mathematics
Url: http://openopt.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://openopt.org/PythonPackages
Source: %name-%version.tar.gz

BuildPreReq: python-devel gcc-fortran /proc
BuildPreReq: libnumpy-devel python-module-setuptools
BuildPreReq: python-module-matplotlib
BuildPreReq: libglpk-devel
BuildPreReq: python-module-cvxopt python-module-pswarm_py
BuildPreReq: python-module-pyipopt python-module-pywrapper
BuildPreReq: python-module-scipy libgotoblas-devel

%description
OpenOpt is a free optimization framework that was created in June of
2007. It is a relatively new project that is currently developed in the
optimization department of the Cybernetics Institute at the Ukrainian
National Academy of Sciences, in collaboration with the SciPy
development team. OpenOpt interfaces with many different algorithms for
solving optimization problems (solvers), some of which are written in C
or Fortran.

%package -n python-module-toms587
Summary: Python wrapper of toms587
Group: Development/Python
%setup_python_module toms587
%py_provides toms587
Conflicts: python-module-toms_587
Obsoletes: python-module-toms_587

%description -n python-module-toms587
This package contains python wrapper of toms587.

%package -n python-module-openopt
Summary: Python module of Numerical optimization framework
Group: Development/Python
BuildArch: noarch
%setup_python_module openopt
Requires: libglpk >= 4.38
Requires: python-module-scipy >= 0.8.0
Requires: python-module-matplotlib
%py_requires scipy setuptools matplotlib cvxopt
%py_requires pswarm_py pyipopt pywrapper toms587
%add_python_req_skip cplex

%description -n python-module-openopt
OpenOpt is a free optimization framework that was created in June of
2007. It is a relatively new project that is currently developed in the
optimization department of the Cybernetics Institute at the Ukrainian
National Academy of Sciences, in collaboration with the SciPy
development team. OpenOpt interfaces with many different algorithms for
solving optimization problems (solvers), some of which are written in C
or Fortran.

This package contains python module of OpenOpt.

%package -n python-module-openopt-tests
Summary: Tests for Python module of Numerical optimization framework
Group: Development/Python
BuildArch: noarch
Requires: python-module-openopt = %version-%release

%description -n python-module-openopt-tests
OpenOpt is a free optimization framework that was created in June of
2007. It is a relatively new project that is currently developed in the
optimization department of the Cybernetics Institute at the Ukrainian
National Academy of Sciences, in collaboration with the SciPy
development team. OpenOpt interfaces with many different algorithms for
solving optimization problems (solvers), some of which are written in C
or Fortran.

This package contains tests for python module of OpenOpt.

%package -n python-module-openopt-examples
Summary: Examples for Python module of Numerical optimization framework
Group: Development/Python
BuildArch: noarch
Requires: python-module-openopt = %version-%release

%description -n python-module-openopt-examples
OpenOpt is a free optimization framework that was created in June of
2007. It is a relatively new project that is currently developed in the
optimization department of the Cybernetics Institute at the Ukrainian
National Academy of Sciences, in collaboration with the SciPy
development team. OpenOpt interfaces with many different algorithms for
solving optimization problems (solvers), some of which are written in C
or Fortran.

This package contains examples for python module of OpenOpt.

%package -n python-module-DerApproximator
Summary: A python module for finite-differences derivatives approximation
Group: Development/Python
%setup_python_module DerApproximator

%description -n python-module-DerApproximator
DerApproximator - tool to get (or check user-supplied) derivatives via
finite-difference approximation.

%package -n python-module-DerApproximator-tests
Summary: Tests for python module for finite-differences derivatives approximation
Group: Development/Python
Requires: python-module-DerApproximator = %version-%release

%description -n python-module-DerApproximator-tests
DerApproximator - tool to get (or check user-supplied) derivatives via
finite-difference approximation.

This package contains tests for DerApproximator.

%package -n python-module-FuncDesigner
Summary: A python module for function design and automatic derivatives
Group: Development/Python
%setup_python_module FuncDesigner

%description -n python-module-FuncDesigner
FuncDesigner - tool to rapidly build functions and get their derivatives
via automatic differentiation. Also, you can solve/optimize problems
coded in FuncDesigner by OpenOpt.

%package -n python-module-FuncDesigner-tests
Summary: Tests for python module for function design and automatic derivatives
Group: Development/Python
Requires: python-module-FuncDesigner = %version-%release

%description -n python-module-FuncDesigner-tests
FuncDesigner - tool to rapidly build functions and get their derivatives
via automatic differentiation. Also, you can solve/optimize problems
coded in FuncDesigner by OpenOpt.

This package contains tests for FuncDesigner.

%package -n python-module-FuncDesigner-examples
Summary: Examples for python module for function design and automatic derivatives
Group: Development/Python
Requires: python-module-FuncDesigner = %version-%release

%description -n python-module-FuncDesigner-examples
FuncDesigner - tool to rapidly build functions and get their derivatives
via automatic differentiation. Also, you can solve/optimize problems
coded in FuncDesigner by OpenOpt.

This package contains examples for FuncDesigner.

%package -n python-module-SpaceFuncs
Summary: Python module for 2D, 3D, ND space objects modelling and optimization
Group: Development/Python
%setup_python_module SpaceFuncs

%description -n python-module-SpaceFuncs
SpaceFuncs is a completely free Python language module for 2D, 3D,
N-dimensional space calculations with abilities of

  * parametrized modeling (using FuncDesigner)
  * performing numerical optimization and solving geometrical systems of
    equations (possibly parametrized), using FuncDesigner automatic
    differentiation, that yields more precise (and very often faster)
    results than finite-differences derivatives approximation
  * some graphic output

%package -n python-module-SpaceFuncs-examples
Summary: Examples for SpaceFuncs
Group: Development/Python
Requires: python-module-SpaceFuncs = %version-%release

%description -n python-module-SpaceFuncs-examples
SpaceFuncs is a completely free Python language module for 2D, 3D,
N-dimensional space calculations with abilities of

  * parametrized modeling (using FuncDesigner)
  * performing numerical optimization and solving geometrical systems of
    equations (possibly parametrized), using FuncDesigner automatic
    differentiation, that yields more precise (and very often faster)
    results than finite-differences derivatives approximation
  * some graphic output

This package contains examples for SpaceFuncs.

%prep
%setup

%build
f2py --opt="%optflags" --f90exec=="f95" \
	-m toms587 \
	-c OpenOpt/openopt/solvers/Standalone/toms587.f \
	-lgoto2
export PYTHONPATH=$PWD
for dir in %dirs; do
	pushd $dir
	%python_build_debug -v
	popd
done

%install
for dir in %dirs; do
	pushd $dir
	%python_install
	popd
done

install -d  %buildroot%python_sitelibdir
install -m644 toms587.so %buildroot%python_sitelibdir

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/DerApproximator* \
	%buildroot%python_sitelibdir/
mv %buildroot%python_sitelibdir_noarch/FuncDesigner* \
	%buildroot%python_sitelibdir/
mv %buildroot%python_sitelibdir_noarch/SpaceFuncs* \
	%buildroot%python_sitelibdir/
mv %buildroot%python_sitelibdir_noarch/kernel* \
	%buildroot%python_sitelibdir/
%endif
cp -fR FuncDesigner/FuncDesigner/examples \
	FuncDesigner/FuncDesigner/tests \
	%buildroot%python_sitelibdir/FuncDesigner/
touch %buildroot%python_sitelibdir/FuncDesigner/examples/__init__.py
touch %buildroot%python_sitelibdir/FuncDesigner/tests/__init__.py
cp -fR DerApproximator/tests \
	%buildroot%python_sitelibdir/DerApproximator/
touch %buildroot%python_sitelibdir/DerApproximator/tests/__init__.py
cp -fR SpaceFuncs/examples \
	%buildroot%python_sitelibdir/SpaceFuncs/
touch %buildroot%python_sitelibdir/SpaceFuncs/examples/__init__.py

%files -n python-module-toms587
%doc OpenOpt/openopt/solvers/Standalone/toms587.f
%python_sitelibdir/toms587.so

%files -n python-module-openopt
%doc OpenOpt/COPYING.txt OpenOpt/README.txt
%doc OpenOpt/openopt/doc/*
%python_sitelibdir_noarch/openopt*
%exclude %python_sitelibdir_noarch/openopt/tests
%exclude %python_sitelibdir_noarch/openopt/examples

%files -n python-module-openopt-tests
%python_sitelibdir_noarch/openopt/tests

%files -n python-module-openopt-examples
%python_sitelibdir_noarch/openopt/examples

%files -n python-module-DerApproximator
%doc DerApproximator/COPYING.txt
%python_sitelibdir/DerApproximator*
%exclude %python_sitelibdir/DerApproximator/tests

%files -n python-module-DerApproximator-tests
%python_sitelibdir/DerApproximator/tests

%files -n python-module-FuncDesigner
%python_sitelibdir/FuncDesigner*
%exclude %python_sitelibdir/FuncDesigner/tests
%exclude %python_sitelibdir/FuncDesigner/examples

%files -n python-module-FuncDesigner-tests
%python_sitelibdir/FuncDesigner/tests

%files -n python-module-FuncDesigner-examples
%python_sitelibdir/FuncDesigner/examples

%files -n python-module-SpaceFuncs
%python_sitelibdir/SpaceFuncs*
%exclude %python_sitelibdir/SpaceFuncs/examples
%python_sitelibdir/kernel

%files -n python-module-SpaceFuncs-examples
%python_sitelibdir/SpaceFuncs/examples

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37-alt2.svn20120206
- Avoide requirement on python-module-matplotlib-gtk

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.37-alt1.svn20120206.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37-alt1.svn20120206
- Version 0.37

* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36-alt1.svn20111210
- Version 0.36

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.34-alt1.svn20110726.1
- Rebuild with Python-2.7

* Sun Jul 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34-alt1.svn20110726
- Version 0.34

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33-alt1.svn20110325.1
- Built with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33-alt1.svn20110325
- Version 0.33
- Added SpaceFuncs package

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.31-alt1.svn20101119.1
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.31-alt1.svn20101119
- Version 0.31

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28-alt1.svn20100603
- Version 0.28

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27-alt1.svn20100303
- Version 0.27
- Rebuilt with shared libraries of PSwarm
- Extracted tests and examples into separate packages

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25-alt1.svn20090925.1
- Rebuilt with python 2.6

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25-alt1.svn20090925
- Initial build for Sisyphus (obsoletes old OpenOpt)

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt3.svn20090820.1
- Rebuilt with updated requirements

* Thu Aug 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt3.svn20090820
- Upstream changes:
  + minor change for graphic output, when last point cord has NaN (thx
    dmitrey).
  + minor changes for some examples (thx dmitrey).

* Sat Aug 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt3.svn20090808
- Upstream changes:
  + range -> xrange (thx dmitrey).
  + minor bugfix for scipy_cobyla and probably similar NLP solvers
    w/o involving gradient (thx dmitrey).

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt3.svn20090801
- Rebuild with modules: cvxopt, pswarm_py, pyipopt, pywrapper, toms_587

* Fri Jul 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt2.svn20090801.1
- New snapshot
- Fixed requirements for GUI

* Thu Jul 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt2.svn20090701
- Fixed requirements

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1.svn20090701
- Version 0.24

* Mon Apr 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1.svn20090420
- Version 0.23

* Sun Apr 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Initial build for Sisyphus
