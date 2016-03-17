%define oname zope.app.apidoc

%def_with python3

Name: python-module-%oname
Version: 3.7.5
Release: alt3.1
Summary: API Documentation and Component Inspection for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.apidoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py_requires zope.app.basicskin zope.app.onlinehelp zope.app.preference
%py_requires zope.app.publisher zope.app.renderer zope.app.testing
%py_requires zope.app.tree zope.cachedescriptors zope.component
%py_requires zope.container zope.configuration zope.deprecation
%py_requires zope.i18n zope.site zope.hookable zope.interface
%py_requires zope.location zope.proxy zope.publisher zope.schema
%py_requires zope.security zope.testbrowser zope.testing zope.traversing

%description
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

%package -n python3-module-%oname
Summary: API Documentation and Component Inspection for Zope 3
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py3_requires zope.app.basicskin zope.app.onlinehelp zope.app.preference
%py3_requires zope.app.publisher zope.app.renderer zope.app.testing
%py3_requires zope.app.tree zope.cachedescriptors zope.component
%py3_requires zope.container zope.configuration zope.deprecation
%py3_requires zope.i18n zope.site zope.hookable zope.interface
%py3_requires zope.location zope.proxy zope.publisher zope.schema
%py3_requires zope.security zope.testbrowser zope.testing zope.traversing

%description -n python3-module-%oname
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.apidoc
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py3_requires zope.browserpage zope.securitypolicy zope.login

%description -n python3-module-%oname-tests
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

This package contains tests for zope.app.apidoc.

%package tests
Summary: Tests for zope.app.apidoc
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.browserpage zope.securitypolicy zope.login

%description tests
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

This package contains tests for zope.app.apidoc.

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
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*
%python_sitelibdir/*/*/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.5-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt1
- Initial build for Sisyphus

