%define pypi_name zope.componentvocabulary

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Component vocabularies
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.componentvocabulary/
Vcs: https://github.com/zopefoundation/zope.componentvocabulary

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.security
%endif

%py3_requires zope zope.component zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.security


%description
This package contains various vocabularies.

%package tests
Summary: Tests for zope.componentvocabulary
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.component

%description tests
This package contains tests for zope.componentvocabulary.

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
%doc *.txt *.rst
%python3_sitelibdir/zope/componentvocabulary/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Version 2.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

