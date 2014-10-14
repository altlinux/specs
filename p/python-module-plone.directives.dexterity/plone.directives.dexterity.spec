%define mname plone.directives
%define oname %mname.dexterity
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev.git20140514
Summary: Grok-like directives for creating Dexterity content
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.directives.dexterity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.directives.dexterity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-plone.mocktestcase

%py_provides %oname
%py_requires %mname five.grok plone.dexterity plone.directives.form
%py_requires zope.deferredimport

%description
This package provides optional, Grok-like directives for configuring
Dexterity content. It depends on five.grok, which in turn depends on the
various re-usable grokcore.* packages, but not Grok itself.

See also plone.directives.form, which provides directives for
configuring schema interfaces with form hints.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.mocktestcase

%description tests
This package provides optional, Grok-like directives for configuring
Dexterity content. It depends on five.grok, which in turn depends on the
various re-usable grokcore.* packages, but not Grok itself.

See also plone.directives.form, which provides directives for
configuring schema interfaces with form hints.

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
%python_sitelibdir/plone/directives/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/directives/*/tests

%files tests
%python_sitelibdir/plone/directives/*/tests

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev.git20140514
- Initial build for Sisyphus

