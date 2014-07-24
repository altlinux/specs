%define oname z3c.skin.pagelet

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt4
Summary: A base skin for pagelet-based UIs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.skin.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app.component zope.app.pagetemplate zope.app.publisher
%py_requires zope.app.container zope.app.securitypolicy zope.app.testing
%py_requires zope.app.twisted zope.app.zapi zope.contentprovider
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema
%py_requires zope.security zope.testing zope.traversing zope.viewlet
%py_requires z3c.i18n z3c.layer z3c.macro z3c.macroviewlet
%py_requires z3c.pagelet z3c.template z3c.viewlet z3c.zrtresource
%py_requires z3c.menu.simple
Requires: python-module-z3c.skin = %EVR

%description
This package provides a base skin for people wanting to develop
pagelet-based applications.

%package -n python3-module-%oname
Summary: A base skin for pagelet-based UIs
Group: Development/Python3
%py3_requires zope.app.component zope.app.pagetemplate zope.app.publisher
%py3_requires zope.app.container zope.app.securitypolicy zope.app.testing
%py3_requires zope.app.twisted zope.app.zapi zope.contentprovider
%py3_requires zope.i18n zope.i18nmessageid zope.interface zope.schema
%py3_requires zope.security zope.testing zope.traversing zope.viewlet
%py3_requires z3c.i18n z3c.layer z3c.macro z3c.macroviewlet
%py3_requires z3c.pagelet z3c.template z3c.viewlet z3c.zrtresource
%py3_requires z3c.menu.simple
Requires: python3-module-z3c.skin = %EVR

%description -n python3-module-%oname
This package provides a base skin for people wanting to develop
pagelet-based applications.

%package -n python3-module-%oname-tests
Summary: Tests for a base skin for pagelet-based UIs
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage z3c.etestbrowser zope.app.testing

%description -n python3-module-%oname-tests
This package provides a base skin for people wanting to develop
pagelet-based applications.

This package contains tests for a base skin for pagelet-based UIs.

%package tests
Summary: Tests for a base skin for pagelet-based UIs
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.etestbrowser zope.app.testing

%description tests
This package provides a base skin for people wanting to develop
pagelet-based applications.

This package contains tests for a base skin for pagelet-based UIs.

%package -n python-module-z3c.skin
Summary: Core package of z3c.skin
Group: Development/Python

%description -n python-module-z3c.skin
This package contains core package of z3c.skin.

%package -n python3-module-z3c.skin
Summary: Core package of z3c.skin
Group: Development/Python3

%description -n python3-module-z3c.skin
This package contains core package of z3c.skin.

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
touch %buildroot%python_sitelibdir/z3c/skin/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/skin/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/z3c/skin/__init__.py*

%files tests
%python_sitelibdir/*/*/*/test*

%files -n python-module-z3c.skin
%python_sitelibdir/z3c/skin/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/z3c/skin/__init__.py
%exclude %python3_sitelibdir/z3c/skin/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-z3c.skin
%python3_sitelibdir/z3c/skin/__init__.py
%python3_sitelibdir/z3c/skin/__pycache__/__init__.*
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt4
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Added python-module-z3c.skin

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

