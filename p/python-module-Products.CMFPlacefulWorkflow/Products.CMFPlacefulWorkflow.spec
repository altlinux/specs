%define oname Products.CMFPlacefulWorkflow

%def_disable check

Name: python-module-%oname
Version: 1.6.1
Release: alt1.dev0.git20140416
Summary: Workflow policies for CMF and Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFPlacefulWorkflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFPlacefulWorkflow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-Products.CMFPlone
#BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.interface zope.i18nmessageid
%py_requires Products.CMFCore Products.GenericSetup
#py_requires Products.CMFPlone
# for tests:
%py_requires zope.testing
#py_requires Products.PloneTestCase

%description
Plone product that allows you to define workflow policies that define
content type to workflow mappings that can be applied in any sub-folder
of your Plone site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Plone product that allows you to define workflow policies that define
content type to workflow mappings that can be applied in any sub-folder
of your Plone site.

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
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev0.git20140416
- Initial build for Sisyphus

