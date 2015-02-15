%define oname Products.PloneExFile
Name: python-module-%oname
Version: 4.2.0
Release: alt1.git20120427
Summary: A Plone file with an attachment, supporting preview & indexing
License: GPLv2+
Group: Development/Python
Url: https://github.com/duffyd/Products.PloneExFile
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/duffyd/Products.PloneExFile.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.AttachmentField
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.CMFCore Products.LinguaPlone
%py_requires Products.AttachmentField Products.ATContentTypes
%py_requires plone.app.upgrade zope.interface

%description
A Plone file with an attachment, supporting preview & indexing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
A Plone file with an attachment, supporting preview & indexing.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/Products
cp -fR src/Products/PloneExFile %buildroot%python_sitelibdir/Products/
cp -fR src/*.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt *.md docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.git20120427
- Initial build for Sisyphus

