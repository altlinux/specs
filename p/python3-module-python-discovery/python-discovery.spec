%define _unpackaged_files_terminate_build 1
%define pypi_name python-discovery
%define mod_name python_discovery

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.3
Release: alt1
Summary: Python interpreter discovery
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-discovery
Vcs: https://github.com/tox-dev/python-discovery
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
%pyproject_builddeps_metadata_extra testing
%endif

%description
%summary.

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
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 06 2026 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.4.2 -> 1.4.3

* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.4.0 -> 1.4.2

* Thu May 28 2026 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1.

* Thu May 07 2026 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.2 -> 1.3.0.

* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2.

* Fri Mar 27 2026 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Thu Mar 19 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.3 -> 1.2.0.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.0 -> 1.1.3.

* Fri Mar 06 2026 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for sisyphus.
