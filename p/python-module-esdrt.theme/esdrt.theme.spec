%define mname esdrt
%define oname %mname.theme
Name: python-module-%oname
Version: 1.16
Release: alt1.dev0.git20141219
Summary: Installable theme: esdrt.theme
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/esdrt.theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/esdrt.theme.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.jbot
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-eea.icons
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname z3c.jbot five.grok eea.icons Products.CMFCore
%py_requires plone.theme plone.app.layout plone.api zope.i18nmessageid

%description
Product containing the theme for the Effort Sharing Decission Review
Tool.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2-tests
%py_requires Products.PloneTestCase

%description tests
Product containing the theme for the Effort Sharing Decission Review
Tool.

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

rm -f ignore.txt

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1.dev0.git20141219
- Initial build for Sisyphus

