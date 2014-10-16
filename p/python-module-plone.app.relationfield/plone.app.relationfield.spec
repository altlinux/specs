%define oname plone.app.relationfield

Name: python-module-%oname
Version: 1.2.3
Release: alt2.dev0.git20140910
Summary: Plone support for z3c.relationfield
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.relationfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.relationfield.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-plone.app.intid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.schemaeditor
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.dexterity

%py_provides %oname
%py_requires plone.app zope.interface zope.component zope.schema
%py_requires zope.intid five.intid plone.app.intid z3c.form
%py_requires z3c.relationfield z3c.formwidget.query plone.autoform
%py_requires plone.supermodel plone.app.vocabularies plone.schemaeditor
%py_requires Products.CMFCore plone.rfc822

%description
Plone support for z3c.relationfield. If this package is installed, you
should be able to use z3c.relationfield as per its documentation for
Dexterity and Archetypes content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
%py_requires plone.app.dexterity

%description tests
Plone support for z3c.relationfield. If this package is installed, you
should be able to use z3c.relationfield as per its documentation for
Dexterity and Archetypes content.

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
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.dev0.git20140910
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20140910
- Initial build for Sisyphus

