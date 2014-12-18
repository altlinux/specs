%define mname eea
%define oname %mname.tags
Name: python-module-%oname
Version: 5.6
Release: alt1
Summary: EEA Tags
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.tags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.jquery plone.browserlayer Products.Archetypes
%py_requires zope.app.pagetemplate zope.browserpage zope.interface
%py_requires zope.publisher

%description
EEA Tags is a Google+/Facebook like replacement for the Plone keywords
widget.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.CMFCore zope.configuration

%description tests
EEA Tags is a Google+/Facebook like replacement for the Plone keywords
widget.

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
%doc *.md *.rst *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6-alt1
- Initial build for Sisyphus

