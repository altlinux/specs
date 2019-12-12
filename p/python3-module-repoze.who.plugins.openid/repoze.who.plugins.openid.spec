%define oname repoze.who.plugins.openid

Name: python3-module-%oname
Version: 0.5.3
Release: alt3

Summary: An OpenID plugin for repoze.who
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.who.plugins.openid/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze.who.plugins openid webob zope.interface repoze.who


%description
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

%package tests
Summary: Tests for repoze.who.plugins.openid
Group: Development/Python3
Requires: %name = %version-%release

%description tests
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

This package contains tests for repoze.who.plugins.openid.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

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
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/*/*/tests


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.3-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

