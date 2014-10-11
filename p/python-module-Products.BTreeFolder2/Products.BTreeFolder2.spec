%define oname Products.BTreeFolder2

%def_disable check

Name: python-module-%oname
Version: 2.13.4
Release: alt1
Summary: A BTree based implementation for Zope 2's OFS
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.BTreeFolder2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ZODB3 python-module-zope.container
BuildPreReq: python-module-zope.event python-module-zope.lifecycleevent

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3 zope.container zope.event zope.lifecycleevent

%description
BTreeFolder2 is a Zope product that acts like a Zope 2 OFS folder but
can store many more items.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BTreeFolder2 is a Zope product that acts like a Zope 2 OFS folder but
can store many more items.

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
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt1
- Initial build for Sisyphus

