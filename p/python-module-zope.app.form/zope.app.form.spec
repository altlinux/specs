%define oname zope.app.form

%def_with python3

Name: python-module-%oname
Version: 4.0.2
Release: alt4.1
Summary: The Original Zope 3 Form Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app transaction zope.formlib zope.browser
%py_requires zope.browserpage zope.browsermenu zope.component
%py_requires zope.configuration zope.datetime zope.exceptions zope.i18n
%py_requires zope.interface zope.proxy zope.publisher zope.schema
%py_requires zope.security

%description
This package provides the old form framework for Zope 3. It also
implements a few high-level ZCML directives for declaring forms. More
advanced alternatives are implemented in zope.formlib and z3c.form. The
widgets that were defined in here were moved to zope.formlib. Version
4.0 and newer are maintained for backwards compatibility reasons only.

%package -n python3-module-%oname
Summary: The Original Zope 3 Form Framework
Group: Development/Python3
%py3_requires zope.app transaction zope.formlib zope.browser
%py3_requires zope.browserpage zope.browsermenu zope.component
%py3_requires zope.configuration zope.datetime zope.exceptions zope.i18n
%py3_requires zope.interface zope.proxy zope.publisher zope.schema
%py3_requires zope.security

%description -n python3-module-%oname
This package provides the old form framework for Zope 3. It also
implements a few high-level ZCML directives for declaring forms. More
advanced alternatives are implemented in zope.formlib and z3c.form. The
widgets that were defined in here were moved to zope.formlib. Version
4.0 and newer are maintained for backwards compatibility reasons only.

%package -n python3-module-%oname-tests
Summary: Tests for The Original Zope 3 Form Framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires ZODB3 zc.sourcefactory zope.container
%py3_requires zope.principalregistry zope.site zope.traversing
%py3_requires zope.app.appsetup zope.app.publication zope.app.testing

%description -n python3-module-%oname-tests
This package provides the old form framework for Zope 3. It also
implements a few high-level ZCML directives for declaring forms. More
advanced alternatives are implemented in zope.formlib and z3c.form. The
widgets that were defined in here were moved to zope.formlib. Version
4.0 and newer are maintained for backwards compatibility reasons only.

This package contains tests for The Original Zope 3 Form Framework.

%package tests
Summary: Tests for The Original Zope 3 Form Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires ZODB3 zc.sourcefactory zope.container
%py_requires zope.principalregistry zope.site zope.traversing
%py_requires zope.app.appsetup zope.app.publication zope.app.testing

%description tests
This package provides the old form framework for Zope 3. It also
implements a few high-level ZCML directives for declaring forms. More
advanced alternatives are implemented in zope.formlib and z3c.form. The
widgets that were defined in here were moved to zope.formlib. Version
4.0 and newer are maintained for backwards compatibility reasons only.

This package contains tests for The Original Zope 3 Form Framework.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.2-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Moved all tests into tests package

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

