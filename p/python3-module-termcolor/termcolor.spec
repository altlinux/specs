%define _unpackaged_files_terminate_build 1
%define pypi_name termcolor
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1
Summary: ANSI color formatting for output in terminal
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/termcolor/
Vcs: https://github.com/termcolor/termcolor
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
%summary.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export TERM=xterm
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 28 2023 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 1.1.0 -> 2.3.0.

* Wed Jul 14 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt2.git20130510
- Build python3 module only

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130510
- Initial build for Sisyphus
