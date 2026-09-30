%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-redis-sdk
%define mod_name redis_fastapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
Summary: FastAPI SDK for Redis

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-redis-sdk/
Vcs: https://github.com/redis/fastapi-redis-sdk.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch1: fastapi-redis-sdk-v0.8.1-skip-tests-if-fakeredis-missing-lua-scripting.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The official Redis integration with FastAPI.

%prep
%setup
%autopatch -p1
# Upstream updates the version only when publishing to PyPI, not in the Git tag.
sed -i 's/^version = "0.1.0"$/version = "%version"/' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 25 2026 Yaroslav Bahtin <alpacost@altlinux.org> 0.8.1-alt1
- Initial build
