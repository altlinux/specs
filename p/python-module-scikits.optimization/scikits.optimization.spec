%define mname scikits
%define oname %mname.optimization

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.3
Release: alt3.git20130417
Summary: A python module for numerical optimization
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.optimization/

# https://github.com/mbrucher/scikit-optimization.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-nose libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-nose libnumpy-py3-devel
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname numpy

%description
This package's goal is to provide a generic optimization framework.

It currently deals with unconstrained optimnization routines based on
line searches.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
This package's goal is to provide a generic optimization framework.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A python module for numerical optimization
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy

%description -n python3-module-%oname
This package's goal is to provide a generic optimization framework.

It currently deals with unconstrained optimnization routines based on
line searches.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
This package's goal is to provide a generic optimization framework.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
nosetests -v

%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/%mname/optimization
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/optimization/tests
%exclude %python_sitelibdir/%mname/optimization/*/tests

%files tests
%python_sitelibdir/%mname/optimization/tests
%python_sitelibdir/%mname/optimization/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/optimization
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/optimization/tests
%exclude %python3_sitelibdir/%mname/optimization/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/optimization/tests
%python3_sitelibdir/%mname/optimization/*/tests
%endif

%changelog
* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.3-alt3.git20130417
- Fixed check.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.3-alt2.git20130417.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.3-alt2.git20130417.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt2.git20130417
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt1.git20130417
- Initial build for Sisyphus

