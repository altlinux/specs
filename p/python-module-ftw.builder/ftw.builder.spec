%define mname ftw
%define oname %mname.builder
Name: python-module-%oname
Version: 1.6.1
Release: alt1.dev0.git20141231
Summary: Builder pattern for creating Plone objects in tests
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.builder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.builder.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-lxml python-module-path
BuildPreReq: python-module-unittest2 python-module-openid
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.lifecycleevent

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires Products.CMFPlone zope.component zope.container z3c.form
%py_requires Products.CMFCore plone.app.testing plone.i18n zope.schema
%py_requires plone.namedfile plone.dexterity plone.app.dexterity
%py_requires zope.container zope.component zope.interface

%description
Create Plone objects in tests with the Builder Pattern.

The builder pattern simplifies constructing objects. In tests we often
need to create Plone objects, sometimes a single object, sometimes a
whole graph of objects. Using the builder pattern allows us to do this
in a DRY way, so that we do not repeat this over and over.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.configuration plone.api plone.testing plone.rfc822
%py_requires plone.autoform zope.lifecycleevent

%description tests
Create Plone objects in tests with the Builder Pattern.

The builder pattern simplifies constructing objects. In tests we often
need to create Plone objects, sometimes a single object, sometimes a
whole graph of objects. Using the builder pattern allows us to do this
in a DRY way, so that we do not repeat this over and over.

This package contains tests for %oname

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev0.git20141231
- Version 1.6.1.dev0

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.dev0.git20141206
- Version 1.5.3.dev0

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev0.git20141127
- Initial build for Sisyphus

