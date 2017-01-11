%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.lockfile

%def_with python3

Name: python-module-%oname
Version: 1.2.1
#Release: alt1.1.1
Summary: Basic inter-process locks
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.lockfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/bd/84/0299bbabbc9d3f84f718ba1039cc068030d3ad723c08f82a64337edf901e/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
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
%setup -q -n %{oname}-%{version}
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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 01 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

