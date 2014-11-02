%define mname collective
%define oname %mname.noticeboard
Name: python-module-%oname
Version: 0.7.2
Release: alt1.dev0.git20141031
Summary: A fancy noticeboard for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.noticeboard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.noticeboard.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-collective.js.backbone
BuildPreReq: python-module-collective.js.underscore
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone collective.js.backbone collective.js.jqueryui
%py_requires collective.js.underscore plone.app.collection z3c.form
%py_requires plone.app.contentlisting plone.app.z3cform plone.z3cform
%py_requires zope.i18n zope.i18nmessageid zope.annotation zope.interface
%py_requires zope.schema zope.component

%description
A fancy noticeboard for Plone inspired by corkboard.me

This Plone-Addon allow suser to transform folders or collections into a
fancy noticeboard where users can add and modify postit-like notes.
Notes display the content of a content-type (by default News Items) and
are editable in overlays. Notes are draggable, resizeable and can change
color.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.testing zope.configuration

%description tests
A fancy noticeboard for Plone inspired by corkboard.me

This Plone-Addon allow suser to transform folders or collections into a
fancy noticeboard where users can add and modify postit-like notes.
Notes display the content of a content-type (by default News Items) and
are editable in overlays. Notes are draggable, resizeable and can change
color.

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
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.dev0.git20141031
- Initial build for Sisyphus

