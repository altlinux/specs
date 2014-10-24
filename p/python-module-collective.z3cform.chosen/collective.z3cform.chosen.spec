%define mname collective.z3cform
%define oname %mname.chosen
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20130604
Summary: chosen widget for z3cform (both chosen & ajax version)
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.chosen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kiorky/collective.z3cform.chosen.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-Plone
BuildPreReq: python-module-demjson
BuildPreReq: python-module-ordereddict
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-collective.js.chosen
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-openid
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires z3c.autoinclude Plone plone.app.upgrade
%py_requires collective.js.chosen z3c.formwidget.query

%description
This package contains 4 widgets for z3cform using the chosen and
ajaxchosen libraries.

* A single valued widget for chosen
* A multi valued widget for chosen
* A single valued widget for ajaxchosen
* A multi valued widget for ajaxchosen

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.component.testing plone.app.testing
%py_requires zope.security.testing

%description tests
This package contains 4 widgets for z3cform using the chosen and
ajaxchosen libraries.

* A single valued widget for chosen
* A multi valued widget for chosen
* A single valued widget for ajaxchosen
* A multi valued widget for ajaxchosen

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

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

install -p -m644 src/collective/z3cform/__init__.py \
	%buildroot%python_sitelibdir/collective/z3cform/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/z3cform/*/test*
%exclude %python_sitelibdir/collective/z3cform/__init__.py*

%files tests
%python_sitelibdir/collective/z3cform/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/z3cform
%python_sitelibdir/collective/z3cform/__init__.py*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20130604
- Initial build for Sisyphus

