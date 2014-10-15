%define oname plone.app.customerize
Name: python-module-%oname
Version: 1.3.2
Release: alt1.dev0.git20140730
Summary: Integrate five.customerize into Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.customerize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.customerize.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.customerize
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app five.customerize plone.browserlayer
%py_requires plone.portlets zope.component zope.interface
%py_requires zope.publisher zope.viewlet Products.CMFCore

%description
This package integrates five.customerize into Plone, which enables site
administrators to customize templates used for Five/Zope-style views,
viewlets and portlets through the web via the ZMI in a way similar to
overriding filesystem-based skin elements via the portal skin
"customize" procedure.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.layout plone.app.testing zope.testing

%description tests
This package integrates five.customerize into Plone, which enables site
administrators to customize templates used for Five/Zope-style views,
viewlets and portlets through the web via the ZMI in a way similar to
overriding filesystem-based skin elements via the portal skin
"customize" procedure.

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
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.dev0.git20140730
- Initial build for Sisyphus

