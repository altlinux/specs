%define mname collective
%define oname %mname.mtrsetup
Name: python-module-%oname
Version: 1.5.3
Release: alt2.dev0.git20141107
Summary: Extension for GenericSetup, adding support for import / export of mimetypes_registry
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.mtrsetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.mtrsetup.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.GenericSetup-tests
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.GenericSetup Products.MimetypesRegistry
%py_requires z3c.autoinclude Products.CMFCore

%description
collective.mtrsetup provides a GenericSetup extension for importing and
exporting mimetypes to / from the mimetypes registry.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Plone zope.testing Products.PloneTestCase
%py_requires Products.GenericSetup.tests

%description tests
collective.mtrsetup provides a GenericSetup extension for importing and
exporting mimetypes to / from the mimetypes registry.

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
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/mtrsetup/profiles/example

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/mtrsetup/profiles/example

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt2.dev0.git20141107
- Moved example into tests subpackage

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.dev0.git20141107
- Initial build for Sisyphus

