%define mname simplelayout
%define oname %mname.ui.base

Name: python-module-%oname
Version: 3.0.2
Release: alt2.dev0.git20141107
Summary: Simplelayout user interface component
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/simplelayout.ui.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/simplelayout.ui.base.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-z3c.json
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname.ui = %EVR
Requires: python-module-Zope2
%py_requires ftw.colorbox z3c.json simplelayout.base Products.CMFPlone
%py_requires Products.CMFCore plone.registry plone.app.upgrade zope.i18n
%py_requires zope.component

%description
Simplelayout ui base package - for plone.

Following features for simplelayout are provided by this package:

* using jquery/ajax
* implement always the newest jquery framework and jquery.ui
* implement the grey jquery theme
* delete blocks by a modal window
* reload blocks
* change block layout

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing plone.app.testing zope.configuration

%description tests
Simplelayout ui base package - for plone.

Following features for simplelayout are provided by this package:

* using jquery/ajax
* implement always the newest jquery framework and jquery.ui
* implement the grey jquery theme
* delete blocks by a modal window
* reload blocks
* change block layout

This package contains tests for %oname.

%package -n python-module-%mname.ui
Summary: Core files of %mname.ui
Group: Development/Python
%py_provides %mname.ui
%py_requires %mname

%description -n python-module-%mname.ui
Core files of %mname.ui.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/ui/__init__.py \
	%buildroot%python_sitelibdir/%mname/ui/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/ui/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/ui/*/test*
%exclude %python_sitelibdir/%mname/ui/__init__.py*

%files tests
%python_sitelibdir/%mname/ui/*/test*

%files -n python-module-%mname.ui
%dir %python_sitelibdir/%mname/ui
%python_sitelibdir/%mname/ui/__init__.py*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt2.dev0.git20141107
- Enabled testing

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.dev0.git20141107
- Initial build for Sisyphus

