%define _unpackaged_files_terminate_build 1
%define pypi_name exceptiongroup

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: Backport of PEP 654 (exception groups)
License: MIT
Group: Development/Python3
VCS: https://github.com/agronholm/exceptiongroup
Url: https://pypi.org/project/exceptiongroup
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
Backport of PEP 654 (exception groups)

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
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 07 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.3 -> 1.2.0.

* Tue Aug 15 2023 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2.

* Thu Jun 15 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt3
- Fixed FTBFS (Python 3.11.0).

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt2
- Rebuilt with flit-core 3.9.0.

* Thu Apr 20 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.1.0 -> 1.1.1.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.4 -> 1.1.0.

* Wed Nov 16 2022 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 1.0.1 -> 1.0.4.

* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
