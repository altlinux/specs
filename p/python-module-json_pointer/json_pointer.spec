%define oname json_pointer

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.2.1
Summary: Simple implementation of the json-pointer spec
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/json_pointer/

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
BuildRequires: python3-module-pytest
%endif

%description
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Simple implementation of the json-pointer spec
Group: Development/Python3

%description -n python3-module-%oname
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Simple implementation of the json-pointer spec:

    http://tools.ietf.org/html/rfc6901

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

%check
python setup.py test
py.test %oname/test.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 %oname/test.py
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

