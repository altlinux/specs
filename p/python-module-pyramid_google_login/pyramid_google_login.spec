%define oname pyramid_google_login

%def_without python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Google Login for Pyramid
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_google_login/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-d2to1
BuildPreReq: python-module-requests python-module-pyramid_mako
BuildPreReq: python-module-mako python-module-markupsafe
BuildPreReq: python-module-mock python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-d2to1
BuildPreReq: python3-module-requests python3-module-pyramid_mako
BuildPreReq: python3-module-mako python3-module-markupsafe
BuildPreReq: python3-module-mock python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Google Login extension for Pyramid. Implement the OAuth2 Server-side
flow.

This extension doesn't configure any authentication policy. You are
responsible of setting the proper security configuration in your Pyramid
application. When authenticated by Google, this extension calls the
method pyramid.security.remember and assume the authentication policy
will remember the user identity.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.tests

%description tests
Google Login extension for Pyramid. Implement the OAuth2 Server-side
flow.

This extension doesn't configure any authentication policy. You are
responsible of setting the proper security configuration in your Pyramid
application. When authenticated by Google, this extension calls the
method pyramid.security.remember and assume the authentication policy
will remember the user identity.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Google Login for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Google Login extension for Pyramid. Implement the OAuth2 Server-side
flow.

This extension doesn't configure any authentication policy. You are
responsible of setting the proper security configuration in your Pyramid
application. When authenticated by Google, this extension calls the
method pyramid.security.remember and assume the authentication policy
will remember the user identity.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.tests

%description -n python3-module-%oname-tests
Google Login extension for Pyramid. Implement the OAuth2 Server-side
flow.

This extension doesn't configure any authentication policy. You are
responsible of setting the proper security configuration in your Pyramid
application. When authenticated by Google, this extension calls the
method pyramid.security.remember and assume the authentication policy
will remember the user identity.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

