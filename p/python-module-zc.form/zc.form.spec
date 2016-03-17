%define oname zc.form

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.1
Summary: This package is a possibly temporary appendage used to hold extra browser widgets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc pytz zc.resourcelibrary zc.sourcefactory
%py_requires ZODB3 zope.annotation zope.app.principalannotation
%py_requires zope.app.catalog zope.app.form zope.app.pagetemplate
%py_requires zope.app.zapi zope.cachedescriptors zope.component
%py_requires zope.exceptions zope.formlib zope.i18n zope.i18nmessageid
%py_requires zope.index zope.interface zope.publisher zope.schema
%py_requires zope.app.security zope.app.appsetup zope.app.securitypolicy
%py_requires zope.app.testing zope.configuration zope.testing
%py_requires zope.traversing zope.app.component zope.app.zcmlfiles

%description
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

%package -n python3-module-%oname
Summary: This package is a possibly temporary appendage used to hold extra browser widgets
Group: Development/Python3
%py3_requires zc pytz zc.resourcelibrary zc.sourcefactory
%py3_requires ZODB3 zope.annotation zope.app.principalannotation
%py3_requires zope.app.catalog zope.app.form zope.app.pagetemplate
%py3_requires zope.app.zapi zope.cachedescriptors zope.component
%py3_requires zope.exceptions zope.formlib zope.i18n zope.i18nmessageid
%py3_requires zope.index zope.interface zope.publisher zope.schema
%py3_requires zope.app.security zope.app.appsetup zope.app.securitypolicy
%py3_requires zope.app.testing zope.configuration zope.testing
%py3_requires zope.traversing zope.app.component zope.app.zcmlfiles

%description -n python3-module-%oname
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

%package -n python3-module-%oname-tests
Summary: Tests for zc.form
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.interface zope.testing zope.schema zope.publisher
%py3_requires zope.formlib zope.configuration zope.component
%py3_requires zope.app.wsgi zope.browser zope.traversing
%py3_requires zope.pagetemplate

%description -n python3-module-%oname-tests
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

This package contains tests for zc.form.

%package tests
Summary: Tests for zc.form
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.interface zope.testing zope.schema zope.publisher
%py_requires zope.formlib zope.configuration zope.component
%py_requires zope.app.wsgi zope.browser zope.traversing
%py_requires zope.pagetemplate

%description tests
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

This package contains tests for zc.form.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
%doc src/zc/form/*.txt *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc src/zc/form/*.txt *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2
- Removed setuptools from requirements

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

