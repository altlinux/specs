%define oname demoapp

%def_without python3
#def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt2.git20141017
Summary: An empty app for the next-gen Services app
License: CC0 Public Domain
Group: Development/Python
Url: https://github.com/mozilla-services/demoapp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/demoapp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid_whoauth python-module-mozsvc
BuildPreReq: python-module-cef python-module-mako
BuildPreReq: python-module-markupsafe python-module-paste
BuildPreReq: python-module-PasteDeploy python-module-PasteScript
BuildPreReq: python-module-Pygments python-module-webob
BuildPreReq: python-module-pyramid-tests python-module-pyramid_debugtoolbar
BuildPreReq: python-module-repoze.lru python-module-venusian
BuildPreReq: python-module-zope.component python-module-zope.deprecation
BuildPreReq: python-module-zope.event python-module-zope.interface
BuildPreReq: python-module-pyramid_who python-module-repoze.who
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-cornice
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-3module-setuptools-tests
BuildPreReq: python3-module-pyramid_whoauth python3-module-mozsvc
BuildPreReq: python3-module-cef python3-module-mako
BuildPreReq: python3-module-markupsafe python3-module-paste
BuildPreReq: python3-module-PasteDeploy python3-module-PasteScript
BuildPreReq: python3-module-Pygments python3-module-webob
BuildPreReq: python3-module-pyramid-tests python3-module-pyramid_debugtoolbar
BuildPreReq: python3-module-repoze.lru python3-module-venusian
BuildPreReq: python3-module-zope.component python3-module-zope.deprecation
BuildPreReq: python3-module-zope.event python3-module-zope.interface
BuildPreReq: python3-module-pyramid_who python3-module-repoze.who
BuildPreReq: python3-module-unittest2 python3-module-argparse
BuildPreReq: python3-module-cornice
%endif

%py_provides %oname
%py_requires paste.deploy repoze.lru zope.component zope.deprecation
%py_requires zope.event zope.interface repoze.who

%description
An empty app for the next-gen Services app.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
An empty app for the next-gen Services app.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An empty app for the next-gen Services app
Group: Development/Python3
%py3_provides %oname
%py3_requires paste.deploy repoze.lru zope.component zope.deprecation
%py3_requires zope.event zope.interface repoze.who

%description -n python3-module-%oname
An empty app for the next-gen Services app.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
An empty app for the next-gen Services app.

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
%doc *.txt docs/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20141017
- Added necessary requirements
- Enabled testing

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141017
- Initial build for Sisyphus

