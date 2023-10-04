%define _unpackaged_files_terminate_build 1
%define pypi_name rich
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 13.6.0
Release: alt1
Summary: Render rich text and beautiful formatting in the terminal
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich/
Vcs: https://github.com/Textualize/rich
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# asv is not yet packaged
%add_pyproject_deps_check_filter asv
%pyproject_builddeps_check
# missing dependency: tests/test_syntax.py::pkg_resources
BuildRequires: python3-module-setuptools
%endif

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more - out of the box.

%prep
%setup
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
%pyproject_run_pytest tests -ra

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 02 2023 Stanislav Levin <slev@altlinux.org> 13.6.0-alt1
- 12.5.1 -> 13.6.0.

* Fri Sep 23 2022 Danil Shein <dshein@altlinux.org> 12.5.1-alt1
- NMU: new version 12.5.1

* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- Initial build.
