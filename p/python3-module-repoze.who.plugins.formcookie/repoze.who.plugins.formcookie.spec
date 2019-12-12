%define oname repoze.who.plugins.formcookie

Name: python3-module-%oname
Version: 0.3.0
Release: alt3

Summary: Stores came_from in cookie instead of url query string
License: Free
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.who.plugins.formcookie/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires repoze.who.plugins paste repoze.who zope.interface


%description
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

%package tests
Summary: Tests for repoze.who.plugins.formcookie
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires webob webtest nose repoze.who.tests

%description tests
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

This package contains tests for repoze.who.plugins.formcookie.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

