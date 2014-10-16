%define oname plone.app.linkintegrity

Name: python-module-%oname
Version: 2.1.0
Release: alt2.dev0.git20141009
Summary: Manage link integrity in Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.linkintegrity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.linkintegrity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
%py_requires plone.app plone.app.referenceablebehavior
%py_requires Products.Archetypes
%py_requires Products.CMFPlone

%description
This package tries to integrate PLIP 125, link integrity checking, into
Plone. It is making use of the zope3 event system in order to modify
Plone itself as little as possible.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.contenttypes
%py_requires plone.app.dexterity

%description tests
This package tries to integrate PLIP 125, link integrity checking, into
Plone. It is making use of the zope3 event system in order to modify
Plone itself as little as possible.

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
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.dev0.git20141009
- Initial build for Sisyphus

