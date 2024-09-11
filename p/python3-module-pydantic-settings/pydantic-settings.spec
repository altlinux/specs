%define _unpackaged_files_terminate_build 1

%define pypi_name pydantic-settings
%define mod_name pydantic_settings

%def_with check

Name: python3-module-%pypi_name
Version: 2.5.2
Release: alt1

Summary: Settings management using pydantic
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic-settings/
Vcs: https://github.com/pydantic/pydantic-settings

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pytest-examples
%add_pyproject_deps_check_filter typed-ast
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%description
Settings management using Pydantic, this is the new official home of
Pydantic's BaseSettings.
This package was kindly donated to the https://github.com/pydanticby
Daniel Daniels, see https://github.com/pydantic/pydantic/pull/4492
for discussion.

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
# tests/test_docs.py: do not execute docs tests
%pyproject_run_pytest --ignore='tests/test_docs.py'

%files
%doc README.md docs
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 11 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.2-alt1
- Updated to 2.5.2.

* Tue Sep 10 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.

* Mon Aug 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Fri Jun 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.4-alt1
- 2.3.1 -> 2.3.4.

* Thu Jun 06 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.1-alt1
- 2.2.1 -> 2.3.1.

* Mon Mar 04 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.2.1-alt1
- 2.1.0 -> 2.2.1

* Fri Nov 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.1.0-alt1
- 2.0.3 -> 2.1.0

* Fri Aug 18 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3

* Tue Aug 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus

