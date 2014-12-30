%define oname yadic

%def_with python3

Name: python-module-%oname
Version: 0.1.11
Release: alt1
Summary: Yet Another DI Container
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/yadic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Take a look to the tests for usage examples.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Take a look to the tests for usage examples.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Yet Another DI Container
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Take a look to the tests for usage examples.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Take a look to the tests for usage examples.

This package contains tests for %oname.

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

%check
python setup.py test
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt1
- Version 0.1.11

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1
- Version 0.1.9

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

