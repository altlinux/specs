%define mname archetypes
%define oname %mname.referencebrowserwidget
Name: python-module-%oname
Version: 2.5.3
Release: alt1.dev0.git20140911
Summary: A referencebrowser implementation for Archetypes
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/archetypes.referencebrowserwidget
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/archetypes.referencebrowserwidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.Archetypes-tests

%py_provides %oname
%py_requires zope.interface zope.component zope.formlib plone.app.form
%py_requires plone.app.jquerytools %mname

%description
This is an implementation of referencebrowser widget. It provides a
widget used for Archetypes reference-fields. The widget can be used on
its own or as a dropin replacement of the ATReferenceBrowserWidget in
Plone 3 and is included in Plone >= 4. Unlike the
ATReferenceBrowserWidget, archetypes.refencebrowserwidget uses an
overlay instead of a popup to display the referencebrowser.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.Archetypes.tests

%description tests
This is an implementation of referencebrowser widget. It provides a
widget used for Archetypes reference-fields. The widget can be used on
its own or as a dropin replacement of the ATReferenceBrowserWidget in
Plone 3 and is included in Plone >= 4. Unlike the
ATReferenceBrowserWidget, archetypes.refencebrowserwidget uses an
overlay instead of a popup to display the referencebrowser.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.dev0.git20140911
- Initial build for Sisyphus

