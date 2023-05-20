%define pypi_name zope.cachedescriptors

%def_with check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt1

Summary: Method and property caching decorators
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.cachedescriptors/
Vcs: https://github.com/zopefoundation/zope.cachedescriptors

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope


%description
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

%package tests
Summary: Tests for zope.cachedescriptors
Group: Development/Python3
Requires: %name = %EVR

%description tests
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

This package contains tests for zope.cachedescriptors.

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
%tox_check_pyproject

%files
%doc *.txt *.rst
%python3_sitelibdir/zope/cachedescriptors/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt2
- Build for python2 disabled.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3.1-alt1
- new version 4.3.1 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150204.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150204.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150204
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

