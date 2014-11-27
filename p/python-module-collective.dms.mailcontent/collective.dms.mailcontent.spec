%define mname collective.dms
%define oname %mname.mailcontent
Name: python-module-%oname
Version: 0.1.8
Release: alt1.dev0.git20141126
Summary: Mail content type for document management system
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dms.mailcontent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dms.mailcontent.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-collective.contact.core
BuildPreReq: python-module-collective.dms.basecontent
BuildPreReq: python-module-plone.formwidget.datetime
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires %mname plone.api plone.app.dexterity plone.directives.form
%py_requires collective.contact.core collective.dms.basecontent
%py_requires plone.formwidget.datetime five.grok

%description
Mail content type for document management system.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ecreall.helpers.testing

%description tests
Mail content type for document management system.

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
%python_sitelibdir/collective/dms/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/dms/*/test*
%exclude %python_sitelibdir/collective/dms/*/*/test*

%files tests
%python_sitelibdir/collective/dms/*/test*
%python_sitelibdir/collective/dms/*/*/test*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.dev0.git20141126
- Version 0.1.8.dev0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.dev0.git20141016
- Initial build for Sisyphus

