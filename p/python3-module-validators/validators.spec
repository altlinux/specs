%define _unpackaged_files_terminate_build 1
%define pypi_name validators
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.21.2
Release: alt1

Summary: Python data validation for Humans
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/validators/
Vcs: https://github.com/python-validators/validators
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 0.21.2-alt1
- 0.18.1 -> 0.21.2.

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.18.1-alt1
- Initial build for Sisyphus.
