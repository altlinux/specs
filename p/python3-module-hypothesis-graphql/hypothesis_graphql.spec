%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-graphql
%define mod_name hypothesis_graphql

%def_with check

Name: python3-module-%pypi_name
Version: 0.12.0
Release: alt1

Summary: Hypothesis strategies for GraphQL queries
License: MIT
Group: Development/Python3
Url: https://github.com/Stranger6667/hypothesis-graphql
Vcs: https://github.com/Stranger6667/hypothesis-graphql.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
It is a Python library that provides a set of Hypothesis strategies
that let you write tests parametrized by a source of examples.
Generated queries have arbitrary depth and may contain any subset of
GraphQL types defined in the input schema.
They expose edge cases in your code that are unlikely to be found otherwise.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_corpus_negative"

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 10 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.12.0-alt1
- New version (0.12.0).
- Updated dependencies management.

* Mon Sep 30 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.11.1-alt1
  - Initial build for ALT.
