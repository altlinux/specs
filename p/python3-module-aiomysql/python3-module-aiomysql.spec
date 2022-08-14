%define _unpackaged_files_terminate_build 1
%define pypi_name aiomysql

# tests require running mysql on 127.0.0.1, so they are disabled
%def_without check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: A library for accessing a MySQL database from the asyncio
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aimysql

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)
BuildRequires: python3(pymysql)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(uvloop)
BuildRequires: python3(sqlalchemy)
%endif

BuildArch: noarch

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
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst LICENSE CHANGES.txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- initial build for Sisyphus
