%define _unpackaged_files_terminate_build 1
%define pypi_name lupa

%def_with check

Name: python3-module-%pypi_name
Version: 1.14.1
Release: alt1.1

Summary: Integrates the runtimes of Lua or LuaJIT2 into CPython
License: MIT
Group: Development/Python3
# Source-git: https://github.com/scoder/lupa.git
Url: https://pypi.org/project/lupa/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

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

%build
%ifarch ppc64le riscv64
%define build_lua_args --backend-config-settings='{"--build-option": ["--no-luajit"]}'
%endif

%pyproject_build %{?build_lua_args}

%install
%pyproject_install

%check
# override upstream config to avoid patching
cat > tox.ini <<'EOF'
[testenv]
allowlist_externals = bash
commands =
    bash -c 'cd lupa/tests && python -m unittest {posargs:}'
EOF
%tox_check_pyproject

%files
%doc README.rst CHANGES.rst LICENSE.txt
%python3_sitelibdir/lupa/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 18 2022 Ivan A. Melnikov <iv@altlinux.org> 1.14.1-alt1.1
- fix build on riscv64

* Thu Nov 17 2022 Stanislav Levin <slev@altlinux.org> 1.14.1-alt1
- 1.9 -> 1.14.1.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.9-alt1
- Initial build for Sisyphus.
