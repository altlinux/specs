%define _unpackaged_files_terminate_build 1
%define pypi_name handy-archives
%define mod_name handy_archives

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt3.35.g735b08c

Summary: Some handy archive helpers for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/handy-archives/
Vcs: https://github.com/domdfcoding/handy-archives

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
BuildRequires: python3-test
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt3.35.g735b08c
- Fixed FTBFS (apply upstream fixes).

* Sun Oct 19 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt2
- Fixed FTBFS.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1.1
- NMU: Ignore deprecation warnings in tests.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt2
- fix requires

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- initial build for Sisyphus (temporary broken package)
