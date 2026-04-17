%define _unpackaged_files_terminate_build 1
%define pypi_name sseclient-py
%define mod_name sseclient

%def_with check

Name: python3-module-%pypi_name
Version: 1.9.0
Release: alt1

Summary: SSE client for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sseclient-py/
Vcs: https://github.com/mpetazzoni/sseclient

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A Python client for SSE event sources that seamlessly integrates with
urllib3 and requests.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

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
* Fri Apr 17 2026 Anton Zhukharev <ancieg@altlinux.org> 1.9.0-alt1
- Packaged for ALT Sisyphus.
