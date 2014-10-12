%define oname plone.batching
Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: Batching facilities used in Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.batching/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone

%description
This package includes facilities for creating a batched sequence.

It originated from the the PloneBatch module written for Plone which in
itself has been based on Zope2's ZTUtils.Batch.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package includes facilities for creating a batched sequence.

It originated from the the PloneBatch module written for Plone which in
itself has been based on Zope2's ZTUtils.Batch.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

