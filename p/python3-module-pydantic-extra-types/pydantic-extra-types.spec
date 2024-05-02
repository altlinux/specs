%define _unpackaged_files_terminate_build 1
%def_with check

%define mod_name pydantic_extra_types
%define pypi_name pydantic-extra-types

Name: python3-module-%pypi_name
Version: 2.7.0
Release: alt1

Summary: Extra Pydantic types
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic-extra-types/
Vcs: https://github.com/pydantic/pydantic-extra-types

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata -- --extra all
%pyproject_builddeps_check
%endif

%description
A place for pydantic types that probably shouldn't exist in the main
pydantic lib.
See https://github.com/pydantic/pydantic/issues/5012 for more info.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Skip tests/test_pendulum_dt.py because pytzdata is broken in Sisyphus.
# See https://bugzilla.altlinux.org/50266
%pyproject_run_pytest --ignore="tests/test_pendulum_dt.py"

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 02 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Initial build for ALT Sisyphus.

