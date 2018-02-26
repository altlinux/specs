%define oname tempstorage
Name: python-module-%oname
Version: 2.12.1
Release: alt2.1
Summary: A RAM-based storage for ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/tempstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3

%description
A storage implementation which uses RAM to persist objects, much like
MappingStorage. Unlike MappingStorage, it needs not be packed to get rid
of non-cyclic garbage and it does rudimentary conflict resolution. This
is a ripoff of Jim's Packless bsddb3 storage.

%package tests
Summary: Tests for tempstorage
Group: Development/Python
Requires: %name = %version-%release

%description tests
A storage implementation which uses RAM to persist objects, much like
MappingStorage. Unlike MappingStorage, it needs not be packed to get rid
of non-cyclic garbage and it does rudimentary conflict resolution. This
is a ripoff of Jim's Packless bsddb3 storage.

This package contains tests for tempstorage.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt2
- Added necessary requirements

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt1
- Initial build for Sisyphus

