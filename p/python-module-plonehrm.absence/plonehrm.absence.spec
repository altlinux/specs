%define mname plonehrm
%define oname %mname.absence

Name: python-module-%oname
Version: 1.6
Release: alt1.dev.svn20100129
Summary: Register employee absence
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.absence/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plonehrm.notifications
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.plonehrm

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone Products.CMFCore zope.i18n
%py_requires Products.ATContentTypes Products.Archetypes zope.component
%py_requires plonehrm.notifications zope.interface zope.annotation
%py_requires zope.event zope.i18nmessageid
%py_requires Products.plonehrm

%description
Register employee absence.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
Register employee absence.

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
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.dev.svn20100129
- Version 1.6dev

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

