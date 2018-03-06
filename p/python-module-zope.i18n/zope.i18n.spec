%define _unpackaged_files_terminate_build 1
%define oname zope.i18n

%def_with check

Name: python-module-%oname
Version: 4.3.1
Release: alt1%ubt

Summary: Zope Internationalization Support
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.i18n.git
Url: http://pypi.python.org/pypi/zope.i18n

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-gettext
BuildRequires: python-module-pytz
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.component-tests
BuildRequires: python-module-zope.i18nmessageid
BuildRequires: python-module-zope.schema
BuildRequires: python-module-zope.deprecation
BuildRequires: python-module-zope.publisher
BuildRequires: python3-module-gettext
BuildRequires: python3-module-pytz
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.i18nmessageid
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.deprecation
BuildRequires: python3-module-zope.publisher
%endif

%py_requires zope.deprecation
%py_requires zope.schema
%py_requires zope.i18nmessageid
%py_requires zope.component

%description
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%package -n python3-module-%oname
Summary: Zope Internationalization Support (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%package -n python3-module-%oname-tests
Summary: Tests for zope.i18n (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.publisher

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for zope.i18n
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing
%py_requires zope.publisher

%description tests
This package contains tests for %oname.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
export PYTHONPATH=src
zope-testrunner --test-path=src -vv

pushd ../python3
zope-testrunner3 --test-path=src -vv
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/i18n/testing.*
%exclude %python_sitelibdir/zope/i18n/tests
%exclude %python_sitelibdir/zope/i18n/locales/tests

%files tests
%python_sitelibdir/zope/i18n/testing.*
%python_sitelibdir/zope/i18n/tests
%python_sitelibdir/zope/i18n/locales/tests

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/i18n/testing.*
%exclude %python3_sitelibdir/zope/i18n/*/testing.*
%exclude %python3_sitelibdir/zope/i18n/tests
%exclude %python3_sitelibdir/zope/i18n/locales/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/i18n/testing.*
%python3_sitelibdir/zope/i18n/*/testing.*
%python3_sitelibdir/zope/i18n/tests
%python3_sitelibdir/zope/i18n/locales/tests

%changelog
* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 4.3.1-alt1%ubt
- 4.1.0 -> 4.3.1

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.8.0-alt1.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

