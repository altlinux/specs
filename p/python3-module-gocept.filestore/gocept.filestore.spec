%define mname gocept
%define oname %mname.filestore

%def_with check

Name: python3-module-%oname
Version: 0.5
Release: alt1

Summary: Provides maildir like access to files
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/gocept.filestore/
Vcs: https://github.com/gocept/gocept.filestore

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.deferredimport
BuildRequires: python3-module-zope.testrunner
%endif

%py3_provides %oname

%description
The filestore is an easy way to to process files with multiple processes
without needing locks.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
The filestore is an easy way to to process files with multiple processes
without needing locks.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%tox_check

%files
%doc *.txt README.md
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests.*
%exclude %python3_sitelibdir/*.pth

%files tests
%python3_sitelibdir/%mname/*/tests.*


%changelog
* Wed Mar 29 2023 Anton Vyatkin <toni@altlinux.org> 0.5-alt1
- New version 0.5.

* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt1
- Version updated to 0.4
- porting on python3

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.1
- (AUTO) subst_x86_64.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.3-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

