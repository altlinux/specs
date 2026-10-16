%define _unpackaged_files_terminate_build 1
%define pypi_name inversion
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1
Summary: Flexible version handling
License: BSD-3-Clause or Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/inversion
Vcs: https://github.com/jimporter/inversion
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
%pyproject_builddeps_metadata_extra test
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
rm -r %buildroot%python3_sitelibdir/doc/

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 16 2026 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for sisyphus.
