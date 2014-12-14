%define oname Products.UserAndGroupSelectionWidget
Name: python-module-%oname
Version: 3.0
Release: alt1.dev.git20130923
Summary: Archetypes Widget for User and Group Selection, works with many users
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.UserAndGroupSelectionWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.UserAndGroupSelectionWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-bda.cache python-module-lxml
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.interface zope.component zope.schema Products.CMFCore
%py_requires Products.CMFPlone Products.PlonePAS bda.cache
%py_requires plone.dexterity

%description
UserAndGroupSelectionWidget is a widget to search and select users
and/or groups from a huge base of users. It uses a modernized, fast
code-base and is tested with hundreds of groups and thousands of users.

It is configurable to select only groups, only users, both or only user
of a distinct group.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.app.testing plone.app.testing

%description tests
UserAndGroupSelectionWidget is a widget to search and select users
and/or groups from a huge base of users. It uses a modernized, fast
code-base and is tested with hundreds of groups and thousands of users.

It is configurable to select only groups, only users, both or only user
of a distinct group.

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
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*

%changelog
* Sun Dec 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev.git20130923
- Initial build for Sisyphus

