%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname repoze.postoffice

%def_with python3

Name: python-module-%oname
Version: 0.25
#Release: alt2.1
Summary: Provides central depot for incoming mail for use by applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.postoffice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/17/fc/0d30131dd129dec51583aab7c20968823f3a7d5b73d67c9d4b22a82d06c5/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze ZODB3 repoze.zodbconn

%description
`repoze.postoffice` provides a centralized depot for collecting incoming
email for consumption by multiple applications.  Incoming mail is sorted
into queues according to rules with the expectation that each
application will then consume its own queue.  Each queue is a
first-in-first-out (FIFO) queue, so messages are processed in the order
received.

ZODB is used for storage and is also used to provide the client
interface.  `repoze.postoffice` clients create a ZODB connection and
manipulate models.  This makes consuming the message queue in the
context of a transaction, relatively simple.

%package -n python3-module-%oname
Summary: Provides central depot for incoming mail for use by applications
Group: Development/Python3
%py3_requires repoze ZODB3 repoze.zodbconn

%description -n python3-module-%oname
`repoze.postoffice` provides a centralized depot for collecting incoming
email for consumption by multiple applications.  Incoming mail is sorted
into queues according to rules with the expectation that each
application will then consume its own queue.  Each queue is a
first-in-first-out (FIFO) queue, so messages are processed in the order
received.

ZODB is used for storage and is also used to provide the client
interface.  `repoze.postoffice` clients create a ZODB connection and
manipulate models.  This makes consuming the message queue in the
context of a transaction, relatively simple.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.postoffice
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
`repoze.postoffice` provides a centralized depot for collecting incoming
email for consumption by multiple applications.  Incoming mail is sorted
into queues according to rules with the expectation that each
application will then consume its own queue.  Each queue is a
first-in-first-out (FIFO) queue, so messages are processed in the order
received.

ZODB is used for storage and is also used to provide the client
interface.  `repoze.postoffice` clients create a ZODB connection and
manipulate models.  This makes consuming the message queue in the
context of a transaction, relatively simple.

This package contains tests for repoze.postoffice.

%package tests
Summary: Tests for repoze.postoffice
Group: Development/Python
Requires: %name = %version-%release

%description tests
`repoze.postoffice` provides a centralized depot for collecting incoming
email for consumption by multiple applications.  Incoming mail is sorted
into queues according to rules with the expectation that each
application will then consume its own queue.  Each queue is a
first-in-first-out (FIFO) queue, so messages are processed in the order
received.

ZODB is used for storage and is also used to provide the client
interface.  `repoze.postoffice` clients create a ZODB connection and
manipulate models.  This makes consuming the message queue in the
context of a transaction, relatively simple.

This package contains tests for repoze.postoffice.

%prep
%setup -q -n %{oname}-%{version}

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
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt2
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1
- Version 0.24

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1
- Version 0.23

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Version 0.21

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Version 0.17

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

