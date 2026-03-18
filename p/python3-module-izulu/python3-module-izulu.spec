%define _unpackaged_files_terminate_build 1
%define pypi_name izulu
%define mod_name izulu

%def_with check

Name: python3-module-%pypi_name
Version: 0.75.0
Release: alt1

Summary: An exceptional library
License: MITX
Group: Development/Python3
Url: https://pypi.org/project/izulu/
Vcs: https://github.com/pyctrl/izulu

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
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.75.0-alt1
- Updated to 0.75.0.

* Tue Mar 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.50.0-alt1
- Updated to 0.50.0.

* Mon Mar 24 2025 Anton Zhukharev <ancieg@altlinux.org> 0.20.1-alt1
- Updated to 0.20.1.

* Fri Mar 21 2025 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt1
- Updated to 0.10.2.

* Mon Mar 17 2025 Anton Zhukharev <ancieg@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Fri Mar 14 2025 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt1
- Built for ALT Sisyphus.
