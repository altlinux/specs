%define _unpackaged_files_terminate_build 1
%define pypi_name llm-echo
%define mod_name llm_echo

# requires the Internet connection
%def_without check

Name: python3-module-%pypi_name
Version: 0.3a3
Release: alt1

Summary: Debug plugin for LLM providing an echo model
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/llm-echo/
Vcs: https://github.com/simonw/llm-echo

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

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.3a3-alt1
- Packaged for ALT Sisyphus.
