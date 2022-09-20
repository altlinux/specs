%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name cachy

%def_disable check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Simple yet effective caching Python library
License: ISC
Group: Development/Python3
Url: https://github.com/sdispater/cachy

%if_disabled snapshot
Source: https://github.com/sdispater/cachy/archive/%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/sdispater/cachy.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

# optional dependencies
Requires: python3(redis)
#Requires: python3(memcached)
Requires: python3(msgpack)

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(flexmock)
BuildRequires: python3(fakeredis)
BuildRequires: /usr/bin/poetry}

%description
Cachy provides a simple yet effective Python caching library.

%prep
%setup -n %pypi_name-%version
cat << EOF >> pyproject.toml

[build-system]
requires = ["poetry-core~=1.0"]
build-backend = "poetry.core.masonry.api"
EOF

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3
#%%tox_check

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README* CHANGELOG*

%changelog
* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus



