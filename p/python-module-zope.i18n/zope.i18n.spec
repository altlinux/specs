%define oname zope.i18n

%def_with python3

Name: python-module-%oname
Version: 3.8.0
Release: alt1
Summary: Zope Internationalization Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18n
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-zope python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-zope python-tools-2to3
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
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
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

