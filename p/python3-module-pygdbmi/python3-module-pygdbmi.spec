%define _unpackaged_files_terminate_build 1
%define pypi_name pygdbmi

%def_with check

Name:    python3-module-%pypi_name
Version: 0.11.0.0
Release: alt1

Summary: A library to parse gdb mi output and interact with gdb subprocesses
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pygdbmi
VCS:     https://github.com/cs01/pygdbmi

BuildRequires(pre): rpm-build-pyproject
Requires: gdb

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
BuildRequires: gdb
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

%description
Python (py) gdb machine interface (mi).

GDB/MI is a line based machine oriented text interface to GDB and is
activated by specifying using the --interpreter command line option
(see Mode Options). It is specifically intended to support the
development of systems which use the debugger as just one small
component of a larger system.

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md docs/api
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Andrey Limachko <liannnix@altlinux.org> 0.11.0.0-alt1
- Initial build for Sisyphus
