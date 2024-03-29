%define oname z3c.zcmlhook

%def_with check

Name: python3-module-%oname
Version: 2.0
Release: alt2

Summary: Easily hook into the ZCML processing machinery
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/z3c.zcmlhook/
Vcs: https://github.com/zopefoundation/z3c.zcmlhook

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.testrunner
%endif

%description
This package provides means of hooking into the Zope (ZCML)
configuration process.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides means of hooking into the Zope (ZCML)
configuration process.

This package contains tests for z3c.zcmlhook.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst *.md
%python3_sitelibdir/z3c/zcmlhook/
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 2.0-alt2
- Fixed FTBFS.

* Sat Apr 01 2023 Anton Vyatkin <toni@altlinux.org> 2.0-alt1
- New version 2.0

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

