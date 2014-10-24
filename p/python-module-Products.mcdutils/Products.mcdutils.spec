%define oname Products.mcdutils
Name: python-module-%oname
Version: 0.2
Release: alt1.b3
Summary: A Zope2 product which provides facilities for storing sessions in memcached
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.mcdutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
The 'mcdutils' product supplies a replacement for the ZODB-based session
data container supplied by the 'Transience' product, shipped with the
Zope core. Rather than using a ZODB storage as the backing store for
session data, as 'Transience' does, 'mcdutils' stores session data in a
cluster of one or more 'memcached' servers.

This approach is a bit of a cheat, as it uses the daemons as primary
stores, rather than as caches for results of an expensive query.
Nevertheless, the semantics are not a bad match for typical session
usage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The 'mcdutils' product supplies a replacement for the ZODB-based session
data container supplied by the 'Transience' product, shipped with the
Zope core. Rather than using a ZODB storage as the backing store for
session data, as 'Transience' does, 'mcdutils' stores session data in a
cluster of one or more 'memcached' servers.

This approach is a bit of a cheat, as it uses the daemons as primary
stores, rather than as caches for results of an expensive query.
Nevertheless, the semantics are not a bad match for typical session
usage.

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
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/ftests

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/ftests

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.b3
- Initial build for Sisyphus

