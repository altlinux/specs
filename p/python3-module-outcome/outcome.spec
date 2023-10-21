%define _unpackaged_files_terminate_build 1
%define modulename outcome

%def_with check

Name: python3-module-%modulename
Version: 1.3.0
Release: alt1
Summary: Capture the outcome of Python function calls
License: MIT or Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/outcome/
Vcs: https://github.com/python-trio/outcome
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Capture the outcome of Python function calls. Extracted from the Trio project.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Modernized packaging.
- Fixed FTBFS (pytest 7.3.1).

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.
- Build with check.

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
