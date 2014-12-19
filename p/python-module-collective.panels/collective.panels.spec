%define mname collective
%define oname %mname.panels
Name: python-module-%oname
Version: 1.9
Release: alt1.dev0.git20141215
Summary: Add-on for Plone that adds portlet panels
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.panels/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.panels.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-z3c.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.portlets Products.CMFCore plone.registry
%py_requires Products.statusmessages plone.portlets plone.z3cform
%py_requires plone.app.registry plone.protect plone.memoize zope.schema
%py_requires plone.app.viewletmanager plone.app.layout zope.component
%py_requires zope.i18nmessageid zope.traversing zope.publisher z3c.form
%py_requires zope.interface zope.annotation zope.configuration
%py_requires zope.container zope.pagetemplate zope.viewlet zope.security

%description
Panels are sets of portlets appearing in various layout configurations
which you can insert into a selection of Plone's existing locations
(above and below page contents, portal top and footer).

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.dev0.git20141215
- Initial build for Sisyphus

