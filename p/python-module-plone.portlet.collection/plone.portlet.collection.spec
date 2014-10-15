%define mname plone.portlet
%define oname %mname.collection

Name: python-module-%oname
Version: 3.0.1
Release: alt2.dev0.git20140826
Summary: Portlet displaying results from a collection
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.portlet.collection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.portlet.collection.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.memoize plone.portlets plone.app.portlets
%py_requires plone.app.vocabularies plone.app.form

%description
A portlet that fetches results from a collection.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.contenttypes

%description tests
A portlet that fetches results from a collection.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires plone

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

install -p -m644 plone/portlet/__init__.py \
	%buildroot%python_sitelibdir/plone/portlet/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/portlet/*/test*
%exclude %python_sitelibdir/plone/portlet/__init__.py*

%files tests
%python_sitelibdir/plone/portlet/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/plone/portlet
%python_sitelibdir/plone/portlet/__init__.py*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2.dev0.git20140826
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20140826
- Initial build for Sisyphus

