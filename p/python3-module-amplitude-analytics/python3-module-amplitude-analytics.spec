%define _unpackaged_files_terminate_build 1
%define pypi_name amplitude-analytics
%define mod_name amplitude

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.3
Release: alt1

Summary: The official Amplitude backend Python SDK for server-side instrumentation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/amplitude-analytics/
Vcs: https://github.com/amplitude/Amplitude-Python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

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
%pyproject_run_unittest discover -v -s ./src -p 'test_*.py'

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 1.2.3-alt1
- Packaged for ALT Sisyphus.
