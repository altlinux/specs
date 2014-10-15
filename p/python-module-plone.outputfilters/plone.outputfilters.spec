%define oname plone.outputfilters
Name: python-module-%oname
Version: 1.15
Release: alt1.dev0.git20140801
Summary: Transformations applied to HTML in Plone text fields as they are rendered
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.outputfilters/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.outputfilters.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-markdown
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires plone Products.CMFCore Products.GenericSetup
%py_requires Products.MimetypesRegistry Products.PortalTransforms

%description
plone.outputfilters provides a framework for registering filters that
get applied to text as it is rendered.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
plone.outputfilters provides a framework for registering filters that
get applied to text as it is rendered.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1.dev0.git20140801
- Initial build for Sisyphus

