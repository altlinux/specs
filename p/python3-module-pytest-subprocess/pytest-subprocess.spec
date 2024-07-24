%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-subprocess
%define mod_name pytest_subprocess

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.1
Release: alt1
Summary: A plugin to fake subprocess for pytest
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-subprocess
Vcs: https://github.com/aklajnert/pytest-subprocess
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
The plugin adds the fake_process fixture (and fp as an alias). It can be used it
to register subprocess results so you won't need to rely on the real processes.
The plugin hooks on the subprocess.Popen(), which is the base for other
subprocess functions. That makes the subprocess.run(), subprocess.call(),
subprocess.check_call() and subprocess.check_output() methods also functional.

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.
