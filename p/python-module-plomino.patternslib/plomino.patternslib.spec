%define mname plomino
%define oname %mname.patternslib
Name: python-module-%oname
Version: 0.5.5
Release: alt1.git20121015
Summary: Fields and other form elements built using the Patterns javascript library
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plomino.patternslib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plomino/plomino.patternslib.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlomino
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires %mname Products.CMFPlomino zope.schema zope.pagetemplate
%py_requires zope.component zope.interface zope.formlib

%description
plomino.patternslib is a Plomino plugin that provides fields and other
form elements built using the Patternslib javascript library. In its
initial implementation, the Chosen select boxes from HarvestHQ are made
available.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.CMFCore

%description tests
plomino.patternslib is a Plomino plugin that provides fields and other
form elements built using the Patternslib javascript library. In its
initial implementation, the Chosen select boxes from HarvestHQ are made
available.

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
%doc *.rst docs/* src/examples
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.git20121015
- Initial build for Sisyphus

