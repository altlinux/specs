%define oname repoze.who.plugins.formcookie

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt2.1
Summary: Stores came_from in cookie instead of url query string
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.formcookie/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.who.plugins paste repoze.who zope.interface

%description
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

%package -n python3-module-%oname
Summary: Stores came_from in cookie instead of url query string
Group: Development/Python3
%py3_requires repoze.who.plugins paste repoze.who zope.interface

%description -n python3-module-%oname
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.formcookie
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires webob webtest nose repoze.who.tests

%description -n python3-module-%oname-tests
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

This package contains tests for repoze.who.plugins.formcookie.

%package tests
Summary: Tests for repoze.who.plugins.formcookie
Group: Development/Python
Requires: %name = %version-%release
%py_requires webob webtest nose repoze.who.tests

%description tests
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

This package contains tests for repoze.who.plugins.formcookie.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

