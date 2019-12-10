%define _unpackaged_files_terminate_build 1

%define oname repoze.tm2

Name: python3-module-%oname
Version: 2.1
Release: alt2

Summary: WSGI middleware: commit / abort transactions
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.tm2

# https://github.com/repoze/repoze.tm2.git
Source0: https://pypi.python.org/packages/25/16/991e1f2658383e8d17c17e49b424ed2537fd635a276524940d7f50d18a61/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides repoze.tm2
%py3_requires repoze transaction


%description
Middleware which uses the ZODB transaction manager to wrap a call to
its pipeline children inside a transaction.  This is a fork of the
``repoze.tm`` package which depends only on the ``transaction``
package rather than the entirety of ZODB (for users who don't rely on
ZODB).

%package tests
Summary: Tests for repoze.tm2
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Middleware which uses the ZODB transaction manager to wrap a call to
its pipeline children inside a transaction.  This is a fork of the
``repoze.tm`` package which depends only on the ``transaction``
package rather than the entirety of ZODB (for users who don't rely on
ZODB).

This package contains tests for repoze.tm2.

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.git20130626.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.git20130626.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.git20130626
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20130626
- Version 2.0

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20120324
- Version 1.1

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1.git20110718
- Version 1.0b2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1.git20110225
- Initial build for Sisyphus

