%define oname Products.PloneArticle
Name: python-module-%oname
Version: 4.0.0
Release: alt1.beta4.git20140930
Summary: A Plone document including images, attachments and links
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneArticle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneArticle.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone Products.ATReferenceBrowserWidget kss.core

%description
A Plone document including images, attachments and links, with a free
choice of layout.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
A Plone document including images, attachments and links, with a free
choice of layout.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/*tests

%files tests
%python_sitelibdir/Products/*/*tests

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.beta4.git20140930
- Initial build for Sisyphus

