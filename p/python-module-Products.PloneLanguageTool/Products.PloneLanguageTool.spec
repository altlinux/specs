%define oname Products.PloneLanguageTool

Name: python-module-%oname
Version: 3.2.8
Release: alt2.dev0.git20141009
Summary: Allows to set available languages in a Plone site e.t.c.
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneLanguageTool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.PloneLanguageTool.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.i18n Products.CMFCore ZODB3 zope.component
%py_requires zope.interface

%description
PloneLanguageTool allows you to set the available languages in your
Plone site, select various fallback mechanisms, and control the use of
flags for language selection and translations.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
PloneLanguageTool allows you to set the available languages in your
Plone site, select various fallback mechanisms, and control the use of
flags for language selection and translations.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.8-alt2.dev0.git20141009
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.8-alt1.dev0.git20141009
- Initial build for Sisyphus

