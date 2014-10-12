%define oname plone.autoform
Name: python-module-%oname
Version: 1.6.1
Release: alt1.dev0.git20141002
Summary: Tools to construct z3c.form forms
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.autoform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.autoform.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema python-module-docutils
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires plone zope.interface zope.schema zope.security
%py_requires zope.dottedname plone.supermodel plone.z3cform
%py_requires z3c.form

%description
plone.autoform builds custom z3c.form forms based on a model (schema) of
what fields to include and what widgets and options should be used for
each field. This model is defined as a zope.schema-based schema, but
additional hints can be supplied to control aspects of form display not
normally specified in a Zope schema.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
plone.autoform builds custom z3c.form forms based on a model (schema) of
what fields to include and what widgets and options should be used for
each field. This model is defined as a zope.schema-based schema, but
additional hints can be supplied to control aspects of form display not
normally specified in a Zope schema.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev0.git20141002
- Initial build for Sisyphus

