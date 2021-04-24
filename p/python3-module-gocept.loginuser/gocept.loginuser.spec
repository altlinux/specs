%define mname gocept
%define oname %mname.loginuser

Name: python3-module-%oname
Version: 3.0
Release: alt1

Summary: Sqlalchemy user object and password management

License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/gocept.loginuser/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
Sqlalchemy user object and password management.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Sqlalchemy user object and password management.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test

%files
%doc *.txt doc/*.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- NMU: new version 3.0 (with rpmrb script)
- NMU: cleanup sources scheme, drop tests subpackage

* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt1
- Version updated to 2.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (AUTO) subst_x86_64.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

