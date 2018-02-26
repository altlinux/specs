%define oname zc.lockfile

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt3
Summary: Basic inter-process locks
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.lockfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%if_with python3
%package -n python3-module-%oname
Summary: Basic inter-process locks (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%package -n python3-module-%oname-tests
Summary: Tests for zc.lockfile (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

This package contains tests for zc.lockfile.
%endif

%package tests
Summary: Tests for zc.lockfile
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

This package contains tests for zc.lockfile.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

