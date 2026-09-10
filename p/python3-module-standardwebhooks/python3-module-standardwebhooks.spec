%define _unpackaged_files_terminate_build 1
%define pypi_name standardwebhooks
%define mod_name standardwebhooks

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Standard Webhooks library for verifying and signing webhooks from Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/standardwebhooks/
Vcs: https://github.com/standard-webhooks/standard-webhooks

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

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
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 10 2026 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- Packaged for ALT Sisyphus.
