%define oname plone.contentrules
Name: python-module-%oname
Version: 2.0.5
Release: alt1.dev0.git20140823
Summary: Plone ContentRules Engine
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.contentrules/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.contentrules.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires plone ZODB3 zope.annotation zope.component zope.container
%py_requires zope.componentvocabulary zope.configuration zope.interface
%py_requires zope.i18nmessageid zope.lifecycleevent zope.schema

%description
plone.contentrules provides a "pure Zope" implementation of a rules
engine which allows arbitrary conditions and actions to be combined into
rules, and rules to be executed dependent on events.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
plone.contentrules provides a "pure Zope" implementation of a rules
engine which allows arbitrary conditions and actions to be combined into
rules, and rules to be executed dependent on events.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*
%exclude %python_sitelibdir/plone/*/*/tests

%files tests
%python_sitelibdir/plone/*/tests.*
%python_sitelibdir/plone/*/*/tests

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.dev0.git20140823
- Initial build for Sisyphus

