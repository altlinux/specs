%define oname Products.CMFDiffTool
Name: python-module-%oname
Version: 3.0
Release: alt1.dev0.git20140930
Summary: Diff tool for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFDiffTool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFDiffTool.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.namedfile
#BuildPreReq: python-module-plone.app.versioningbehavior
#BuildPreReq: python-module-plone.app.dexterity
#BuildPreReq: python-module-plone.app.contenttypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.GenericSetup zope.interface
#py_requires plone.app.versioningbehavior

%description
Diff tool for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component plone.app.testing plone.namedfile
#py_requires plone.app.dexterity plone.app.contenttypes

%description tests
Diff tool for Plone.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev0.git20140930
- Initial build for Sisyphus

