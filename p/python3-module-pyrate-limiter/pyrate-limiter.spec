%define _unpackaged_files_terminate_build 1
%define pypi_name pyrate-limiter
%define mod_name pyrate_limiter

%def_with check

Name: python3-module-%pypi_name
Version: 4.4.0
Release: alt1

Summary: The request rate limiter using Leaky-bucket Algorithm
License: MIT
Group: Development/Python3
Url: https://github.com/vutran1710/PyrateLimiter
Vcs: https://github.com/vutran1710/PyrateLimiter.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-modules-sqlite3
%add_pyproject_deps_check_filter nox-poetry
%add_pyproject_deps_check_filter redis
# psycopg requires optional psycopg[pool] dependencies
%add_pyproject_deps_check_filter psycopg
%pyproject_builddeps_metadata
%pyproject_builddeps -- check_all %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%pyproject_builddeps -- check_dev %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init v%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check_all pep735 all
%pyproject_deps_resync check_dev pep735 dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra --ignore=tests/test_multiprocessing.py

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 16 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.4.0-alt1
- New version (4.4.0).

* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.2.0-alt1
- New version (4.2.0).

* Tue Mar 24 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.1.0-alt1
- New version (4.1.0).

* Tue Mar 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.0.2-alt1
- New version (4.0.2).

* Tue Jul 29 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.8.1-alt1
- New version (3.8.1).

* Mon Jun 02 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.7.1-alt1
- New version (3.7.1).

* Tue Oct 01 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 3.7.0-alt1
  - Initial build for ALT.
