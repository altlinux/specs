%define oname Products.PFGExtendedMailAdapter
Name: python-module-%oname
Version: 2.4
Release: alt1.git20130506
Summary: Adds extended mail adapter to Products.PloneFormGen
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PFGExtendedMailAdapter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PFGExtendedMailAdapter.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-hexagonit.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PloneFormGen

%description
This package extends PloneFormGen default mail adapter with the image
and file attachments.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing

%description tests
This package extends PloneFormGen default mail adapter with the image
and file attachments.

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
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.git20130506
- Initial build for Sisyphus

