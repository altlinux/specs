%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-installer
%define pep503_name pyproject_installer

%define pyproject_installer export PYTHONPATH=$(pwd)/src; %__python3 -m %pep503_name -v

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1
Summary: Builder and installer of Python project
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-installer
VCS: https://github.com/stanislavlevin/pyproject_installer
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%py3_provides %pypi_name
# hide vendored distributions
%add_findprov_skiplist %python3_sitelibdir/%pep503_name/_vendor/*
# don't allow vendored distributions have deps other than stdlib
%add_findreq_skiplist %python3_sitelibdir/%pep503_name/_vendor/*

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
%endif

%description
This tool is intended to build wheel from Python source tree and install it.

%prep
%setup
%autopatch -p1

%build
%pyproject_installer build

%install
%pyproject_installer install --destdir=%buildroot

%check
%pyproject_installer run -- pytest -vra tests/unit

%files
%doc README.md
%python3_sitelibdir/%pep503_name/
%python3_sitelibdir/%pep503_name-%version.dist-info/

%changelog
* Tue Jul 11 2023 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2.

* Thu Jun 01 2023 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.5.0 -> 0.5.1.

* Fri Apr 14 2023 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Wed Jan 11 2023 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.0 -> 0.4.0.

* Thu Jun 16 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
