%define _unpackaged_files_terminate_build 1

%define pypi_name pytest-testinfra
%define mod_name testinfra

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 10.2.2
Release: alt1.1
Summary: pytest plugin for infrastructure testing
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-testinfra/
Vcs: https://github.com/pytest-dev/pytest-testinfra
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-ansible
BuildRequires: python3-module-distro
BuildRequires: python3-module-looseversion
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pywinrm
BuildRequires: python3-module-salt
BuildRequires: python3-module-tornado
BuildRequires: /proc
%endif

%add_python_extra ansible
%add_python_extra paramiko
%add_python_extra winrm
%add_python_extra salt

%description
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on. Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine

%prep
%setup
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra test

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 10.2.2-alt1.1
- Demodernized packaging.

* Mon Mar 31 2025 Stanislav Levin <slev@altlinux.org> 10.2.2-alt1
- 10.1.1 -> 10.2.2.

* Fri May 31 2024 Stanislav Levin <slev@altlinux.org> 10.1.1-alt1
- 10.0.0 -> 10.1.1.

* Mon Dec 18 2023 Slava Aseev <ptrnine@altlinux.org> 10.0.0-alt1
- New version

* Thu Sep 15 2022 Slava Aseev <ptrnine@altlinux.org> 6.8.0-alt1
- new version

* Mon Nov 15 2021 Slava Aseev <ptrnine@altlinux.org> 6.4.0-alt1
- Initial build for ALT

