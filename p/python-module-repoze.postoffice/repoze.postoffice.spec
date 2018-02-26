%define oname repoze.postoffice
Name: python-module-%oname
Version: 0.17
Release: alt1
Summary: Provides central depot for incoming mail for use by applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.postoffice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Version 0.17

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

