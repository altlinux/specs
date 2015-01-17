%define mname plone.app
%define oname %mname.themingplugins
Name: python-module-%oname
Version: 1.0
Release: alt1.b1.git20131124
Summary: Plugins providing advanced plone.app.theming integration
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.themingplugins/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.themingplugins.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-z3c.jbot
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-plone.registry

%py_provides %oname
%py_requires %mname plone.app.theming zope.interface zope.dottedname
%py_requires plone.resource zope.configuration z3c.jbot Products.CMFCore
%py_requires zope.browsermenu

%description
plone.app.theming supports plugins that allow theme authors to bundle
more advanced functionality with their themes. This package contains two
such plugins:

* The ability to override specific Zope Page Templates when a theme is
  enabled
* The ability to register views providing custom markup using Zope Page
  Templates when a theme is enabled

Both of these only work for themes distributed on the filesystem (either
in a Python package or in the global themes resource directory), i.e.
not for themes imported through-the-web in ZIP archives. That said, the
features provided by these plugins are more likely to be useful in
building "customer" sites (where filesystem development is likely to be
the norma) than in distributing generic themes (where the
through-the-web ZIP import is more attractive).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.registry zope.component

%description tests
plone.app.theming supports plugins that allow theme authors to bundle
more advanced functionality with their themes. This package contains two
such plugins:

* The ability to override specific Zope Page Templates when a theme is
  enabled
* The ability to register views providing custom markup using Zope Page
  Templates when a theme is enabled

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

pushd plone/app/themingplugins
install -p -m644 *.zcml \
	%buildroot%python_sitelibdir/plone/app/themingplugins/
cp -fR tests/*.zcml tests/resources \
	%buildroot%python_sitelibdir/plone/app/themingplugins/tests/
for i in browserlayer overrides views; do
	install -p -m644 $i/*.zcml \
		%buildroot%python_sitelibdir/plone/app/themingplugins/$i/
done
popd

%check
python setup.py test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20131124
- Initial build for Sisyphus

