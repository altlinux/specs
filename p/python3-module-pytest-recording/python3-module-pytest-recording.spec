%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-recording
%define mod_name pytest_recording

# requires the Internet connection
%def_with check

Name: python3-module-%pypi_name
Version: 0.13.4
Release: alt1

Summary: A pytest plugin to record and replay HTTP traffic
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-recording/
Vcs: https://github.com/kiwicom/pytest-recording

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
%pyproject_builddeps_metadata_extra tests
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
# Skip test_block_network_with_allowed hosts due to it requires the Internet
# connection to do requests.
%pyproject_run_pytest -vra \
    --deselect 'tests/test_blocking_network.py::test_block_network_with_allowed_hosts'

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.13.4-alt1
- Packaged for ALT Sisyphus.
