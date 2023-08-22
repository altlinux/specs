%define _unpackaged_files_terminate_build 1
%define pypi_name aiomysql

# tests require running mysql on 127.0.0.1, so they are disabled
%def_without check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: A library for accessing a MySQL database from the asyncio
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiomysql/
Vcs: https://github.com/aio-libs/aiomysql

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter setuptools-scm-git-archive
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
aiomysql is a "driver" for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends on and reuses most parts of PyMySQL.
aiomysql tries to be like awesome aiopg library and preserve same api,
look and feel.

Internally aiomysql is copy of PyMySQL, underlying io calls switched to async,
basically yield from and asyncio.coroutine added in proper places)).
sqlalchemy support ported from aiopg.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst LICENSE CHANGES.txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- initial build for Sisyphus
