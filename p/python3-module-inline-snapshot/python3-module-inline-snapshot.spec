%define _unpackaged_files_terminate_build 1
%define pypi_name inline-snapshot
%define mod_name inline_snapshot

%def_with check

Name: python3-module-%pypi_name
Version: 0.34.0
Release: alt1

Summary: Create and update inline snapshots in your python tests
License: MIT
Group: Development/Python3
Url: https://15r10nk.github.io/inline-snapshot/latest/
Vcs: https://github.com/15r10nk/inline-snapshot

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-mypy
BuildRequires: python3-module-black
BuildRequires: python3-module-isort
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
%pyproject_run_pytest -k "not pyright and not test_compare"

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 17 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.34.0-alt1
- NMU: updated to 0.34.0.

* Wed May 20 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.33.0-alt1
- NMU: updated to 0.33.0.

* Tue May 05 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.32.7-alt1
- Updated to 0.32.7.

* Tue Apr 21 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.32.6-alt1
- Updated to 0.32.6.

* Tue Mar 17 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.32.5-alt1
- Updated to 0.32.5.

* Wed Mar 04 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.32.4-alt1
- Updated to 0.32.4.

* Wed Feb 25 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.32.3-alt1
- Updated to 0.32.3.

* Tue Dec 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.31.1-alt1
- Updated to 0.31.1.

* Wed Sep 03 2025 Alexander Burmatov <thatman@altlinux.org> 0.28.0-alt1
- New version 0.28.0.

* Fri Aug 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt2
- Built with Hypothesis supplied without numerous redundant dependencies.

* Wed Jul 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt1
- Updated to 0.24.0.

* Tue Jun 17 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.23.2-alt1
- Updated to 0.23.2.

* Wed Apr 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.23.0-alt1
- New version 0.23.0.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.17.1-alt1
- New version 0.17.1.

* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
