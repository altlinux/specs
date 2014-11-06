%define oname Products.AutoUserMakerPASPlugin
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20141106
Summary: Automatically generate members on login in Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AutoUserMakerPASPlugin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.AutoUserMakerPASPlugin.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PlonePAS Products.PluggableAuthService
%py_requires Products.CMFCore

%description
Accept Apache based authentication in Zope and create Plone users.

AutoUserMakerPasPlugin is a PAS plugin developed from apachepas, which
allows Zope to delegate authentication concerns to Apache, and that
automatically creates users as Apache lets them through. Using
AutoUserMakerPasPlugin, you can configure your Plone site so any user
known to your LDAP, Kerberos, Shibboleth, or Cosign (a.k.a. WebAccess)
system--or indeed any other system which has an Apache authentication
module--can transparently log in using his enterprise-wide credentials.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing zope.component.testing
%py_requires zope.security.testing

%description tests
Accept Apache based authentication in Zope and create Plone users.

AutoUserMakerPasPlugin is a PAS plugin developed from apachepas, which
allows Zope to delegate authentication concerns to Apache, and that
automatically creates users as Apache lets them through. Using
AutoUserMakerPasPlugin, you can configure your Plone site so any user
known to your LDAP, Kerberos, Shibboleth, or Cosign (a.k.a. WebAccess)
system--or indeed any other system which has an Apache authentication
module--can transparently log in using his enterprise-wide credentials.

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
%doc *.txt *.rst
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20141106
- Initial build for Sisyphus

