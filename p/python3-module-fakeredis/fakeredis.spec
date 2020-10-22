%define _unpackaged_files_terminate_build 1
%define oname fakeredis

%def_with check

Name: python3-module-%oname
Version: 1.4.3
Release: alt1

Summary: A fake version of a redis-py
License: BSD
Group: Development/Python3
# Source-git: https://github.com/jamesls/fakeredis.git
Url: https://pypi.org/project/fakeredis/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(aioredis)
BuildRequires: python3(async_generator)
BuildRequires: python3(hypothesis)
BuildRequires: python3(lupa)
BuildRequires: python3(redis)
BuildRequires: python3(six)
BuildRequires: python3(sortedcontainers)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
fakeredis is a pure-Python implementation of the redis-py python client that
simulates talking to a redis server. This was created for a single purpose: to
write unittests. Setting up redis is not hard, but many times you want to write
unittests that do not talk to an external server (such as redis). This module
now allows tests to simply use this module as a reasonable substitute for
redis.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc README.rst COPYING
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus.
