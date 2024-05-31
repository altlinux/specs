%define _unpackaged_files_terminate_build 1

%define pypi_name pytest-testinfra
%define mod_name testinfra

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%{expand:%%pyproject_runtimedeps_metadata -- --extra %1} \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 10.1.1
Release: alt1
Summary: pytest plugin for infrastructure testing
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-testinfra/
Vcs: https://github.com/pytest-dev/pytest-testinfra
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
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
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

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
* Fri May 31 2024 Stanislav Levin <slev@altlinux.org> 10.1.1-alt1
- 10.0.0 -> 10.1.1.

* Mon Dec 18 2023 Slava Aseev <ptrnine@altlinux.org> 10.0.0-alt1
- New version

* Thu Sep 15 2022 Slava Aseev <ptrnine@altlinux.org> 6.8.0-alt1
- new version

* Mon Nov 15 2021 Slava Aseev <ptrnine@altlinux.org> 6.4.0-alt1
- Initial build for ALT

