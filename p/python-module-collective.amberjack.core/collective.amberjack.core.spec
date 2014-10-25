%define mname collective.amberjack
%define oname %mname.core
Name: python-module-%oname
Version: 1.1.1
Release: alt1.git20131218
Summary: The Amberjack layer
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.amberjack.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.amberjack.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-i18ndude
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.layout Products.GenericSetup
%py_requires collective.js.jqueryui plone.registry

%description
This package provides core functionality for collective.amberjack
package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
This package provides core functionality for collective.amberjack
package.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/amberjack/__init__.py \
	%buildroot%python_sitelibdir/collective/amberjack/

%check
python setup.py test

%files
%doc *.txt docs/*
%_bindir/*
%python_sitelibdir/collective/amberjack/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/amberjack/*/tests
%exclude %python_sitelibdir/collective/amberjack/__init__.py*

%files tests
%python_sitelibdir/collective/amberjack/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/amberjack
%python_sitelibdir/collective/amberjack/__init__.py*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20131218
- Initial build for Sisyphus

