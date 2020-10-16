%define _unpackaged_files_terminate_build 1
%define oname lupa

%def_with check

Name: python3-module-%oname
Version: 1.9
Release: alt1

Summary: Integrates the runtimes of Lua or LuaJIT2 into CPython
License: MIT
Group: Development/Python3
# Source-git: https://github.com/scoder/lupa.git
Url: https://pypi.org/project/lupa/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%ifarch ppc64le
# luajit doesn't officially support ppc64le
BuildRequires: liblua-devel
%else
BuildRequires: libluajit-devel
%endif

BuildRequires: python3-module-Cython

%if_with check
BuildRequires: python3(tox)
%endif

%description
Lupa integrates the runtimes of Lua or LuaJIT2 into CPython. It is a partial
rewrite of LunaticPython in Cython with some additional features such as proper
coroutine support.

%prep
%setup
%autopatch -p1

# unbundle
rm -r ./third-party/*

%build
%ifarch ppc64le
export PY_LUA_ARGS=--no-luajit
%endif

%python3_build $PY_LUA_ARGS

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -- -v

%files
%doc README.rst CHANGES.rst LICENSE.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.9-alt1
- Initial build for Sisyphus.
