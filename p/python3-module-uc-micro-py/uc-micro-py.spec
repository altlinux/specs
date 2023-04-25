%define _unpackaged_files_terminate_build 1
%define pypi_name uc-micro-py
%define mod_name uc_micro

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1
Summary: Micro subset of unicode data files for linkify-it-py projects
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uc-micro-py
Vcs: https://github.com/tsutsu3/uc.micro-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This is a Python port of uc.micro.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
