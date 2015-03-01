%define mname scikits
%define oname %mname.odes

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 2.0.2
Release: alt1.git20150123
Summary: Ordinary differential equation anddifferential algebraic equation solvers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.odes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bmcage/odes.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ gcc-fortran libsundials-devel liblapack-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy

%description
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Ordinary differential equation anddifferential algebraic equation solvers
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

This package contains tests for %oname.

%prep
%setup

for i in sundials cvode cvodes ida idas kinsol nvector
do
	rm -fR scikits/odes/sundials/$i
	ln -s %_includedir/sundials-double/$i scikits/odes/sundials/
done

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%add_optflags -I%_includedir/openblas
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
pushd ~
nosetests -v
popd
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
nosetests3 -v
popd
popd
%endif

%files
%doc README docs/src/examples
%python_sitelibdir/%mname/odes
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/odes/tests

%files tests
%python_sitelibdir/%mname/odes/tests

%if_with python3
%files -n python3-module-%oname
%doc README docs/src/examples
%python3_sitelibdir/%mname/odes
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/odes/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/odes/tests
%endif

%changelog
* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.git20150123
- Initial build for Sisyphus

