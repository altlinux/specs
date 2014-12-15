%define oname Products.RedirectionTool
Name: python-module-%oname
Version: 1.3.2
Release: alt1.git20140308
Summary: The Redirection Tool allows the management of the aliases stored in plone.app.redirector
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.RedirectionTool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.RedirectionTool.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.redirector
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFFormController

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.CMFCore Products.statusmessages
%py_requires plone.memoize plone.app.controlpanel plone.app.redirector
%py_requires zope.i18nmessageid zope.formlib zope.schema zope.component
%py_requires zope.interface zope.deprecation

%description
The Redirection Tool allows the management of the aliases stored in
plone.app.redirector, both globally through a control panel and per-item
in an editing tab.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.CMFFormController

%description tests
The Redirection Tool allows the management of the aliases stored in
plone.app.redirector, both globally through a control panel and per-item
in an editing tab.

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

pushd Products/RedirectionTool
cp -fR *.zcml *.gif locales profiles \
	%buildroot%python_sitelibdir/Products/RedirectionTool/
install -p -m644 browser/*.pt \
	%buildroot%python_sitelibdir/Products/RedirectionTool/browser/
popd

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
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20140308
- Initial build for Sisyphus

