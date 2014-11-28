%define oname jsmin

%def_with python3

Name: python-module-%oname
Version: 2.0.11
Release: alt1
Summary: JavaScript minifier
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsmin/
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
JavaScript minifier.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JavaScript minifier.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JavaScript minifier
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JavaScript minifier.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JavaScript minifier.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.11-alt1
- Initial build for Sisyphus

