%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.context
%define ns_name jaraco
%define mod_name context

%def_with check

Name: python3-module-%pypi_name
Version: 6.1.1
Release: alt1
Summary: Context managers by Jaraco
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.context/
VCS: https://github.com/jaraco/jaraco.context.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
# requires internet
%add_pyproject_deps_build_filter coherent-licensed
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%pypi_name provides context managers by Jaraco.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra \
    --deselect='%ns_name/%mod_name/__init__.py::jaraco.context.repo_context'

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1.0 -> 6.1.1.

* Fri Feb 06 2026 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1
- 6.0.2 -> 6.1.0 (fixes: CVE-2026-23949).

* Thu Dec 25 2025 Stanislav Levin <slev@altlinux.org> 6.0.2-alt1
- 6.0.1 -> 6.0.2.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 5.3.0 -> 6.0.1.

* Mon Apr 08 2024 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 5.1.0 -> 5.3.0.

* Fri Apr 05 2024 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 4.3.0 -> 5.1.0.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 4.3.0-alt2
- Mapped PyPI name to distro's one.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1
- 4.2.0 -> 4.3.0.

* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1
- 4.1.2 -> 4.2.0.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 4.1.2-alt1
- 4.1.1 -> 4.1.2.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 4.0.0 -> 4.1.1.

* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
