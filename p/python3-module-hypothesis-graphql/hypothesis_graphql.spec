%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-graphql
%define mod_name hypothesis_graphql

%def_with check

Name:    python3-module-%pypi_name
Version: 0.11.1
Release: alt1

Summary:   Hypothesis strategies for GraphQL queries
License:   MIT
Group:     Development/Python3
Url:       https://github.com/Stranger6667/hypothesis-graphql
Vcs:       https://github.com/Stranger6667/hypothesis-graphql.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-graphql-core
BuildRequires: python3-module-hypothesis
%endif

%description
It is a Python library that provides a set of Hypothesis strategies
that let you write tests parametrized by a source of examples.
Generated queries have arbitrary depth and may contain any subset of
GraphQL types defined in the input schema.
They expose edge cases in your code that are unlikely to be found otherwise.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 30 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.11.1-alt1
  - Initial build for ALT.
