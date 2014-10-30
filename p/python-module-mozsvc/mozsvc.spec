%define oname mozsvc

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.9
Release: alt2.dev.git20140915
Summary: Various utilities for Mozilla apps
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozsvc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/mozservices.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-simplejson
BuildPreReq: python-module-konfig python-module-umemcache
BuildPreReq: python-module-pyramid_hawkauth python-module-tokenlib
BuildPreReq: python-module-hawkauthlib python-module-wsgiproxy
BuildPreReq: python-module-unittest2 python-module-webtest
BuildPreReq: python-module-gunicorn python-module-gevent
BuildPreReq: python-module-testfixtures python-module-zope.interface
BuildPreReq: python-module-argparse python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation python-module-repoze.lru
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-cornice
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-simplejson
BuildPreReq: python3-module-konfig
BuildPreReq: python3-module-pyramid_hawkauth python3-module-tokenlib
BuildPreReq: python3-module-hawkauthlib python3-module-wsgiproxy
BuildPreReq: python3-module-unittest2 python3-module-webtest
BuildPreReq: python3-module-gunicorn python3-module-gevent
BuildPreReq: python3-module-testfixtures python3-module-zope.interface
BuildPreReq: python3-module-argparse python3-module-PasteDeploy
BuildPreReq: python3-module-zope.deprecation python3-module-repoze.lru
BuildPreReq: python3-module-zope.component
BuildPreReq: python3-module-cornice
%endif

%py_provides %oname
%py_requires zope.interface

%description
Various utilities for Pyramid-based Mozilla applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Various utilities for Pyramid-based Mozilla applications.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Various utilities for Mozilla apps
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface

%description -n python3-module-%oname
Various utilities for Pyramid-based Mozilla applications.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Various utilities for Pyramid-based Mozilla applications.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.dev.git20140915
- Added necessaary requirements

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.dev.git20140915
- Initial build for Sisyphus

