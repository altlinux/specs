%define mname collective.z3cform
%define oname %mname.wizard
Name: python-module-%oname
Version: 1.4.9
Release: alt1.dev.git20140207
Summary: This is a library for creating multi-page wizards using z3c.form
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.wizard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.wizard.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.z3cform-tests
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.z3cform Products.statusmessages plone.autoform
%py_requires zope.component zope.i18nmessageid zope.security zope.i18n
%py_requires zope.interface zope.schema zope.app.pagetemplate
%py_requires zope.browserpage zope.publisher

%description
This library implements a simple z3c.form-based wizard. The wizard is
composed of multiple steps. Each step is a form. Data is stored in a
session until the user clicks the Finish button on the last step.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.z3cform.tests z3c.form.testing zope.annotation
%py_requires zope.configuration zope.testing

%description tests
This library implements a simple z3c.form-based wizard. The wizard is
composed of multiple steps. Each step is a form. Data is stored in a
session until the user clicks the Finish button on the last step.

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
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*
%exclude %python_sitelibdir/collective/z3cform/*/tests.*

%files tests
%python_sitelibdir/collective/z3cform/*/tests.*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.9-alt1.dev.git20140207
- Initial build for Sisyphus

