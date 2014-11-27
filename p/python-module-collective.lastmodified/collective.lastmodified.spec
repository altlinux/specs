%define mname collective
%define oname %mname.lastmodified
Name: python-module-%oname
Version: 1.0.1
Release: alt1.dev0.git20141127
Summary: Adds a viewlet that displays the last modification date
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.lastmodified
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.lastmodified.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component

%py_provides %oname
%py_requires %mname Products.CMFCore Products.ATContentTypes
%py_requires Products.Archetypes plone.app.layout zope.interface
%py_requires zope.i18nmessageid zope.component

%description
This add-on provides a viewlet that shows the last modification date of
a document. By default, the viewlet is not activated. It can be switched
on per document in the settings tab of the edit screen.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing

%description tests
This add-on provides a viewlet that shows the last modification date of
a document. By default, the viewlet is not activated. It can be switched
on per document in the settings tab of the edit screen.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20141127
- Initial build for Sisyphus

