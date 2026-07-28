%define _unpackaged_files_terminate_build 1
%define pypi_name pyinfra-testing
%define mod_name pyinfra_testing

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1

Summary: Generate Python unit tests from JSON and YAML files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyinfra-testing/
Vcs: https://github.com/pyinfra-dev/pyinfra-testing

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Obsoletes: python3-module-pyinfra-testgen <= 0.1.1-alt1
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
* Tue Jul 28 2026 Anton Zhukharev <ancieg@altlinux.org> 0.2.1-alt1
- Renamed from 'pyinfra-testgen' to 'pyinfra-testing'.
- Updated to 0.2.1.

* Thu Jan 15 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Packaged for ALT Sisyphus.
