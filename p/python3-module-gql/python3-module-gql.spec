%define _unpackaged_files_terminate_build 1
%define module_name gql
%def_without check

Name: python3-module-%module_name
Version: 3.5.0
Release: alt1
Summary: A GraphQL client in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/gql
VCS: https://github.com/graphql-python/gql

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3(anyio)
BuildRequires: python3(backoff)
BuildRequires: python3(graphql)
BuildRequires: python3(parse)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_asyncio)
BuildRequires: python3(mock)
BuildRequires: python3(yarl)
%endif

%description
This is a GraphQL client for Python 3.7+. Plays nicely with graphene,
graphql-core, graphql-js and any other GraphQL implementation
compatible with the spec.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/gql-cli
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%doc LICENSE

%changelog
* Sun Dec 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.0-alt1
- Initial build for ALT.
