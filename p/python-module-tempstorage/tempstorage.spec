%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname tempstorage

%def_with python3

Name: python-module-%oname
Version: 3.0
Release: alt1.1
Summary: A RAM-based storage for ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/tempstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/tempstorage.git
Source0: https://pypi.python.org/packages/9b/6e/79cd4bae58329f6c0d15bb906300b474f9c3988bfa414a72f5a3dbdb02ae/%{oname}-%{version}.zip
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.testing python-module-ZODB3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3 python3-module-zope.testing
#BuildPreReq: python3-module-ZODB3 python3-module-zodbpickle
%endif

%py_requires ZODB3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZODB python-module-persistent python-module-pytest python-module-setuptools python-module-transaction python-module-zc.lockfile python-module-zdaemon python-module-zodbpickle python-module-zope.event python-module-zope.exceptions python-module-zope.interface python-module-zope.proxy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-BTrees python3-module-ZODB python3-module-persistent python3-module-pytest python3-module-setuptools python3-module-transaction python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.event python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.proxy
BuildRequires: python-module-ZEO python-module-setuptools python-module-zope.testing python3-module-ZEO python3-module-setuptools python3-module-zodbpickle python3-module-zope.testing rpm-build-python3 time

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
%setup -q -n %{oname}-%{version}

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13-alt1.dev0.git20140318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.13-alt1.dev0.git20140318.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13-alt1.dev0.git20140318
- Version 2.13.dev0
- Enabled testing

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

