%define _unpackaged_files_terminate_build 1
%define pypi_name fasttransport
%define mod_name fasttransport

# no tests
%def_without check

Name: python3-module-%pypi_name
Version: 0.0.1
Release: alt1

Summary: Sync and async HTTP transports over httpx2, plus base classes for small REST clients
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fasttransport/
Vcs: https://github.com/AnswerDotAI/fasttransport

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
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Wed Aug 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.1-alt1
- Packaged for ALT Sisyphus.
