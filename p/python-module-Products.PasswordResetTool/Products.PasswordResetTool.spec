%define oname Products.PasswordResetTool

%def_disable check

Name: python-module-%oname
Version: 2.1.1
Release: alt1.dev0.git20141009
Summary: Password reset UI and infrastructure for the Plone CMS
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PasswordResetTool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.PasswordResetTool.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.memoize zope.component zope.i18nmessageid zope.i18n
%py_requires zope.interface Products.CMFCore
#py_requires Products.CMFPlone

%description
The Password Reset Tool hooks into the standard mechanisms for password
mailing provided by the CMF in the Registration Tool and certain skins
and replaces this with a facility for resetting passwords with email
authentication.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
The Password Reset Tool hooks into the standard mechanisms for password
mailing provided by the CMF in the Registration Tool and certain skins
and replaces this with a facility for resetting passwords with email
authentication.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.dev0.git20141009
- Initial build for Sisyphus

