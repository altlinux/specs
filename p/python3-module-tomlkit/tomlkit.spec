%define _unpackaged_files_terminate_build 1
%define pypi_name tomlkit

%def_with check

Name: python3-module-%pypi_name
Version: 0.12.5
Release: alt1
Summary: Style preserving TOML library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tomlkit
VCS: https://github.com/sdispater/tomlkit.git
BuildArch: noarch
Source: %name-%version.tar
Source1: toml-test.tar
Source2: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter furo
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
TOML Kit is a 1.0.0-compliant TOML library. It includes a parser that preserves
all comments, indentations, whitespace and internal element ordering, and makes
them accessible and editable via an intuitive API. You can also create new TOML
documents from scratch using the provided helpers.

%prep
%setup -a1
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
%pyproject_run_pytest -ra tests

%files
%doc README.md
%python3_sitelibdir/tomlkit/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 0.12.5-alt1
- 0.12.4 -> 0.12.5.

* Tue Feb 27 2024 Stanislav Levin <slev@altlinux.org> 0.12.4-alt1
- 0.12.3 -> 0.12.4.

* Wed Nov 15 2023 Stanislav Levin <slev@altlinux.org> 0.12.3-alt1
- 0.12.2 -> 0.12.3.

* Fri Nov 03 2023 Stanislav Levin <slev@altlinux.org> 0.12.2-alt1
- 0.12.1 -> 0.12.2.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.12.0 -> 0.12.1.

* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.8 -> 0.12.0.

* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 0.11.8-alt1
- 0.11.7 -> 0.11.8.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 0.11.7-alt1
- 0.11.6 -> 0.11.7.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 0.11.6-alt1
- 0.11.5 -> 0.11.6.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.11.5-alt1
- 0.11.4 -> 0.11.5.

* Sat Aug 13 2022 Stanislav Levin <slev@altlinux.org> 0.11.4-alt1
- 0.10.1 -> 0.11.4.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.2 -> 0.10.0.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2.

* Mon Feb 07 2022 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
