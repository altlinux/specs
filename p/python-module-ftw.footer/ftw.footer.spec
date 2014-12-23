%define mname ftw
%define oname %mname.footer
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20141223
Summary: Adds portlet columns as footer to Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.footer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.footer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pyquery
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.viewlet

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.statusmessages plone.registry zope.schema
%py_requires plone.portlets plone.app.layout plone.app.portlets
%py_requires zope.i18nmessageid zope.component zope.interface
%py_requires zope.publisher

%description
ftw.footer provides a viewlet, which shows 1 - 4 contextual portlet
columns.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing plone.app.testing zope.configuration
%py_requires zope.viewlet

%description tests
ftw.footer provides a viewlet, which shows 1 - 4 contextual portlet
columns.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20141223
- Initial build for Sisyphus

