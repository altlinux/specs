%define _unpackaged_files_terminate_build 1
%define pypi_name flynt
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1
Summary: CLI tool to convert a python project's %-formatted strings to f-strings
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/flynt
Vcs: https://github.com/ikamensh/flynt
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
flynt is a command line tool to automatically convert a project's Python code
from old "%-formatted" and .format(...) strings into Python 3.6+'s "f-strings".

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%_bindir/flynt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 31 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
 - Initial build for Sisyphus.
