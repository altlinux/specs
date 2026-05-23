%define _unpackaged_files_terminate_build 1
%define pypi_name pydantic-settings
%define mod_name pydantic_settings
%def_with check

Name: python3-module-%pypi_name
Version: 2.14.1
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
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
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
%pyproject_deps_resync_check_depgroup testing
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_docs.py: do not execute docs tests
# tests/test_source_azure_key_vault.py: there's error with new
# python3-module-azure-keyvault-secrets==4.9.0 and we don't need to check
# azure functional.
# tests/test_source_gcp_secret_manager.py: there's no sense testing
# google-cloud-secret-manager since that package is no in Sisyphus
%pyproject_run_pytest \
    --ignore='tests/test_docs.py' \
    --ignore='tests/test_source_azure_key_vault.py' \
    --ignore='tests/test_source_gcp_secret_manager.py'

%files
%doc README.md LICENSE docs
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 20 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.14.1-alt1
- NMU: updated to 2.14.1.

* Tue Apr 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.14.0-alt1
- Updated to 2.14.0.

* Tue Mar 03 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Fri Nov 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.12.0-alt1
- Updated to 2.12.0.

* Thu Sep 25 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.11.0-alt1
- Updated to 2.11.0.

* Thu Jun 26 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.1-alt1
- Updated to 2.10.1.

* Sat Apr 19 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.1-alt1
- Updated to 2.9.1.

* Thu Feb 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.8.1-alt1
- Updated to 2.8.1.

* Mon Feb 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.1-alt1
- Updated to 2.7.1.

* Fri Dec 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Fri Nov 01 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.1-alt1
- Updated to 2.6.1.

* Fri Oct 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0.

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

