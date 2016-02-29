%define mname scikits
%define oname %mname.bvp_solver

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt3.git20120926.1
Summary: Python package for solving two-point boundary value problems
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.bvp_solver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jsalvatier/scikits.bvp_solver.git
Source: %name-%version.tar

#BuildPreReq: gcc-fortran
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose libnumpy-devel
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose libnumpy-py3-devel
%endif

%py_provides %oname
%py_requires %mname numpy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libgfortran-devel libnumpy-devel libquadmath-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib python-module-numpy python-module-numpydoc python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-dev python3-module-numpy python3-module-setuptools
BuildRequires: gcc-fortran libnumpy-py3-devel python-module-alabaster python-module-html5lib python-module-nose python-module-numpy-testing python-module-objects.inv python-module-setuptools-tests python3-module-nose python3-module-numpy-testing python3-module-pytest rpm-build-python3 time

%description
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

%package tests
Summary: Tests and examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

This package contains tests and examples for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python package for solving two-point boundary value problems
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy

%description -n python3-module-%oname
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

%package -n python3-module-%oname-tests
Summary: Tests and examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

This package contains tests and examples for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
scikits.bvp_solver is a python package for solving two point boundary
value problems which is based on a modified version of the BVP_SOLVER
Fortran package.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
mv %buildroot%python_sitelibdir/%mname/bvp_solver/%mname/bvp_solver/examples \
	%buildroot%python_sitelibdir/%mname/bvp_solver/

%if_with python3
pushd ../python3
%python3_install
mv %buildroot%python3_sitelibdir/%mname/bvp_solver/%mname/bvp_solver/examples \
	%buildroot%python3_sitelibdir/%mname/bvp_solver/
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/examples

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests
%exclude %python3_sitelibdir/%mname/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/tests
%python3_sitelibdir/%mname/*/examples
%endif

%changelog
* Mon Feb 29 2016 Denis Medvedev <nbr@altlinux.org> 1.1-alt3.git20120926.1
- just rebuild.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt2.git20120926.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.git20120926
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20120926
- Initial build for Sisyphus

