%define oname plone.app.jquerytools
Name: python-module-%oname
Version: 1.6.2
Release: alt1.dev0.git20140923
Summary: jQuery Tools integration for Plone plus overlay and AJAX form helpers
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.jquerytools/1.6.1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.jquerytools.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-selenium
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app zope.component Products.CMFCore
%py_requires Products.GenericSetup

%description
plone.app.jquerytools adds jquery.tools and some related overlay and
form-handling JavaScript libraries to Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.jquerytools adds jquery.tools and some related overlay and
form-handling JavaScript libraries to Plone.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.dev0.git20140923
- Initial build for Sisyphus

