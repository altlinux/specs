%define _unpackaged_files_terminate_build 1
%define pypi_name httpx2-pytest
%define mod_name pytest_httpx2

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: Send responses to httpx2
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/httpx-pytest/
Vcs: https://github.com/angryfoxx/httpx2-pytest

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
%pyproject_builddeps_metadata_extra testing
%endif

%description
Send responses to HTTPX2 using pytest.

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
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 24 2026 Anton Zhukharev <ancieg@altlinux.org> 1.0.1-alt1
- Packaged for ALT Sisyphus.
