%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.i18n

%def_with python3

Name: python-module-%oname
Version: 4.1.0
#Release: alt1.1.1
Summary: Zope Internationalization Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18n
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/52/16/846c445fe3009b9180618145b86aeebc1c851a3da1cb9893a51c8b45d567/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-zope python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-zope.interface
BuildRequires: python-module-setuptools python3-module-setuptools python3-module-zope rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-zope python-tools-2to3
%endif

%py_requires zope pytz zope.schema zope.i18nmessageid zope.component

%description
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%if_with python3
%package -n python3-module-%oname
Summary: Zope Internationalization Support (Python 3)
Group: Development/Python3
%py3_requires zope pytz zope.schema zope.i18nmessageid zope.component

%description -n python3-module-%oname
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%package -n python3-module-%oname-tests
Summary: Tests for zope.i18n (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.component.testing

%description -n python3-module-%oname-tests
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

This package contains tests for zope.i18n.
%endif

%package tests
Summary: Tests for zope.i18n
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

This package contains tests for zope.i18n.

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
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

