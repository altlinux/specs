%define oname osiris

%def_without python3

Name: python-module-%oname
Version: 1.4
Release: alt1.dev0.git20140723
Summary: Pyramid based oAuth server
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/osiris/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sneridagh/osiris.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests
BuildPreReq: python-module-pyramid_who python-module-pymongo
BuildPreReq: python-module-waitress python-module-WSGIProxy2
BuildPreReq: python-module-webtest python-module-pyramid_ldap
BuildPreReq: python-module-repoze.lru python-module-Pygments
BuildPreReq: python-module-pyramid_mako python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation python-module-mako
BuildPreReq: python-module-markupsafe python-module-zope.component
BuildPreReq: python-module-pyramid_debugtoolbar
BuildPreReq: python-module-ldap
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests
BuildPreReq: python3-module-pyramid_who python3-module-pymongo
BuildPreReq: python3-module-waitress python3-module-WSGIProxy2
BuildPreReq: python3-module-webtest python3-module-pyramid_debugtoolbar
BuildPreReq: python3-module-repoze.lru python3-module-Pygments
BuildPreReq: python3-module-pyramid_mako python3-module-PasteDeploy
BuildPreReq: python3-module-zope.deprecation python3-module-mako
BuildPreReq: python3-module-markupsafe python3-module-zope.component
BuildPreReq: python3-module-ldap python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-WSGIProxy2

%description
Osiris is an oAuth 2.0 compliant server based on Pyramid. The current
version (1.0) it supports the resource owner password credentials
authentication flow. You can use your preferred authentication backend
(LDAP, SQL, etc.) in order to oAuth enable it with Osiris. You can also
use your preferred backend storage as Osiris uses a pluggable store
factory to store the issued token information. The current version
includes the MongoDB one.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Osiris is an oAuth 2.0 compliant server based on Pyramid. The current
version (1.0) it supports the resource owner password credentials
authentication flow. You can use your preferred authentication backend
(LDAP, SQL, etc.) in order to oAuth enable it with Osiris. You can also
use your preferred backend storage as Osiris uses a pluggable store
factory to store the issued token information. The current version
includes the MongoDB one.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid based oAuth server
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-WSGIProxy2

%description -n python3-module-%oname
Osiris is an oAuth 2.0 compliant server based on Pyramid. The current
version (1.0) it supports the resource owner password credentials
authentication flow. You can use your preferred authentication backend
(LDAP, SQL, etc.) in order to oAuth enable it with Osiris. You can also
use your preferred backend storage as Osiris uses a pluggable store
factory to store the issued token information. The current version
includes the MongoDB one.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Osiris is an oAuth 2.0 compliant server based on Pyramid. The current
version (1.0) it supports the resource owner password credentials
authentication flow. You can use your preferred authentication backend
(LDAP, SQL, etc.) in order to oAuth enable it with Osiris. You can also
use your preferred backend storage as Osiris uses a pluggable store
factory to store the issued token information. The current version
includes the MongoDB one.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev0.git20140723
- Initial build for Sisyphus

