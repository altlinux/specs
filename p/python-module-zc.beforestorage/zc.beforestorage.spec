%define oname zc.beforestorage

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt2.1
Summary: View storage before a given time
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.beforestorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.interface

%description
ZODB storages typically store multiple object revisions to support
features such as multi-version concurrency control and undo.  In the
case of the mod popular storage implementation, old revisions aren't
discarded until a pack.  This feature has often been exploited to
perform time travel, allowing one to look at a database as it existed
in at some point in time.  In the past, this has been possible with
file storage by specifying a time at which to open the file
storage. This works fairly well, but is very slow for large databases
because existing index files can't easily be used.  Time travel is
also supported for individual objects through the ZODB history
mechanism.

%package -n python3-module-%oname
Summary: View storage before a given time
Group: Development/Python3
%py3_requires ZODB3 zope.interface

%description -n python3-module-%oname
ZODB storages typically store multiple object revisions to support
features such as multi-version concurrency control and undo.  In the
case of the mod popular storage implementation, old revisions aren't
discarded until a pack.  This feature has often been exploited to
perform time travel, allowing one to look at a database as it existed
in at some point in time.  In the past, this has been possible with
file storage by specifying a time at which to open the file
storage. This works fairly well, but is very slow for large databases
because existing index files can't easily be used.  Time travel is
also supported for individual objects through the ZODB history
mechanism.

%package -n python3-module-%oname-tests
Summary: Tests for zc.beforestorage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
ZODB storages typically store multiple object revisions to support
features such as multi-version concurrency control and undo.  In the
case of the mod popular storage implementation, old revisions aren't
discarded until a pack.  This feature has often been exploited to
perform time travel, allowing one to look at a database as it existed
in at some point in time.  In the past, this has been possible with
file storage by specifying a time at which to open the file
storage. This works fairly well, but is very slow for large databases
because existing index files can't easily be used.  Time travel is
also supported for individual objects through the ZODB history
mechanism.

This package contains tests for zc.beforestorage.

%package tests
Summary: Tests for zc.beforestorage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
ZODB storages typically store multiple object revisions to support
features such as multi-version concurrency control and undo.  In the
case of the mod popular storage implementation, old revisions aren't
discarded until a pack.  This feature has often been exploited to
perform time travel, allowing one to look at a database as it existed
in at some point in time.  In the past, this has been possible with
file storage by specifying a time at which to open the file
storage. This works fairly well, but is very slow for large databases
because existing index files can't easily be used.  Time travel is
also supported for individual objects through the ZODB history
mechanism.

This package contains tests for zc.beforestorage.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

