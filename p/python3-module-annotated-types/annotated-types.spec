%define _unpackaged_files_terminate_build 1
%define mod_name annotated_types
%define pypi_name annotated-types

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: Reusable constraint types to use with typing.Annotated
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/annotated-types
Vcs: https://github.com/annotated-types/annotated-types

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter coverage
%pyproject_builddeps_check
%endif

%description
PEP-593 added typing.Annotated as a way of adding context-specific
metadata to existing types, and specifies that Annotated[T, x] should
be treated as T by any tool or library without special logic for x.

This package provides metadata objects which can be used to represent
common constraints such as upper and lower bounds on scalar values and
collection sizes, a Predicate marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some
cases, we also note alternative representations which do not require
this package.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/testing.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0.

* Wed Feb 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0

* Thu Aug 10 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

