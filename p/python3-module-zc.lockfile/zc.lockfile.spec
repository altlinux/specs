%define _unpackaged_files_terminate_build 1
%define oname zc.lockfile

%def_with check

Name: python3-module-%oname
Version: 2.0
Release: alt1
Summary: Basic inter-process locks
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zc.lockfile/
#Git: https://github.com/zopefoundation/zc.lockfile.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.testing
%endif

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%package tests
Summary: Tests for zc.lockfile (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

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

%build
%python3_build

%install
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*

%changelog
* Fri Jan 17 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.0-alt1
- NMU: 1.2.1 -> 2.0
- Remove python2 module build
- Change package repo style from srpm to git subtree
- Add unittests execution
- Cleanup BR:
- Fix license

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

