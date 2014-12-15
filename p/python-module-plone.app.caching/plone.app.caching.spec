%define oname plone.app.caching
Name: python-module-%oname
Version: 1.2.3
Release: alt1.dev0.git20141023
Summary: HTTP caching framework for the Plone CMS
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.caching/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.caching.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-plone.caching
BuildPreReq: python-module-plone.cachepurging
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.zcmlhook
BuildPreReq: python-module-plone.app.contenttypes-tests
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.caching plone.cachepurging zope.interface
%py_requires plone.app.registry zope.browserresource zope.component
%py_requires zope.publisher zope.pagetemplate plone.memoize z3c.form
%py_requires plone.protect plone.registry Products.CMFDynamicViewFTI
%py_requires Products.GenericSetup Products.CMFCore plone.app.z3cform
%py_requires Products.statusmessages z3c.zcmlhook

%description
plone.app.caching provides a Plone UI and default rules for managing
HTTP response caching in Plone. It builds on z3c.caching, plone.caching
and plone.cachepurging.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.contenttypes.testing plone.app.testing

%description tests
plone.app.caching provides a Plone UI and default rules for managing
HTTP response caching in Plone. It builds on z3c.caching, plone.caching
and plone.cachepurging.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
plone.app.caching provides a Plone UI and default rules for managing
HTTP response caching in Plone. It builds on z3c.caching, plone.caching
and plone.cachepurging.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
plone.app.caching provides a Plone UI and default rules for managing
HTTP response caching in Plone. It builds on z3c.caching, plone.caching
and plone.cachepurging.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst
%dir %python_sitelibdir/%oname
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20141023
- Version 1.2.3.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20141009
- Initial build for Sisyphus

