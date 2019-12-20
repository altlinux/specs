%define _unpackaged_files_terminate_build 1
%define oname zope.i18n

%def_with check

Name: python3-module-%oname
Version: 4.7.0
Release: alt1

Summary: Zope Internationalization Support
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.i18n
#Git: https://github.com/zopefoundation/zope.i18n.git

Source: %name-%version.tar
Patch0: %oname-fix-tests.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
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

%py3_requires zope.deprecation
%py3_requires zope.schema
%py3_requires zope.i18nmessageid
%py3_requires zope.component
%py3_requires zope.deferredimport
%py3_requires zope.hookable

%description
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%package tests
Summary: Tests for zope.i18n (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-zope.component-tests
%py3_requires zope.publisher
%py3_requires zope.testrunner

%description tests
This package contains tests for %oname.

%prep
%setup
%patch0 -p2

%build
%python3_build

%install
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
export PYTHONPATH=src
zope-testrunner3 --test-path=src -vv

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/i18n/testing.*
%exclude %python3_sitelibdir/zope/i18n/*/testing.*
%exclude %python3_sitelibdir/zope/i18n/tests
%exclude %python3_sitelibdir/zope/i18n/locales/tests

%files tests
%python3_sitelibdir/zope/i18n/testing.*
%python3_sitelibdir/zope/i18n/*/testing.*
%python3_sitelibdir/zope/i18n/tests
%python3_sitelibdir/zope/i18n/locales/tests

%changelog
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.7.0-alt1
- NMU: 4.6.2 -> 4.7.0
- Remove python2 module build
- Remove ubt tag from changelog
- Enable check

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Mon Apr 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt3
- requires for tests fixed

* Fri Mar 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt2
- py3 requires fixed

* Thu Mar 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt1
- Version updated to 4.6.2

* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 4.3.1-alt1
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

