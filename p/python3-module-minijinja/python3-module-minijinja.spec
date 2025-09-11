%define pname minijinja

%def_with check

Name:    python3-module-%pname
Version: 2.1.2
Release: alt2

Summary: Experimental binding of MiniJinja to Python3
License: Apache-2.0
Group:   Development/Python3
Url:     https://github.com/mitsuhiko/minijinja

Source: %name-%version.tar
Patch0: minijinja-2.1.2-fix-pytest-8.4.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-maturin

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
pushd %pname-py
%pyproject_build
popd

%install
pushd %pname-py
%pyproject_install
popd

%check
pushd %pname-py
%pyproject_run_pytest
popd

%files
%doc %pname-py/*.md
%python3_sitelibdir/%pname
%python3_sitelibdir/%{pyproject_distinfo %pname}

%changelog
* Thu Sep 11 2025 Stanislav Levin <slev@altlinux.org> 2.1.2-alt2
- NMU: fixed FTBFS (pytest 8.4.0).

* Tue Aug 06 2024 Alexander Burmatov <thatman@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus.
