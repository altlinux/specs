%define oname pyramid_hawkauth

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.dev1.git20140324
Summary: Hawk Access Auth plugin for pyramid
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_hawkauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/pyramid_hawkauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-hawkauthlib
BuildPreReq: python-module-tokenlib python-module-webtest
BuildPreReq: python-module-PasteDeploy python-module-zope.deprecation
BuildPreReq: python-module-zope.interface python-module-repoze.lru
BuildPreReq: python-module-zope.component
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-hawkauthlib
BuildPreReq: python3-module-tokenlib python3-module-webtest
BuildPreReq: python3-module-PasteDeploy python3-module-zope.deprecation
BuildPreReq: python3-module-zope.interface python3-module-repoze.lru
BuildPreReq: python3-module-zope.component
%endif

%py_provides %oname
%py_requires zope.interface

%description
This is a Pyramid authenitcation plugin for Hawk Access Authentication:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and secret key.
They use these credentials to make signed requests to the server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a Pyramid authenitcation plugin for Hawk Access Authentication:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and secret key.
They use these credentials to make signed requests to the server.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Hawk Access Auth plugin for pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a Pyramid authenitcation plugin for Hawk Access Authentication:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and secret key.
They use these credentials to make signed requests to the server.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a Pyramid authenitcation plugin for Hawk Access Authentication:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and secret key.
They use these credentials to make signed requests to the server.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%endif

%changelog
* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.dev1.git20140324
- Initial build for Sisyphus

