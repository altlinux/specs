%define _unpackaged_files_terminate_build 1
%define oname aioredis

%def_with check

Name: python3-module-%oname
Version: 1.3.1
Release: alt1

Summary: asyncio (PEP 3156) Redis client library
License: MIT
Group: Development/Python3
# Source-git: https://github.com/aio-libs/aioredis.git
Url: https://pypi.org/project/aioredis/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: redis
BuildRequires: python3(async_timeout)
BuildRequires: python3(hiredis)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
asyncio (PEP 3156) Redis client library.
The library is intended to provide simple and clear interface to Redis based on
asyncio.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
whitelist_externals =
    /bin/cp
    /bin/sed
commands_pre =
    /bin/cp %_bindir/py.test3 {envbindir}/py.test
    /bin/sed -i '1c #!{envpython}' {envbindir}/py.test
commands =
    {envbindir}/py.test {posargs:-vra}
EOF

export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3

%ifarch armh
# https://github.com/redis/redis/issues/7935
export REDIS_7935=yes
export TOX_TESTENV_PASSENV='REDIS_7935'
%endif

tox.py3 --sitepackages -vvr

%files
%doc README.rst CHANGES.txt LICENSE
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
