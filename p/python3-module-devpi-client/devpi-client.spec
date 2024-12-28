%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-client
%define mod_name devpi

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.0
Release: alt1
Summary: Manage devpi-server, Python packaging and testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-client
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter setuptools-changelog-shortener
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-github-actions-annotate-failures
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# filtered by default but needed: command not found: sphinx-build
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pip
# testing/conftest.py::initproj
BuildRequires: python3-module-flit-core
%endif

%description
The devpi command line tool is typically used in conjunction with devpi-server.
It allows to upload, test and install packages from devpi indexes.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# symlink server plugins as it's made in upstream
ln -sf -t testing/ \
    %python3_sitelibdir/test_devpi_server/{functional,reqmock,simpypi}.py

%pyproject_run_pytest -ra

%files
%doc README.*
%_bindir/devpi
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- Initial build for Sisyphus.
