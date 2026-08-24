%define _unpackaged_files_terminate_build 1
%define pypi_name vermin
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1
Summary: Concurrently detect the minimum Python versions needed to run code
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/vermin
Vcs: https://github.com/netromdk/vermin
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
%endif

%description
%summary.

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
%pyproject_run -- make test

%files
%_bindir/vermin
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Aug 24 2026 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- Initial build for sisyphus.
