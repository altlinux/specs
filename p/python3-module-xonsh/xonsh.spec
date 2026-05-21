%define _unpackaged_files_terminate_build 1
%define pypi_name xonsh
%def_with check

Name: python3-module-%pypi_name
Version: 0.23.7
Release: alt1.14.g2791ce61

Summary: Python-powered, cross-platform, Unix-gazing shell
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/xonsh
Vcs: https://github.com/xonsh/xonsh
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

# self-dependencies
%filter_from_requires /python3(xonsh.ply)/d
%pyproject_runtimedeps_metadata
Provides: %pypi_name = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra full
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
BuildRequires: git
BuildRequires: pip
BuildRequires: pytest3
BuildRequires: man-db
BuildRequires: bash-completion
BuildRequires: /dev/pts
BuildRequires: /proc
%endif

%description
Xonsh is a Python-powered, cross-platform, Unix-gazing shell language and command prompt.
The language is a superset of Python 3.6+ with additional shell primitives.
Xonsh (pronounced conch) is meant for the daily use of experts and novices alike.

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
# --reruns: this is necessary to avoid flaky tests failed with raise condition.
# Link: https://github.com/xonsh/xonsh/issues/6456
%pyproject_run_pytest -vvvra --timeout=240 --reruns 2

%files
%_bindir/xonsh*
%python3_sitelibdir/xompletions/
%python3_sitelibdir/xontrib/
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 20 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.23.7-alt1.14.g2791ce61
- New version.

* Tue Apr 21 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.23.0-alt1
- New version.

* Fri Mar 27 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.22.8-alt1
- New version.

* Thu Feb 26 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.22.4-alt1
- New version.

* Mon Jan 19 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.22.1-alt1
- New version.

* Sun Dec 21 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.22.0-alt1
- New version.

* Mon Nov 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.20.0-alt1
- New version.

* Thu Jun 26 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.9-alt1
- New version.

* Fri Mar 28 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.4-alt1
- New version.

* Mon Mar 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.3-alt1
- New version.

* Sat Feb 15 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.2-alt1
- New version.

* Wed Jan 15 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.1-alt1
- New version.

* Wed Dec 11 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.19.0-alt1
- New version.

* Sat Nov 23 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.18.4-alt1
- New version.

* Wed Aug 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.18.3-alt1
- New version.

* Fri Jul 19 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.18.2-alt1
- New version.

* Fri Jun 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.17.0-alt1
- New version.

* Wed Apr 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.16.0-alt1
- New version.
- Provide pypi name.
- Fix FTBFS: xfail for test_virtualenv_activator.

* Fri Mar 22 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.15.1-alt1
- New version.

* Tue Mar 05 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.15.0-alt1
- First build for ALT.
