%define oname zope.bforest

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt3.1
Summary: Mappings based transparently on multiple BTrees; good for rotating caches and logs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.bforest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.interface ZODB3

%description
BForests are dictionary-like objects that use multiple BTrees for a
backend and support rotation of the composite trees. This supports
various implementations of timed member expirations, enabling caches and
semi-persistent storage. A useful and simple subclass would be to
promote a key-value pair to the first (newest) bucket whenever the key
is accessed, for instance. It also is useful with disabling the rotation
capability.

Like btrees, bforests come in four flavors: Integer-Integer (IIBForest),
Integer-Object (IOBForest), Object-Integer (OIBForest), and
Object-Object (OOBForest). The examples here will deal with them in the
abstract: we will create classes from the imaginary and representative
BForest class, and generate keys from KeyGenerator and values from
ValueGenerator. From the examples you should be able to extrapolate
usage of all four types.

First let's instantiate a bforest and look at an empty example. By
default, a new bforest creates two composite btree buckets.

%package -n python3-module-%oname
Summary: Mappings based transparently on multiple BTrees; good for rotating caches and logs
Group: Development/Python3
%py3_requires zope zope.interface ZODB3

%description -n python3-module-%oname
BForests are dictionary-like objects that use multiple BTrees for a
backend and support rotation of the composite trees. This supports
various implementations of timed member expirations, enabling caches and
semi-persistent storage. A useful and simple subclass would be to
promote a key-value pair to the first (newest) bucket whenever the key
is accessed, for instance. It also is useful with disabling the rotation
capability.

Like btrees, bforests come in four flavors: Integer-Integer (IIBForest),
Integer-Object (IOBForest), Object-Integer (OIBForest), and
Object-Object (OOBForest). The examples here will deal with them in the
abstract: we will create classes from the imaginary and representative
BForest class, and generate keys from KeyGenerator and values from
ValueGenerator. From the examples you should be able to extrapolate
usage of all four types.

%package -n python3-module-%oname-tests
Summary: Tests for zope.bforest
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
BForests are dictionary-like objects that use multiple BTrees for a
backend and support rotation of the composite trees. This supports
various implementations of timed member expirations, enabling caches and
semi-persistent storage. A useful and simple subclass would be to
promote a key-value pair to the first (newest) bucket whenever the key
is accessed, for instance. It also is useful with disabling the rotation
capability.

This package contains tests for zope.bforest.

%package tests
Summary: Tests for zope.bforest
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
BForests are dictionary-like objects that use multiple BTrees for a
backend and support rotation of the composite trees. This supports
various implementations of timed member expirations, enabling caches and
semi-persistent storage. A useful and simple subclass would be to
promote a key-value pair to the first (newest) bucket whenever the key
is accessed, for instance. It also is useful with disabling the rotation
capability.

This package contains tests for zope.bforest.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

