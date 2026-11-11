%define _unpackaged_files_terminate_build 1
%define pypi_name inline-snapshot
%define mod_name inline_snapshot

%def_with check

Name: python3-module-%pypi_name
Version: 0.36.2
Release: alt1

Summary: Create and update inline snapshots in your python tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/inline-snapshot/
Vcs: https://github.com/15r10nk/inline-snapshot

BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-mypy
BuildRequires: python3-module-black
BuildRequires: python3-module-isort
%endif
%pyproject_configure_pypi_package

%description
%summary.

%pyproject_configure_pypi_subpackage black
%pyproject_configure_pypi_subpackage dirty-equals

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --session-timeout=600 -k "not pyright and not test_compare"

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.36.2-alt1
- Updated to 0.36.2.

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.36.1-alt1
- Updated to 0.36.1.

* Sun Oct 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.36.0-alt1
- Updated to 0.36.0.

* Fri Sep 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.35.4-alt1
- Updated to 0.35.4.

* Thu Aug 13 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.35.3-alt1
- NMU: updated to 0.35.3.

* Wed Jul 22 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.35.2-alt1
- NMU: updated to 0.35.2.

* Mon Jul 06 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.34.2-alt1
- NMU: updated to 0.34.2.

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
