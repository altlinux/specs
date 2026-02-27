%define _unpackaged_files_terminate_build 1
%define pypi_name schemathesis

# unstable testsuite, randomly fails out of the blue
%def_without check

Name: python3-module-%pypi_name
Version: 4.7.6
Release: alt2

Summary: Property-based testing framework for Open API and GraphQL based apps
License: MIT
Group: Development/Python3
Url: https://schemathesis.readthedocs.io
VCS: https://github.com/schemathesis/schemathesis.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
# backported from a49aad8ecbf219b29feb45878e6c21c20318c5fe
Patch0: schemathesis-4.7.6-chore-Ditch-pytest-subtests.patch
# backported from b13d26060ff581a9ccc24a4bdb92b13b7b60dc46
Patch1: schemathesis-4.7.6-hypothesis-6.149.0.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
BuildRequires: python3-module-aiohttp-tests
BuildRequires: curl
#Added because the package jsonschema is built in the repository without optional dependencies.
BuildRequires: python3-module-rfc3339-validator
BuildRequires: python3-module-fqdn
BuildRequires: python3-module-idna
%endif

%description
Schemathesis is an API testing tool that automatically
finds crashes and validates spec compliance.

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
%pyproject_run_pytest --snapshot-update test/ -n auto

%files
%doc LICENSE README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/%pypi_name
%_bindir/st

%changelog
* Wed Feb 25 2026 Stanislav Levin <slev@altlinux.org> 4.7.6-alt2
- NMU: fixed FTBFS (pytest 9).

* Fri Dec 19 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.7.6-alt1
- New version (4.7.6).

* Wed Nov 05 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.3.18-alt1
- New version (4.3.18).

* Thu Sep 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.1.4-alt1
- New version (4.1.4).

* Thu Jul 31 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.0.15-alt1
- New version (4.0.15).

* Mon Jul 14 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.0.9-alt1
- New version (4.0.9).

* Mon Jun 30 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.0.3-alt1
- New version (4.0.3).

* Wed Jun 11 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.0.0-alt1
- New version(4.0.0).

* Fri Apr 25 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.16-alt1
- New version 3.39.16.
- Updated dependencies managment.

* Mon Feb 03 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.9-alt1
  - New version 3.39.9

* Mon Jan 27 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.8-alt1
  - New version 3.39.8

* Fri Jan 17 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.7-alt1
  - New version 3.39.7
  - Fix missing runtime dependencies

* Thu Jan 09 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.5-alt1
  - Initial build for ALT.
