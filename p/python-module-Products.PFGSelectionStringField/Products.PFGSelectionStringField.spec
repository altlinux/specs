%define oname Products.PFGSelectionStringField
Name: python-module-%oname
Version: 2.5.1
Release: alt1.git20130510
Summary: Adds selection field type with string field to Products.PloneFormGen
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PFGSelectionStringField/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PFGSelectionStringField.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.GenericSetup

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PloneFormGen Products.CMFCore Products.Archetypes
%py_requires Products.CMFPlone Products.ATContentTypes
%py_requires Products.GenericSetup

%description
Products.PFGSelectionStringField provides selection field with string
field for PloneFormGen.

This is useful when you need some comments related to the selected
option.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing

%description tests
Products.PFGSelectionStringField provides selection field with string
field for PloneFormGen.

This is useful when you need some comments related to the selected
option.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20130510
- Initial build for Sisyphus

