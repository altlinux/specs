%define oname tempstorage

%def_with python3

Name: python-module-%oname
Version: 2.12.2
Release: alt3
Summary: A RAM-based storage for ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/tempstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3

%description
A storage implementation which uses RAM to persist objects, much like
MappingStorage. Unlike MappingStorage, it needs not be packed to get rid
of non-cyclic garbage and it does rudimentary conflict resolution. This
is a ripoff of Jim's Packless bsddb3 storage.

%package -n python3-module-%oname
Summary: A RAM-based storage for ZODB
Group: Development/Python3
%py3_requires ZODB3

%description -n python3-module-%oname
A storage implementation which uses RAM to persist objects, much like
MappingStorage. Unlike MappingStorage, it needs not be packed to get rid
of non-cyclic garbage and it does rudimentary conflict resolution. This
is a ripoff of Jim's Packless bsddb3 storage.

%package -n python3-module-%oname-tests
Summary: Tests for tempstorage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A storage implementation which uses RAM to persist objects, much like
MappingStorage. Unlike MappingStorage, it needs not be packed to get rid
of non-cyclic garbage and it does rudimentary conflict resolution. This
is a ripoff of Jim's Packless bsddb3 storage.

This package contains tests for tempstorage.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt3
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt2
- Avoid requirement on ZODB3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt1
- Version 2.12.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt2
- Added necessary requirements

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt1
- Initial build for Sisyphus

