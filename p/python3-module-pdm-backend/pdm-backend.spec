%define _unpackaged_files_terminate_build 1
%define pypi_name pdm-backend
%def_without vendored

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.1
Release: alt1

Summary: The build backend used by PDM that supports latest packaging standards
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdm-backend/
VCS: https://github.com/pdm-project/pdm-backend
BuildArch: noarch
Source: %name-%version.tar
%if_without vendored
Source1: debundler.py.in
%endif
Source2: pyproject_deps.json
Patch: %name-%version-alt.patch
# manage deps with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
# namespace root
%py3_requires pdm

%if_without vendored
%pyproject_runtimedeps -- vendored
%endif

%if_with vendored
# self-contained deps
%add_findprov_skiplist %python3_sitelibdir/pdm/backend/_vendor/*
%endif

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_without vendored
%pyproject_builddeps -- vendored
%endif

%if_with check
%pyproject_builddeps_metadata
# not packaged yet
%add_pyproject_deps_check_filter vendoring
%pyproject_builddeps -- pdm_test --exclude %pyproject_deps_check_filter
%pyproject_builddeps -- pdm_dev --exclude %pyproject_deps_check_filter
# required by tests/pdm/backend/hooks/version/test_scm.py
BuildRequires: /usr/bin/git
BuildRequires: /usr/bin/hg
%endif

%description
This is the backend for PDM projects that is fully-compatible with PEP 517 spec,
but you can also use it alone. It reads the metadata of PEP 621 format and
coverts it to Core metadata.

%prep
%setup
%autopatch -p1

%if_without vendored
%pyproject_deps_resync vendored pip_reqfile src/pdm/backend/_vendor/vendor.txt

# unbundle packages
VENDORED_PATH='src/pdm/backend/_vendor'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"pdm.backend._vendor"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"
%endif

%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync pdm_test pdm test
%pyproject_deps_resync pdm_dev pdm dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc README.md
%python3_sitelibdir/pdm/backend/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 19 2024 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.3.0 -> 2.3.1.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.1 -> 2.3.0.

* Thu Apr 18 2024 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.2.0 -> 2.2.1.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.8 -> 2.2.0.

* Mon Feb 19 2024 Stanislav Levin <slev@altlinux.org> 2.1.8-alt1
- 2.1.7 -> 2.1.8.

* Fri Oct 27 2023 Stanislav Levin <slev@altlinux.org> 2.1.7-alt1
- 2.1.6 -> 2.1.7.

* Wed Sep 27 2023 Stanislav Levin <slev@altlinux.org> 2.1.6-alt1
- 2.1.5 -> 2.1.6.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 2.1.5-alt1
- 2.1.4 -> 2.1.5.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1
- 2.1.0 -> 2.1.4.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.7 -> 2.1.0.

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 2.0.7-alt1
- 2.0.6 -> 2.0.7.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 2.0.6-alt1
- 2.0.5 -> 2.0.6.

* Tue Mar 28 2023 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- NMU:
  + fix build --without check
  + minor spec cleanup

* Tue Feb 28 2023 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.3 -> 2.0.5.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.1.2 -> 2.0.2.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.6 -> 1.1.1.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.5 -> 1.0.6.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.4 -> 1.0.5.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus.
