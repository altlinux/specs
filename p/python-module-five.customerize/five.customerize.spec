%define oname five.customerize
Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20130313
Summary: TTW customization of template-based Zope views
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/five.customerize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/five.customerize.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-transaction
BuildPreReq: python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.testing zope.traversing zope.viewlet
%py_requires zope.pagetemplate zope.publisher zope.schema zope.site
%py_requires zope.dottedname zope.interface zope.lifecycleevent
%py_requires five plone.portlets zope.component zope.componentvocabulary

%description
five.customerize provides the ability to locally customize Page
Template-based browser views, much like it is possible to customize
file-system based view templates in the CMF's portal_skin tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
five.customerize provides the ability to locally customize Page
Template-based browser views, much like it is possible to customize
file-system based view templates in the CMF's portal_skin tools.

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
%doc *.rst
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/test*

%files tests
%python_sitelibdir/five/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20130313
- Initial build for Sisyphus

