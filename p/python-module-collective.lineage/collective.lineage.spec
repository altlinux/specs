%define mname collective
%define oname %mname.lineage
Name: python-module-%oname
Version: 2.1
Release: alt1.dev0.git20141029
Summary: The microsite creation product for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.lineage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.lineage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-plone.app.imaging
BuildPreReq: python-module-interlude python-module-plone.app.testing
BuildPreReq: python-module-zope.i18nmessageid python-module-openid
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-p4a.subtyper
BuildPreReq: python-module-p4a.z2utils

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone plone.app.imaging zope.component zope.event
%py_requires zope.i18nmessageid zope.interface plone.app.layout
%py_requires plone.folder Products.CMFCore p4a.subtyper p4a.z2utils

%description
Lineage is a Plone product that allows subfolders of a Plone site to
appear as autonomous Plone sites to the everyday user. This hub and
spoke structure allows site administrators to easily manage multiple,
seemingly independent, sub-entity websites in one Plone. Furthermore,
the "parent" site can access and view the content in all the "child"
sites while the child sites only view their own content. The parent site
can also syndicate chosen content to the selected child sites. Lineage
is less complex and easier to manage than a cluster of nested Plone
sites but gives users all the same benefits.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration plone.browserlayer
%py_requires plone.testing

%description tests
Lineage is a Plone product that allows subfolders of a Plone site to
appear as autonomous Plone sites to the everyday user. This hub and
spoke structure allows site administrators to easily manage multiple,
seemingly independent, sub-entity websites in one Plone. Furthermore,
the "parent" site can access and view the content in all the "child"
sites while the child sites only view their own content. The parent site
can also syndicate chosen content to the selected child sites. Lineage
is less complex and easier to manage than a cluster of nested Plone
sites but gives users all the same benefits.

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
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev0.git20141029
- Initial build for Sisyphus

