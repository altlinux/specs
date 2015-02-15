%define mname collective
%define oname %mname.js.datatables
Name: python-module-%oname
Version: 3.1.10.5
Release: alt1.dev0.git20150129
Summary: Plone Integration of jquery.dataTables plugin
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.datatables/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.datatables.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-plone.browserlayer

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.js Products.CMFCore zope.i18nmessageid zope.i18n

%description
DataTables is a plug-in for the jQuery Javascript library. It is a
highly flexible tool, based upon the principle of progressive
enhancement, which will add advanced interaction controls to any HTML
table.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.browserlayer zope.interface

%description tests
DataTables is a plug-in for the jQuery Javascript library. It is a
highly flexible tool, based upon the principle of progressive
enhancement, which will add advanced interaction controls to any HTML
table.

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
%python_sitelibdir/%mname/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/js/*/test*
%exclude %python_sitelibdir/%mname/js/*/example
%exclude %python_sitelibdir/%mname/js/*/*/*/*/*/examples

%files tests
%python_sitelibdir/%mname/js/*/test*
%python_sitelibdir/%mname/js/*/example
%python_sitelibdir/%mname/js/*/*/*/*/*/examples

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.10.5-alt1.dev0.git20150129
- Version 3.1.10.5.dev0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.10.4-alt1.dev0.git20141215
- Initial build for Sisyphus

