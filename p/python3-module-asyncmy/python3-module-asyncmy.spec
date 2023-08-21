%define _unpackaged_files_terminate_build 1
%define pypi_name asyncmy

# tests require running mysqld, so they are disabled
%def_without check

Name: python3-module-%pypi_name
Version: 0.2.8
Release: alt1

Summary: A fast asyncio MySQL/MariaDB driver with replication protocol support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/asyncmy

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(cython)
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
%endif

%description
asyncmy is a fast asyncio MySQL/MariaDB driver, which reuse most of pymysql
and aiomysql but rewrite core protocol with cython to speedup.

%prep
%setup

%build
%pyproject_build --backend-config-settings='{"user-option": ["--inline"]}'

%install
%pyproject_install

# remove wrong-installed docs
rm %buildroot%python3_sitelibdir/{README.md,CHANGELOG.md,LICENSE}

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md LICENSE CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 15 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.2.8-alt1
- Updated to upstream 0.2.8

* Thu Mar 02 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt3
- Fixed build with python3.11.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 0.2.5-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sun Aug 14 2022 Anton Zhukharev <ancieg@altlinux.org> 0.2.5-alt1
- initial build for Sisyphus
