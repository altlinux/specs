%define _unpackaged_files_terminate_build 1
%define pypi_name fakeredis
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.12.1
Release: alt1
Summary: Fake implementation of redis API for testing purposes
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/fakeredis/
Vcs: https://github.com/cunla/fakeredis-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter tox-docker
%add_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata_extra lua
%pyproject_builddeps_metadata_extra json
%pyproject_builddeps_check
%endif

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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -m fake -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 2.12.1-alt1
- 1.4.3 -> 2.12.1.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus.
