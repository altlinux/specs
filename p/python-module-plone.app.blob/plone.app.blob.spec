%define oname plone.app.blob

Name: python-module-%oname
Version: 1.5.11
Release: alt2.dev0.git20141001
Summary: ZODB blob support for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.blob/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.blob.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.proxy python-module-plone.app
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.scale
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app ZODB3 zope.proxy archetypes.schemaextender
%py_requires plone.app.imaging plone.scale Products.CMFPlone
%py_requires Products.Archetypes

%description
This package aims to be an add-on for Plone (>= 3.x) integrating ZODB
(>=3.8) blob support, which allows large binary data to be managed by
the ZODB, but separately from your usual FileStorage database, i.e.
Data.fs. This has several advantages, most importantly a much smaller
Data.fs and better performance both cpu- as well as memory-wise.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.monkeypatcher Products.contentmigration
%py_requires plone.app.testing plone.testing

%description tests
This package aims to be an add-on for Plone (>= 3.x) integrating ZODB
(>=3.8) blob support, which allows large binary data to be managed by
the ZODB, but separately from your usual FileStorage database, i.e.
Data.fs. This has several advantages, most importantly a much smaller
Data.fs and better performance both cpu- as well as memory-wise.

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
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.11-alt2.dev0.git20141001
- Added necessary requirements
- Enabled testing

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.11-alt1.dev0.git20141001
- Initial build for Sisyphus

