%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-describe
%define mod_name pytest_describe

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Describe-style plugin for the pytest framework
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-describe/
Vcs: https://github.com/pytest-dev/pytest-describe

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
pytest-describe is a plugin for pytest that allows tests to be written
in arbitrary nested describe-blocks, similar to RSpec (Ruby) and
Jasmine (JavaScript).

%prep
%setup
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
%pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Sisyphus.
