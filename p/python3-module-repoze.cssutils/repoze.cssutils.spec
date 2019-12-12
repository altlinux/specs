%define oname repoze.cssutils

Name: python3-module-%oname
Version: 1.0a6
Release: alt3

Summary: CSS parsing and utilities
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.cssutils/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze nose


%description
repoze.cssutils provides css parsing and utilities for CSS 2.1 and CSS3.

%package tests
Summary: Tests for repoze.cssutils
Group: Development/Python3
Requires: %name = %version-%release

%description tests
repoze.cssutils provides css parsing and utilities for CSS 2.1 and CSS3.

This package contains tests for repoze.cssutils.

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
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0a6-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0a6-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a6-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a6-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a6-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a6-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a6-alt1
- Initial build for Sisyphus

