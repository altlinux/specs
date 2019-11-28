%define oname zope.fixers

Name: python3-module-%oname
Version: 1.1.2
Release: alt2

Summary: 2to3 fixers for Zope
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.fixers/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope

%description
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

%package tests
Summary: Tests for zope.fixers
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

This package contains tests for zope.fixers.

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.2-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 01 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

