%define _unpackaged_files_terminate_build 1
%define pypi_name lupa

%def_with check

Name: python3-module-%pypi_name
Version: 2.0
Release: alt2
Summary: Python wrapper around Lua and LuaJIT
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lupa/
Vcs: https://github.com/scoder/lupa
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-cython
%if_with check
%pyproject_builddeps_metadata
%endif
%ifarch ppc64le riscv64
# luajit doesn't officially support ppc64le and riscv64
BuildRequires: liblua-devel
%else
BuildRequires: libluajit-devel
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

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%global build_lua_args "--no-bundle","--with-cython"
%ifarch ppc64le riscv64
%global build_lua_args %build_lua_args,"--no-luajit"
%endif
%global backend_args --backend-config-settings='{"--build-option": [%build_lua_args]}'

%pyproject_build %backend_args

%install
%pyproject_install

%check
# upstream relies on deprecated setuptools' test command
# arch-dependent package and in-tree unittest tests
%pyproject_run -- bash -s <<-'ENDUNITTEST'
set -eu
LUPA_VENV_PATH="$(python -I -c 'import lupa;print(lupa.__path__[0])')"
ln -sfr ./lupa/tests "$LUPA_VENV_PATH/"
cd lupa
python3 -m unittest
ENDUNITTEST

%files
%doc README.rst CHANGES.rst
%python3_sitelibdir/lupa/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 07 2023 Stanislav Levin <slev@altlinux.org> 2.0-alt2
- Backported fix for build against Cython 3.0.

* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 2.0-alt1
- 1.14.1 -> 2.0.

* Fri Nov 18 2022 Ivan A. Melnikov <iv@altlinux.org> 1.14.1-alt1.1
- fix build on riscv64

* Thu Nov 17 2022 Stanislav Levin <slev@altlinux.org> 1.14.1-alt1
- 1.9 -> 1.14.1.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.9-alt1
- Initial build for Sisyphus.
