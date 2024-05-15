%define _unpackaged_files_terminate_build 1
%define pypi_name rich-click
%define mod_name rich_click

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.2
Release: alt1
Summary: Format click help output nicely with rich
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich-click
Vcs: https://github.com/ewels/rich-click
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter rich-codex
%pyproject_builddeps_metadata_extra dev
%endif

%description
The intention of rich-click is to provide attractive help output from click,
formatted with rich, with minimal customisation required.

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
# .github/workflows/pytest.yml
# https://rich.readthedocs.io/en/latest/console.html?highlight=term#terminal-detection
# by default it's set to dumb in hasher
export TERM=xterm
%pyproject_run_pytest -ra

%files
%doc README.*
%_bindir/rich-click
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 1.8.2-alt1
- 1.8.1 -> 1.8.2.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.8.0 -> 1.8.1.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.4 -> 1.8.0.

* Tue Mar 12 2024 Stanislav Levin <slev@altlinux.org> 1.7.4-alt1
- 1.7.3 -> 1.7.4.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1
- 1.7.1 -> 1.7.3.

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 1.6.1 -> 1.7.1.

* Wed Oct 04 2023 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
