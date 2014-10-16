%define oname plone.app.referenceablebehavior

Name: python-module-%oname
Version: 0.7.1
Release: alt2.dev0.git20140826
Summary: Referenceable dexterity type behavior
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.referenceablebehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.referenceablebehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Plone

%py_provides %oname
%py_requires plone.app plone.behavior plone.dexterity plone.indexer
%py_requires plone.uuid
%py_requires Products.Archetypes

%description
The "IReferenceable" behavior is used for enabling UUID (plone.app.uuid)
support for dexterity contents, like in archetypes content types. This
allow for example references between archetypes and dexterity content
types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.dexterity
%py_requires Plone

%description tests
The "IReferenceable" behavior is used for enabling UUID (plone.app.uuid)
support for dexterity contents, like in archetypes content types. This
allow for example references between archetypes and dexterity content
types.

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
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2.dev0.git20140826
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev0.git20140826
- Initial build for Sisyphus

