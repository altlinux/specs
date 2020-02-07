%define mname gocept
%define oname %mname.testing

%def_without check

Name: python3-module-%oname
Version: 1.10.1
Release: alt2

Summary: A collection of test helpers, additional assertions, and the like
License: ZPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/gocept.testing/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mock python3-module-six
BuildRequires: python3-module-pytest-cov

%py3_provides %oname
%py3_requires %mname mock six


%description
This package collects various helpers for writing tests.

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
%__python3 setup.py test
py.test3 -vv

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.1-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1
- (AUTO) subst_x86_64.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus

