%define oname plone.app.versioningbehavior

%def_disable check

Name: python-module-%oname
Version: 1.2.1
Release: alt1.dev0.git20140915
Summary: Provides a behavior for using CMFEditions with dexterity content types
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.versioningbehavior
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.versioningbehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-rwproperty
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFDiffTool
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-plone.app.dexterity
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
%py_requires plone.app plone.autoform plone.dexterity plone.namedfile
%py_requires Products.CMFEditions zope.app.container
#py_requires plone.app.dexterity

%description
The ``IVersionable`` behavior is used for enabling the CMFEditions
functionality for dexterity contents. It adds a changeNote-field to the
edit- and add-forms and creates a new version when the content is
edited, if enabled for the content type.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Products.CMFEditions-tests
%py_requires plone.app.testing Products.CMFDiffTool plone.app.testing
#py_requires Products.CMFPlone

%description tests
The ``IVersionable`` behavior is used for enabling the CMFEditions
functionality for dexterity contents. It adds a changeNote-field to the
edit- and add-forms and creates a new version when the content is
edited, if enabled for the content type.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.dev0.git20140915
- Initial build for Sisyphus

