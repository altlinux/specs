%define _unpackaged_files_terminate_build 1
%define mname hurry
%define oname %mname.filesize

%def_with check

Name: python3-module-%oname
Version: 0.9
Release: alt2
Summary: A simple Python library for human readable file sizes (or anything sized in bytes)
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/hurry.filesize/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
%py3_requires %mname

%description
hurry.filesize a simple Python library that can take a number of bytes
and returns a human-readable string with the size in it, in kilobytes
(K), megabytes (M), etc.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hurry.filesize a simple Python library that can take a number of bytes
and returns a human-readable string with the size in it, in kilobytes
(K), megabytes (M), etc.

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
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests.*
%exclude %python3_sitelibdir/*-nspkg.pth

%files tests
%python3_sitelibdir/%mname/*/tests.*

%changelog
* Sat Jan 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.9-alt2
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

