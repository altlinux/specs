%define _unpackaged_files_terminate_build 1
%define pypi_name inline-snapshot
%define mod_name inline_snapshot

%def_with check

Name: python3-module-%pypi_name
Version: 0.23.2
Release: alt1

Summary: Create and update inline snapshots in your python tests
License: MIT
Group: Development/Python3
Url: https://15r10nk.github.io/inline-snapshot/latest/
Vcs: https://github.com/15r10nk/inline-snapshot

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-mypy
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
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
%pyproject_run_pytest -k "not pyright"

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 17 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.23.2-alt1
- Updated to 0.23.2.

* Wed Apr 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.23.0-alt1
- New version 0.23.0.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.17.1-alt1
- New version 0.17.1.

* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
