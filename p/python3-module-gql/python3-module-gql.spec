%define _unpackaged_files_terminate_build 1
%define module_name gql
%def_with check

Name: python3-module-%module_name
Version: 4.0.0
Release: alt2
Summary: A GraphQL client in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/gql
VCS: https://github.com/graphql-python/gql

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-anyio
BuildRequires: python3-module-backoff
BuildRequires: python3-module-botocore
BuildRequires: python3-module-graphql-core
BuildRequires: python3-module-mock
BuildRequires: python3-module-parse
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-console-scripts
BuildRequires: python3-module-requests
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-vcrpy
BuildRequires: python3-module-websockets
BuildRequires: python3-module-yarl
BuildRequires: python3-module-httpx
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
* Thu Dec 04 2025 Stanislav Levin <slev@altlinux.org> 4.0.0-alt2
- NMU: fixed FTBFS (vcrpy 8.0.0).

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.0.0-alt1
- Updated to version 4.0.0.

* Mon Dec 23 2024 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.0-alt2
- Fixed BuildRequires.

* Sun Dec 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.0-alt1
- Initial build for ALT.
