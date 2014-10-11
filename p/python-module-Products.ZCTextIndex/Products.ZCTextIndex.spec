%define oname Products.ZCTextIndex

%def_disable check

Name: python-module-%oname
Version: 2.13.5
Release: alt1
Summary: Full text indexing for ZCatalog / Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZCTextIndex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.interface

%description
This distribution contains a full text indexing facility for Zope 2 and
more specifically for Products.ZCatalog.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This distribution contains a full text indexing facility for Zope 2 and
more specifically for Products.ZCatalog.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.5-alt1
- Initial build for Sisyphus

