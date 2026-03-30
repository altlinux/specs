%define _unpackaged_files_terminate_build 1
%define pypi_name ncclient
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1.1
Summary: Python library for NETCONF clients
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ncclient/
VCS: https://github.com/ncclient/ncclient
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-sphinx

BuildRequires: python3-module-lxml
BuildRequires: python3-module-paramiko
%endif

%filter_from_requires /python3(ssh.*)/d

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. ncclient
was developed by Shikar Bhushan. It is now maintained by Leonidas
Poulopoulos (@leopoul)

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag v"%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra test/

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- Demodernized packaging.

* Mon Mar 16 2026 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- 0.6.19 -> 0.7.0.

* Tue Mar 04 2025 Stanislav Levin <slev@altlinux.org> 0.6.19-alt1
- 0.6.17 -> 0.6.19.

* Mon Feb 24 2025 Stanislav Levin <slev@altlinux.org> 0.6.17-alt1
- 0.6.16 -> 0.6.17.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 0.6.16-alt1
- 0.6.13 -> 0.6.16.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.13-alt2
- Fixed FTBFS.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 0.6.13-alt1
- 0.6.12 -> 0.6.13.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.6.12-alt1
- 0.6.3 -> 0.6.12.
- Enabled testing.

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3
- build python3 package

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.2-alt1
- New version

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.7-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.3-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.2-alt1
- Initla build for ALT

