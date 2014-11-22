%define oname pyramid_oauthlib

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.dev.git20141121
Summary: Pyramid OAuthLib integration
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_oauthlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tilgovi/pyramid-oauthlib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-oauthlib
BuildPreReq: python-module-mock python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-oauthlib
BuildPreReq: python3-module-mock python3-module-pytest-cov
%endif

%py_provides %oname

%description
Pyramid OAuthLib is a library to integrate the excellent OAuthLib
library easily into Pyramid applications. It is designed to ease
development of OAuth applications, provide smooth migration possibilites
to legacy codebases using other authentication or authorization schemes,
and configuration patterns for creating pluggable OAuth components for
Pyramid.

NOTICE: Pyramid OAuthLib is not feature complete! It is missing the
hooks for token revocation. While this shouldn't be hard to add, it
wasn't a priority to get the initial version released.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
Pyramid OAuthLib is a library to integrate the excellent OAuthLib
library easily into Pyramid applications. It is designed to ease
development of OAuth applications, provide smooth migration possibilites
to legacy codebases using other authentication or authorization schemes,
and configuration patterns for creating pluggable OAuth components for
Pyramid.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid OAuthLib integration
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pyramid OAuthLib is a library to integrate the excellent OAuthLib
library easily into Pyramid applications. It is designed to ease
development of OAuth applications, provide smooth migration possibilites
to legacy codebases using other authentication or authorization schemes,
and configuration patterns for creating pluggable OAuth components for
Pyramid.

NOTICE: Pyramid OAuthLib is not feature complete! It is missing the
hooks for token revocation. While this shouldn't be hard to add, it
wasn't a priority to get the initial version released.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
Pyramid OAuthLib is a library to integrate the excellent OAuthLib
library easily into Pyramid applications. It is designed to ease
development of OAuth applications, provide smooth migration possibilites
to legacy codebases using other authentication or authorization schemes,
and configuration patterns for creating pluggable OAuth components for
Pyramid.

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
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.dev.git20141121
- Initial build for Sisyphus

