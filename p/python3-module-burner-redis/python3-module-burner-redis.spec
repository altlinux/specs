%define _unpackaged_files_terminate_build 1
%define pypi_name burner-redis
%define mod_name burner_redis

%def_with check

%python3_set_limited_api

Name: python3-module-%pypi_name
Version: 0.1.7
Release: alt1

Summary: An embedded, in-process Redis-compatible database
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/burner-redis/
Vcs: https://github.com/prefectlabs/burner-redis

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: liblua5.4
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
An embedded, in-process Redis-compatible database written in Rust with Python
bindings. Drop-in replacement for redis.asyncio.Redis that runs inside the host
process with no external server needed.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export LUB_LIB_NAME=lua-5.4
export LUA_LIB=%_libdir
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.7-alt1
- Packaged for ALT Sisyphus.
