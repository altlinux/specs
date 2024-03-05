%define _unpackaged_files_terminate_build 1
%define pypi_name xonsh
%def_with check

Name: python3-module-%pypi_name
Version: 0.15.0
Release: alt1

Summary: Python-powered, cross-platform, Unix-gazing shell
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/xonsh
Vcs: https://github.com/xonsh/xonsh
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# this patch is only needed by ALT, because python in our distribution means python2
Patch0: %pypi_name-%version-alt-fix-tests-python-to-python3.patch

# self-dependencies
%filter_from_requires /python3(xonsh.ply)/d
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra full
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
BuildRequires: git
BuildRequires: pip
BuildRequires: pytest3
BuildRequires: man-db
BuildRequires: bash-completion
BuildRequires: /dev/pts
BuildRequires: /proc
%endif

%description
Xonsh is a Python-powered, cross-platform, Unix-gazing shell language and command prompt.
The language is a superset of Python 3.6+ with additional shell primitives.
Xonsh (pronounced conch) is meant for the daily use of experts and novices alike.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m xonsh run-tests.xsh test -- \
    --timeout=240 -vvvra

%files
%_bindir/xonsh*
%python3_sitelibdir/xompletions/
%python3_sitelibdir/xontrib/
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 05 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.15.0-alt1
- First build for ALT.
