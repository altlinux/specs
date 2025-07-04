%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-crosshair
%define import_name hypothesis_crosshair_provider

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.24
Release: alt1

Summary: Level-up your Hypothesis tests with CrossHair
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hypothesis-crosshair/
Vcs: https://github.com/pschanely/hypothesis-crosshair

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
Add the power of solver-based symbolic execution to your Hypothesis
tests with CrossHair.

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
%doc LICENSE README.md
%python3_sitelibdir/%import_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.24-alt1
- Packaged for ALT Sisyphus.
