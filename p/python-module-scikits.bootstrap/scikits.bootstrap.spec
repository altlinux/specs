%define mname scikits
%define oname %mname.bootstrap

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.git20150327.1
Summary: Bootstrap confidence interval estimation routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cgevans/scikits-bootstrap.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy python-module-scipy
BuildPreReq: python-module-nose python-module-pandas
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-scipy
BuildPreReq: python3-module-nose python3-module-pandas
%endif

%py_provides %oname
%py_requires %mname numpy scipy

%description
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pandas

%description tests
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Bootstrap confidence interval estimation routines for SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pandas

%description -n python3-module-%oname-tests
Scikits.bootstrap provides bootstrap confidence interval algorithms for
scipy.

At present, it is rather feature-incomplete and in flux. However, the
functions that have been written should be relatively stable as far as
results.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/test*
%exclude %python3_sitelibdir/%mname/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/test*
%python3_sitelibdir/%mname/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150327
- New snapshot

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140521
- Initial build for Sisyphus

