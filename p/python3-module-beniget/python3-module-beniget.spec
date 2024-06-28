%define _unpackaged_files_terminate_build 1

%define pypi_name beniget
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.2.post1
Release: alt1
Summary: Extract semantic information about static Python code
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/beniget/
Vcs: https://github.com/serge-sans-paille/beniget/
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Beniget provides a static over-approximation of the global and local definitions
inside Python Module/Class/Function. It can also compute def-use chains from
each definition.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover tests

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 28 2024 Stanislav Levin <slev@altlinux.org> 0.4.2.post1-alt1
- 0.4.1 -> 0.4.2.post1.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- NMU: added missing build dependency on setuptools.

* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- first build for Sisyphus
