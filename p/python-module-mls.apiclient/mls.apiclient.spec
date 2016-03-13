%define oname mls.apiclient

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.dev.git20140714.1
Summary: Python client for the RESTful API of the Propertyshelf MLS
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mls.apiclient/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/propertyshelf/mls.apiclient.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-requests
BuildPreReq: python-module-httpretty
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-requests
BuildPreReq: python3-module-httpretty
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-mls = %EVR

%description
mls.apiclient is a Python client for the RESTful API of the
Propertyshelf MLS.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
mls.apiclient is a Python client for the RESTful API of the
Propertyshelf MLS.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python client for the RESTful API of the Propertyshelf MLS
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-mls = %EVR

%description -n python3-module-%oname
mls.apiclient is a Python client for the RESTful API of the
Propertyshelf MLS.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
mls.apiclient is a Python client for the RESTful API of the
Propertyshelf MLS.

This package contains tests for %oname.

%package -n python-module-mls
Summary: Core files of mls
Group: Development/Python
%py_provides mls

%description -n python-module-mls
Core files of mls.

%package -n python3-module-mls
Summary: Core files of mls
Group: Development/Python3
%py3_provides mls

%description -n python3-module-mls
Core files of mls.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/mls/__init__.py \
	%buildroot%python_sitelibdir/mls/
cp -fR src/mls/apiclient/tests/fixtures \
	%buildroot%python_sitelibdir/mls/apiclient/tests/
%if_with python3
pushd ../python3
install -p -m644 src/mls/__init__.py \
	%buildroot%python3_sitelibdir/mls/
cp -fR src/mls/apiclient/tests/fixtures \
	%buildroot%python3_sitelibdir/mls/apiclient/tests/
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
%doc *.rst docs/*
%python_sitelibdir/mls/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/mls/*/tests
%exclude %python_sitelibdir/mls/__init__.py*

%files tests
%python_sitelibdir/mls/*/tests

%files -n python-module-mls
%dir %python_sitelibdir/mls
%python_sitelibdir/mls/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*
%python3_sitelibdir/mls/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/mls/*/tests
%exclude %python3_sitelibdir/mls/__init__.py
%exclude %python3_sitelibdir/mls/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/mls/*/tests

%files -n python3-module-mls
%dir %python3_sitelibdir/mls
%dir %python3_sitelibdir/mls/__pycache__
%python3_sitelibdir/mls/__init__.py
%python3_sitelibdir/mls/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.dev.git20140714.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev.git20140714
- Initial build for Sisyphus

