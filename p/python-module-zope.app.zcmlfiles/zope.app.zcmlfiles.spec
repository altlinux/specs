%define oname zope.app.zcmlfiles

%def_with python3

Name: python-module-%oname
Version: 3.8.0
Release: alt2.1
Summary: Zope application server ZCML files
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.zcmlfiles
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.annotation zope.component zope.componentvocabulary
%py_requires zope.copypastemove zope.dublincore zope.formlib zope.i18n
%py_requires zope.location zope.publisher zope.size zope.traversing
%py_requires zope.app.applicationcontrol zope.app.appsetup
%py_requires zope.app.basicskin zope.app.broken zope.app.component
%py_requires zope.app.container zope.app.content zope.app.dependable
%py_requires zope.app.error zope.app.exception zope.app.folder
%py_requires zope.app.form zope.app.generations zope.app.http
%py_requires zope.app.i18n zope.app.locales zope.app.pagetemplate 
%py_requires zope.app.principalannotation zope.app.publication zope.app
%py_requires zope.app.publisher zope.app.rotterdam zope.app.schema 
%py_requires zope.app.security zope.app.wsgi zope.app.zopeappgenerations

%description
Zope application server ZCML files.

%package -n python3-module-%oname
Summary: Zope application server ZCML files
Group: Development/Python3
%py3_requires zope.annotation zope.component zope.componentvocabulary
%py3_requires zope.copypastemove zope.dublincore zope.formlib zope.i18n
%py3_requires zope.location zope.publisher zope.size zope.traversing
%py3_requires zope.app.applicationcontrol zope.app.appsetup
%py3_requires zope.app.basicskin zope.app.broken zope.app.component
%py3_requires zope.app.container zope.app.content zope.app.dependable
%py3_requires zope.app.error zope.app.exception zope.app.folder
%py3_requires zope.app.form zope.app.generations zope.app.http
%py3_requires zope.app.i18n zope.app.locales zope.app.pagetemplate 
%py3_requires zope.app.principalannotation zope.app.publication zope.app
%py3_requires zope.app.publisher zope.app.rotterdam zope.app.schema 
%py3_requires zope.app.security zope.app.wsgi zope.app.zopeappgenerations

%description -n python3-module-%oname
Zope application server ZCML files.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.zcmlfiles
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
Zope application server ZCML files.

This package contains tests for zope.app.zcmlfiles.

%package tests
Summary: Tests for zope.app.zcmlfiles
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Zope application server ZCML files.

This package contains tests for zope.app.zcmlfiles.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.8.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Disabled .pth
- Added necessary requirements

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

