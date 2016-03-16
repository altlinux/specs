%define oname zope.app.onlinehelp

%def_with python3

Name: python-module-%oname
Version: 3.5.2
Release: alt3.1
Summary: Framework for Context-Sensitive Help Pages
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.onlinehelp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.app.component zope.app.file
%py_requires zope.app.pagetemplate zope.app.publication
%py_requires zope.app.security zope.app.testing zope.component
%py_requires zope.configuration zope.container zope.contenttype
%py_requires zope.i18n zope.interface zope.location zope.publisher
%py_requires zope.schema zope.security zope.testing zope.traversing

%description
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

%package -n python3-module-%oname
Summary: Framework for Context-Sensitive Help Pages
Group: Development/Python3
%py3_requires ZODB3 zope.app.component zope.app.file
%py3_requires zope.app.pagetemplate zope.app.publication
%py3_requires zope.app.security zope.app.testing zope.component
%py3_requires zope.configuration zope.container zope.contenttype
%py3_requires zope.i18n zope.interface zope.location zope.publisher
%py3_requires zope.schema zope.security zope.testing zope.traversing

%description -n python3-module-%oname
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.onlinehelp
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.preference zope.app.apidoc
%py3_requires zope.site zope.login zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.securitypolicy

%description -n python3-module-%oname-tests
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

This package contains tests for zope.app.onlinehelp.

%package tests
Summary: Tests for zope.app.onlinehelp
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.preference zope.app.apidoc
%py_requires zope.site zope.login zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.securitypolicy

%description tests
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

This package contains tests for zope.app.onlinehelp.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

