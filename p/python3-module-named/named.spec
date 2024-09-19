%define _unpackaged_files_terminate_build 1
%define pypi_name named
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1
Summary: Named types
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/named
Vcs: https://github.com/nekitdev/named
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 19 2024 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
