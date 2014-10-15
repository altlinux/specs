%define oname plone.fieldsets
Name: python-module-%oname
Version: 2.0.3
Release: alt1.dev0.git20140823
Summary: An extension to zope.formlib, which allows to group fields into different fieldsets
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.fieldsets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.fieldsets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires plone five.formlib zope.component zope.formlib
%py_requires zope.interface zope.schema

%description
An extension to zope.formlib, which allows to group fields into
different fieldsets.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.publisher zope.testing

%description tests
An extension to zope.formlib, which allows to group fields into
different fieldsets.

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

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.dev0.git20140823
- Initial build for Sisyphus

