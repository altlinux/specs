%define oname Products.TextIndexNG3
Name: python-module-%oname
Version: 3.4.9
Release: alt1.git20141123
Summary: Pluggable fulltext indexing solution for Zope 2 and Zope 3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.TextIndexNG3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/Products.TextIndexNG3.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-Pillow
BuildPreReq: python-module-zopyx.txng3.core
BuildPreReq: python-module-zopyx.txng3.ext
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-zope.app.zapi
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zopyx.txng3.core zopyx.txng3.ext Products.GenericSetup
%py_requires Products.CMFDefault Products.ATContentTypes zope.component
%py_requires Products.CMFCore Products.ZCatalog Products.PageTemplates
%py_requires zope.app.zapi zope.interface

%description
TXNG 3 is the reimplementation of the well-known TextIndexNG product for
Zope 2 using Zope 3 technologies. The current implementation runs
out-of-the-box on Zope 2 (in combination with Five). The core
implementation can be re-used easily in Zope 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.indexer Products.PloneTestCase

%description tests
TXNG 3 is the reimplementation of the well-known TextIndexNG product for
Zope 2 using Zope 3 technologies. The current implementation runs
out-of-the-box on Zope 2 (in combination with Five). The core
implementation can be re-used easily in Zope 3.

This package contains tests for %oname.

%prep
%setup

rm -fR $(find ./ -name .svn)

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd Products/TextIndexNG3
cp -fR Extensions adapters doc i18n interfaces profiles pt skins tests \
	%buildroot%python_sitelibdir/Products/TextIndexNG3/
popd

%check
python setup.py test

%files
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.9-alt1.git20141123
- Initial build for Sisyphus

