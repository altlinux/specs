%define _unpackaged_files_terminate_build 1
%define pypi_name condense-json
%define mod_name condense_json

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.2
Release: alt1

Summary: Python function for condensing JSON using replacement strings
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/condense-json/
Vcs: https://github.com/simonw/condense-json

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

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
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Apr 08 2025 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- Built for ALT Sisyphus.


