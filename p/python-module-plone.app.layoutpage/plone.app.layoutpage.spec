%define mname plone.app
%define oname %mname.layoutpage
Name: python-module-%oname
Version: 1.2
Release: alt1.git20121217
Summary: A basic page content type for Plone using Deco layout
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.layoutpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.layoutpage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.blocks
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.behavior

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.interface zope.component zope.lifecycleevent
%py_requires z3c.form plone.dexterity plone.app.blocks
%py_requires plone.app.dexterity

%description
plone.app.layoutpage provides a very basic page content type for Plone
that is editable via Deco.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing plone.app.testing plone.behavior

%description tests
plone.app.layoutpage provides a very basic page content type for Plone
that is editable via Deco.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20121217
- Initial build for Sisyphus

