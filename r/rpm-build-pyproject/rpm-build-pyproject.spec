%define _unpackaged_files_terminate_build 1
# https://github.com/stanislavlevin/pyproject_installer/issues/179
%define pyproject_installer_ver 0.6.1

%def_with check

Name: rpm-build-pyproject
Version: 0.3.0
Release: alt1
Summary: Extra RPM macros for packaging Python projects
License: GPL-2.0-or-later
Group: Development/Other
Url: https://altlinux.space/slev/rpm-build-pyproject
Vcs: https://altlinux.space/slev/rpm-build-pyproject.git
BuildArch: noarch
Source: %name-%version.tar

%if_with check
BuildRequires: rpm-build-python3
BuildRequires: python3-module-pyproject-installer >= %pyproject_installer_ver
# build and check real Python extensions
BuildRequires: gcc
BuildRequires: python3-dev
BuildRequires: python3-module-abi3audit
%endif

# run command
Requires: rpm-build-python3 >= 0.1.21-alt1
Requires: rpm-macros-pyproject = %EVR

%description
%summary.

%package -n rpm-macros-pyproject
Summary: Extra RPM macros for packaging Python projects
Group: Development/Other
BuildArch: noarch
Conflicts: %name < %version
Requires: python3-module-pyproject-installer >= %pyproject_installer_ver

%description -n rpm-macros-pyproject
%summary.

%prep
%setup

%install
install -pD -m0644 macros/pyproject -t %buildroot%_rpmmacrosdir/
install -pD -m0644 macros/pyproject.env -t %buildroot%_rpmmacrosdir/
install -pD -m0644 macros/pyproject-legacy -t %buildroot%_rpmmacrosdir/
install -pD -m0755 scripts/pyproject.req -t %buildroot%_rpmlibdir/
install -pD -m0755 scripts/pyproject.req.files -t %buildroot%_rpmlibdir/
install -pD -m0755 user_scripts/pyproject_deps.py %buildroot%_bindir/pyproject-deps

%check
PYPROJECT_USE_SYSTEM_DEPS=1 tools/run_tests.sh

%files -n rpm-macros-pyproject
%_rpmmacrosdir/pyproject
%_rpmmacrosdir/pyproject.env
%_rpmmacrosdir/pyproject-legacy

%files
%doc README.md docs/deps.md
%_bindir/pyproject-deps
%_rpmlibdir/pyproject.req
%_rpmlibdir/pyproject.req.files

%changelog
* Mon Oct 26 2026 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.3 -> 0.3.0

* Thu Feb 12 2026 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1
- Filtered coherent.licensed from build dependencies (closes: #57827).

* Wed Dec 10 2025 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- Added support for configuration of setuptools-rust (closes: #57197).

* Tue Nov 18 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.2.1-alt1
- Extended typing stubs filter to include *-stubs pattern (closes: #56895).

* Tue Oct 21 2025 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- Added support for Python Stable ABI (closes: #56201).
- Fixed support for extensions having multiple init functions.

* Tue Oct 14 2025 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1
- Readded support for alt-specific dependency on Python ABI.

* Tue Sep 16 2025 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt1
- Reverted previous change for building python3.13.

* Mon Aug 04 2025 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1
- Added support for alt-specific dependency on Python ABI (closes: #55340).

* Thu Nov 14 2024 Stanislav Levin <slev@altlinux.org> 0.0.9-alt1
- Added support for dependency groups (PEP735).
- Allowed gradual migration to updated PEP518 specification.

* Tue Oct 01 2024 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1
- Introduced %%pyproject_runtimedeps_metadata_extra.

* Thu Aug 22 2024 Stanislav Levin <slev@altlinux.org> 0.0.7-alt1
- Allow to disable verify mode on syncing deps.

* Tue Jul 02 2024 Stanislav Levin <slev@altlinux.org> 0.0.6-alt1
- Added support for migration to setuptools 70.1.0.

* Fri Apr 12 2024 Stanislav Levin <slev@altlinux.org> 0.0.5-alt1
- Added support for pipenv deps.

* Fri Jun 02 2023 Stanislav Levin <slev@altlinux.org> 0.0.4-alt1
- Added support for hatch and pdm deps.

* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1
- Added %%pyproject_scm_init.

* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1
- Added %%pyproject_deps_config_name.
- Added more default exclusions of check dependencies.

* Mon Mar 20 2023 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Added support for external source of upstream dependencies.
