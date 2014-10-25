%define oname Products.CMFQuickInstallerTool
Name: python-module-%oname
Version: 3.0.8
Release: alt1.dev0.git20141024
Summary: Facility for comfortable activation/deactivation of CMF compliant products
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFQuickInstallerTool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFQuickInstallerTool.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.annotation zope.component zope.i18nmessageid
%py_requires zope.interface Products.CMFCore Products.GenericSetup

%description
CMFQuickInstallerTool is a facility for comfortable
activation/deactivation of CMF compliant products inside a CMF site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.app.testing

%description tests
CMFQuickInstallerTool is a facility for comfortable
activation/deactivation of CMF compliant products inside a CMF site.

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
%exclude %python_sitelibdir/Products/*/*/test

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/test

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.dev0.git20141024
- Version 3.0.8.dev0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.git20140921
- Initial build for Sisyphus

