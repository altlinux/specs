%define oname zc.catalogqueue
Name: python-module-%oname
Version: 0.3.1
Release: alt2.1
Summary: A queue for catalog indexing
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.catalogqueue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires pytz ZODB3 zope.interface

%description
A catalog queue provides a queue for catalog indexing. The basic idea is
to queue catalog operations so:

 * Operations can be batched for greater efficiency
* Application requests don't have to wait for indexing to be done

The benefits of queueing are especially significant when text indexes
are used.

%package tests
Summary: Tests for zc.catalogqueue
Group: Development/Python
Requires: %name = %version-%release

%description tests
A catalog queue provides a queue for catalog indexing. The basic idea is
to queue catalog operations so:

 * Operations can be batched for greater efficiency
* Application requests don't have to wait for indexing to be done

The benefits of queueing are especially significant when text indexes
are used.

This package contains tests for zc.catalogqueue.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

