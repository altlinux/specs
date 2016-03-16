%define oname z3c.widget

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt3.1
Summary: Additional zope.formlib Widgets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.widget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 z3c.i18n z3c.javascript z3c.schema zc.resourcelibrary
%py_requires zope.app.cache zope.app.container zope.app.file
%py_requires zope.app.i18n zope.app.pagetemplate zope.component
%py_requires zope.event zope.filerepresentation zope.formlib zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.publisher zope.schema zope.security zope.traversing

%description
Additional zope.formlib Widgets.

%package -n python3-module-%oname
Summary: Additional zope.formlib Widgets
Group: Development/Python3
%py3_requires ZODB3 z3c.i18n z3c.javascript z3c.schema zc.resourcelibrary
%py3_requires zope.app.cache zope.app.container zope.app.file
%py3_requires zope.app.i18n zope.app.pagetemplate zope.component
%py3_requires zope.event zope.filerepresentation zope.formlib zope.i18n
%py3_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py3_requires zope.publisher zope.schema zope.security zope.traversing

%description -n python3-module-%oname
Additional zope.formlib Widgets.

%package -n python3-module-%oname-tests
Summary: Tests for Additional zope.formlib Widgets
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.testbrowser

%description -n python3-module-%oname-tests
Additional zope.formlib Widgets.

This package contains tests for Additional zope.formlib Widgets.

%package tests
Summary: Tests for Additional zope.formlib Widgets
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
Additional zope.formlib Widgets.

This package contains tests for Additional zope.formlib Widgets.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

