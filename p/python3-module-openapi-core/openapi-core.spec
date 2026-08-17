%define _unpackaged_files_terminate_build 1
%define pypi_name openapi-core
%define mod_name openapi_core

%def_with check

Name: python3-module-%pypi_name
Version: 0.23.1
Release: alt1
Summary: Client-side and server-side support for the OpenAPI Specification v3
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/openapi-core/
Vcs: https://github.com/python-openapi/openapi-core
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not yet packaged
%add_pyproject_deps_check_filter tbump
%pyproject_builddeps_metadata_extra flask
%pyproject_builddeps_check
%endif

%description
Openapi-core is a Python library that provides client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 and OpenAPI v3.2 specifications.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts='' tests/unit/

%files
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Aug 17 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.23.1-alt1
- NMU: New version (0.23.1).

* Tue Dec 23 2025 Anton Vyatkin <toni@altlinux.org> 0.22.0-alt1
- New version 0.22.0.

* Tue Dec 16 2025 Anton Vyatkin <toni@altlinux.org> 0.20.0-alt1
- New version 0.20.0.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 0.19.5-alt1.1
- NMU: fixed FTBFS (removed jsonschema-spec).

* Fri Mar 21 2025 Anton Vyatkin <toni@altlinux.org> 0.19.5-alt1
- New version 0.19.5.

* Thu Oct 10 2024 Anton Vyatkin <toni@altlinux.org> 0.19.4-alt1
- New version 0.19.4.

* Mon Mar 11 2024 Anton Vyatkin <toni@altlinux.org> 0.18.2-alt2
- Fixed FTBFS.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 0.18.2-alt1
- New version 0.18.2.

* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 0.18.1-alt1
- New version 0.18.1.

* Tue Aug 29 2023 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt3
- Fix FTBFS.

* Mon Aug 07 2023 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt2
- Fix FTBFS.

* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt1
- New version 0.18.0.

* Mon Jun 19 2023 Anton Vyatkin <toni@altlinux.org> 0.17.2-alt1
- Initial build for Sisyphus
