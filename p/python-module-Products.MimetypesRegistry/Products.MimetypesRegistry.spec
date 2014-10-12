%define oname Products.MimetypesRegistry
Name: python-module-%oname
Version: 2.0.7
Release: alt1.dev0.git20140907
Summary: MIME type handling for Zope
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.MimetypesRegistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.MimetypesRegistry.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-Products.CMFCore
#BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3 zope.contenttype zope.interface Products.CMFCore
%add_python_req_skip _winreg win32api win32con

%description
mimetypes_registry (the mimetypes tool) : handle mime types
information.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#py_requires Products.Archetypes

%description tests
mimetypes_registry (the mimetypes tool) : handle mime types
information.

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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.7-alt1.dev0.git20140907
- Initial build for Sisyphus

