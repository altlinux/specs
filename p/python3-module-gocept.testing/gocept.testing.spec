%define mname gocept
%define oname %mname.testing

%def_with check

Name: python3-module-%oname
Version: 4.0
Release: alt1

Summary: A collection of test helpers, additional assertions, and the like
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/gocept.testing/
VCS: https://github.com/gocept/gocept.testing

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
This package collects various helpers for writing tests.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%mname/*/tests


%changelog
* Wed May 22 2024 Anton Vyatkin <toni@altlinux.org> 4.0-alt1
- New version 4.0.

* Tue Jan 23 2024 Anton Vyatkin <toni@altlinux.org> 3.0-alt2
- Fix FTBFS.

* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- new version 3.0

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.1-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1
- (AUTO) subst_x86_64.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus

