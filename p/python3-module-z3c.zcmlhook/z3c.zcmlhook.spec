%define oname z3c.zcmlhook

Name: python3-module-%oname
Version: 1.0b1
Release: alt4

Summary: Easily hook into the ZCML processing machinery
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.zcmlhook/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires zope.component zope.interface zope.schema
%py3_requires zope.configuration


%description
This package provides means of hooking into the Zope (ZCML)
configuration process.

%package tests
Summary: Tests for z3c.zcmlhook
Group: Development/Python
Requires: %name = %version-%release
%py3_requires nose

%description tests
This package provides means of hooking into the Zope (ZCML)
configuration process.

This package contains tests for z3c.zcmlhook.

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
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0b1-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0b1-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b1-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

