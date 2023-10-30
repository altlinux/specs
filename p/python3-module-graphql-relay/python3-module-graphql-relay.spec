%define pypi_name graphql-relay
%define mod_name  graphql_relay

%def_without check

Name:    python3-module-%pypi_name
Version: 3.2.0
Release: alt1

Summary: A library to help construct a graphql-py server supporting react-relay
License: MIT
Group:   Development/Python3
URL:     https://github.com/graphql-python/graphql-relay-py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-graphql-core
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
GraphQL-relay-py is the Relay library for GraphQL-core.
It allows the easy creation of Relay-compliant servers using GraphQL-core.
GraphQL-Relay-Py is a Python port of graphql-relay-js, while GraphQL-Core
is a Python port of GraphQL.js, the reference implementation of GraphQL
for JavaScript.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 05 2023 Alexander Burmatov <thatman@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.
