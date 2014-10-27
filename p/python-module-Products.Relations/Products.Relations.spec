%define oname Products.Relations
Name: python-module-%oname
Version: 0.9
Release: alt2.b2.git20110919
Summary: Define sets of rules for validation, creation and lifetime of Archetypes references
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Relations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.Relations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.CMFCore Products.CMFPlone
%py_requires zope.interface zope.event zope.i18n

%description
Relations allows for the definition of sets of rules for validation,
creation and lifetime of Archetypes references. Contained in each
ruleset are components that make for the actual rules logic.

Rulesets may be created and edited through the web (TTW). Components
implementing custom behaviour are easily added.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing Products.Archetypes.tests
%py_requires Products.CMFCore.testing

%description tests
Relations allows for the definition of sets of rules for validation,
creation and lifetime of Archetypes references. Contained in each
ruleset are components that make for the actual rules logic.

Rulesets may be created and edited through the web (TTW). Components
implementing custom behaviour are easily added.

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

cp -fR Products/Relations/skins \
	%buildroot%python_sitelibdir/Products/Relations/

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
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.b2.git20110919
- Added skins

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.b2.git20110919
- Initial build for Sisyphus

