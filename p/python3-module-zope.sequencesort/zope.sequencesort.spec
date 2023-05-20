%define pypi_name zope.sequencesort

%def_with check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt1

Summary: Sequence Sorting
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.sequencesort/
Vcs: https://github.com/zopefoundation/zope.sequencesort

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope


%description
This package provides support for sorting sequences based on multiple keys,
including locale-based comparisons and per-key directions.

%package tests
Summary: Tests for zope.sequencesort
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
This package provides support for sorting sequences based on multiple keys,
including locale-based comparisons and per-key directions.

This package contains tests for zope.sequencesort.

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
%doc CHANGES.rst LICENSE.txt README.rst
%python3_sitelibdir/zope/sequencesort/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version  5.0.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt3
- Fixed BuildRequires.

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev.git20141106.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev.git20141106.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev.git20141106.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev.git20141106
- Version 4.0.2dev
- Enabled check

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

