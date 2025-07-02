%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-memray
%def_with check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: Pytest-memray is a pytest plugin for easy integration of memray
License: Apache-2.0
Group: Development/Python3
Url: https://pytest-memray.readthedocs.io
Vcs: https://github.com/bloomberg/pytest-memray.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-anyio
BuildRequires: python3-module-flaky
BuildRequires: python3-module-pytest-xdist
BuildRequires: /proc
BuildRequires: /dev/kvm
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Professional-grade memory analysis toolkit for Python developers.  Tracks
Python and native allocations, detects leaks, enforces memory limits, and
generates detailed reports. Essential for developing memory-efficient
applications and system components.

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/bloomberg/pytest-memray/issues/145
%pyproject_run -- %make check \
  PYTEST_ARGS="-p pytest_memray -p anyio \
  --ignore=tests/test_pytest_memray.py" \
  #

%files
%python3_sitelibdir_noarch/pytest_memray/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jun 29 2025 Ivan Khanas <xeno@altlinux.org> 1.7.0-alt1
- First build for ALT.
