%define oname plone.z3cform
Name: python-module-%oname
Version: 0.8.1
Release: alt2.git20150122
Summary: plone.z3cform is a library that allows use of z3c.form with Zope 2 and the CMF
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.z3cform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/plone.z3cform.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-docutils
BuildPreReq: python-module-plone.batching
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone plone.batching z3c.form zope.i18n zope.browserpage
%py_requires zope.component

%description
plone.z3cform is a library that enables the use of z3c.form in Zope 2.
It depends only on Zope 2 and z3c.form.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing

%description tests
plone.z3cform is a library that enables the use of z3c.form in Zope 2.
It depends only on Zope 2 and z3c.form.

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
%doc *.rst
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2.git20150122
- Version 0.8.1

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.dev0.git20130313
- Initial build for Sisyphus

