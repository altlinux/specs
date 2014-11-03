%define mname plone.app
%define oname %mname.stagingbehavior
Name: python-module-%oname
Version: 0.1.1
Release: alt1.dev0.git20141027
Summary: Provides a behavior for using plone.app.iterate with dexterity content types
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.stagingbehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.stagingbehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.versioningbehavior
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-Products.CMFPlacefulWorkflow

%py_provides %oname
%py_requires %mname Products.CMFPlone plone.app.dexterity plone.locking
%py_requires plone.app.iterate plone.app.relationfield z3c.relationfield

%description
The IStagingSupport behavior is used for enabling the plone.app.iterate
functionality for Dexterity content. It allows you to perform the
checkout and checkin operations to work on a copy of your original
content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.versioningbehavior
%py_requires plone.app.referenceablebehavior
%py_requires Products.CMFPlacefulWorkflow

%description tests
The IStagingSupport behavior is used for enabling the plone.app.iterate
functionality for Dexterity content. It allows you to perform the
checkout and checkin operations to work on a copy of your original
content.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.dev0.git20141027
- Initial build for Sisyphus

