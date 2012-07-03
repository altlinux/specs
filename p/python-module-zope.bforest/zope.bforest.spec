%define oname zope.bforest
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: Mappings based transparently on multiple BTrees; good for rotating caches and logs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.bforest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

