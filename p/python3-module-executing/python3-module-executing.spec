%define _unpackaged_files_terminate_build 1
%define pypi_name executing
%define mod_name %pypi_name

%def_with check

Name: python3-module-executing
Version: 2.0.1
Release: alt2
Summary: Get the currently executing AST node of a frame, and other information
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/executing/
Vcs: https://github.com/alexmojaki/executing
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: .gear/executing-2.0.1-python3.12.5-fix.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
This mini-package lets you get information about
what a frame is currently doing, particularly the AST node being executed.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 29 2024 Anton Vyatkin <toni@altlinux.org> 2.0.1-alt2
- Fixed FTBFS.

* Thu Jan 25 2024 Anton Vyatkin <toni@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Wed Apr 26 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 0.8.2 -> 1.2.0.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt1
- Initial build for ALT.
