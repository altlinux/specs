%define _unpackaged_files_terminate_build 1
%define pypi_name schemathesis
%define mod_name schemathesis

# unstable testsuite, randomly fails out of the blue
%def_without check

Name: python3-module-%pypi_name
Version: 4.21.7
Release: alt1

Summary: Property-based testing framework for Open API and GraphQL based apps
License: MIT
Group: Development/Python3
Url: https://schemathesis.readthedocs.io
VCS: https://github.com/schemathesis/schemathesis.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

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
%pyproject_run_pytest \
--snapshot-update \
-n auto \
-k "not test_stateful_auth \
and not test_stateful_seed \
and not test_responses_in_another_file \
and not test_hooks_combination \
and not test_stateful_all_generation_modes \
and not test_request_body_with_boolean_true_schema \
and not test_find_use_after_free_via_state_machine \
and not test_check_header_errors \
and not test_multipart_examples_serialization \
and not test_multiple_hooks_per_spec \
and not test_multiple_hops_references_swagger" \
test/

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/schemathesis
%_bindir/st

%changelog
* Tue Jun 16 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.21.7-alt1
- New version (4.21.7).

* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.21.0-alt1
- New version (4.21.0).

* Wed Apr 15 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.15.2-alt1
- New version (4.15.2).

* Tue Mar 24 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.13.0-alt1
- New version (4.13.0).

* Tue Mar 17 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.12.1-alt1
- New version (4.12.1).

* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.11.2-alt1
- New version (4.11.2).

* Tue Mar 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.11.0-alt1
- New version (4.11.0).

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
