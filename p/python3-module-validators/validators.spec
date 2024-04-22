%define _unpackaged_files_terminate_build 1
%define pypi_name validators
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.28.1
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
%add_pyproject_deps_check_filter pypandoc-binary
%add_pyproject_deps_check_filter pyright
%pyproject_builddeps_metadata
%pyproject_builddeps_check
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
%if_with check
%pyproject_deps_resync_check_pdm tooling
%endif

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
* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 0.28.1-alt1
- 0.28.0 -> 0.28.1.

* Thu Apr 04 2024 Stanislav Levin <slev@altlinux.org> 0.28.0-alt1
- 0.27.0 -> 0.28.0.

* Wed Apr 03 2024 Stanislav Levin <slev@altlinux.org> 0.27.0-alt1
- 0.24.0 -> 0.27.0.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 0.24.0-alt1
- 0.23.2 -> 0.24.0.

* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 0.23.2-alt1
- 0.23.0 -> 0.23.2.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.23.0-alt1
- 0.22.0 -> 0.23.0.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 0.22.0-alt1
- 0.21.2 -> 0.22.0.

* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 0.21.2-alt1
- 0.18.1 -> 0.21.2.

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.18.1-alt1
- Initial build for Sisyphus.
