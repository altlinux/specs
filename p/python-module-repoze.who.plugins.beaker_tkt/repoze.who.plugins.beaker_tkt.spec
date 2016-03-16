%define oname repoze.who.plugins.beaker_tkt

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt4.1
Summary: Identifier (auth_tkt) plugin with beaker.session cache implementation
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.beaker_tkt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who.plugins paste.script beaker repoze.who

%description
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

%package -n python3-module-%oname
Summary: Identifier (auth_tkt) plugin with beaker.session cache implementation
Group: Development/Python3
%py3_requires repoze.who.plugins paste.script beaker repoze.who

%description -n python3-module-%oname
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.beaker_tkt
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires webob webtest nose

%description -n python3-module-%oname-tests
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

This package contains tests for repoze.who.plugins.beaker_tkt.

%package tests
Summary: Tests for repoze.who.plugins.beaker_tkt
Group: Development/Python
Requires: %name = %version-%release
%py_requires webob webtest nose

%description tests
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

This package contains tests for repoze.who.plugins.beaker_tkt.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/__init__.*
%exclude %python_sitelibdir/*/*/*/__init__.*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/__init__.*
%exclude %python3_sitelibdir/*/*/__init__.*
%exclude %python3_sitelibdir/*/*/*/__init__.*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Avoid conflict with python-module-repoze.who (previous stage doesn't
  completed)

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Avoid conflict with python-module-repoze.who

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

