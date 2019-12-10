%define oname repoze.urchin

Name: python3-module-%oname
Version: 0.2
Release: alt3

Summary: WSGI middleware for Google analytics
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.urchin/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires repoze webob


%description
This package provides WSGI middleware for injecting the markup required
to use Google Analytics into web pages.

%package tests
Summary: Tests for repoze.urchin
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides WSGI middleware for injecting the markup required
to use Google Analytics into web pages.

This package contains tests for repoze.urchin.

%prep
%setup

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
%doc *.txt docs/*.rst docs/*.ini
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

