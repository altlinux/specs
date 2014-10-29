%define oname pyramid_whoauth

%def_without python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20120528
Summary: A pyramid authentication policy using repoze.who
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_whoauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/pyramid_whoauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-unittest2
BuildPreReq: python-module-repoze.who python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation python-module-repoze.lru
BuildPreReq: python-module-zope.component
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-unittest2
BuildPreReq: python3-module-repoze.who python3-module-PasteDeploy
BuildPreReq: python3-module-zope.deprecation python3-module-repoze.lru
BuildPreReq: python3-module-zope.component python3-module-unittest2
%endif

%py_provides %oname
%py_requires repoze.who zope.interface

%description
This plugin allows you to configure a repoze.who authentication stack as
a pyramid authentication policy. It takes a repoze.who API factory and
turns it into an pyramid IAuthenticationPolicy.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This plugin allows you to configure a repoze.who authentication stack as
a pyramid authentication policy. It takes a repoze.who API factory and
turns it into an pyramid IAuthenticationPolicy.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A pyramid authentication policy using repoze.who
Group: Development/Python3
%py3_provides %oname
%py3_requires repoze.who zope.interface

%description -n python3-module-%oname
This plugin allows you to configure a repoze.who authentication stack as
a pyramid authentication policy. It takes a repoze.who API factory and
turns it into an pyramid IAuthenticationPolicy.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This plugin allows you to configure a repoze.who authentication stack as
a pyramid authentication policy. It takes a repoze.who API factory and
turns it into an pyramid IAuthenticationPolicy.

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
* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20120528
- Initial build for Sisyphus

