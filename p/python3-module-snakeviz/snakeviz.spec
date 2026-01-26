%define _unpackaged_files_terminate_build 1
%define pypi_name snakeviz
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.2
Release: alt1

Summary: A web-based viewer for Python profiler output
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/snakeviz/
Vcs: https://github.com/jiffyclub/snakeviz.git

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-requests
BuildRequires: python3-module-ipython
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
SnakeViz is a viewer for Python profiling data that runs as a web application
in your browser. It is inspired by the wxPython profile viewer RunSnakeRun.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE.txt
%_bindir/snakeviz
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 30 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
