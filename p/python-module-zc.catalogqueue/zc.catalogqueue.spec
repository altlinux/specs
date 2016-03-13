%define oname zc.catalogqueue

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt3.1
Summary: A queue for catalog indexing
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.catalogqueue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pytz ZODB3 zope.interface

%description
A catalog queue provides a queue for catalog indexing. The basic idea is
to queue catalog operations so:

 * Operations can be batched for greater efficiency
* Application requests don't have to wait for indexing to be done

The benefits of queueing are especially significant when text indexes
are used.

%package -n python3-module-%oname
Summary: A queue for catalog indexing
Group: Development/Python3
%py3_requires pytz ZODB3 zope.interface

%description -n python3-module-%oname
A catalog queue provides a queue for catalog indexing. The basic idea is
to queue catalog operations so:

 * Operations can be batched for greater efficiency
* Application requests don't have to wait for indexing to be done

The benefits of queueing are especially significant when text indexes
are used.

%package -n python3-module-%oname-tests
Summary: Tests for zc.catalogqueue
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A catalog queue provides a queue for catalog indexing. The basic idea is
to queue catalog operations so:

 * Operations can be batched for greater efficiency
* Application requests don't have to wait for indexing to be done

The benefits of queueing are especially significant when text indexes
are used.

This package contains tests for zc.catalogqueue.

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

%if_with python3
cp -fR . ../python3
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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

