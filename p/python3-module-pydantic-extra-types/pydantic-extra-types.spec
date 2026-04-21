%define _unpackaged_files_terminate_build 1
%def_with check

%define module_name pydantic_extra_types
%define pypi_name pydantic-extra-types

Name: python3-module-%pypi_name
Version: 2.11.2
Release: alt2

Summary: Extra Pydantic types
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic-extra-types/
Vcs: https://github.com/pydantic/pydantic-extra-types

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

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
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Skip pendulum-related tests due to broken pytzdata in Sisyphus
# and missing pendulum 3.x dependency (Interval class unavailable in pendulum 2.x).
# See https://bugzilla.altlinux.org/50266
# See https://bugzilla.altlinux.org/58620
%pyproject_run_pytest \
    --ignore="tests/test_pendulum_dt.py" \
    --ignore="tests/test_json_schema.py" \
    -Wignore::DeprecationWarning

%files
%doc LICENSE README.*
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 21 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.11.2-alt2
- Fixed FTBFS: adjusted test_json_schema() for Pydantic 2.13.

* Wed Apr 15 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.11.2-alt1
- Updated to 2.11.2.

* Wed Mar 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.11.1-alt1
- Updated to 2.11.1.

* Mon Dec 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.11.0-alt1
- Updated to 2.11.0.

* Sat Dec 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.6-alt1
- Updated to 2.10.6.

* Mon Jun 09 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.5-alt1
- Updated to 2.10.5.

* Fri Apr 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.3-alt1
- Updated to 2.10.3.

* Thu Jan 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.2-alt1
- Updated to 2.10.2.

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.1-alt1
- Updated to 2.10.1.

* Fri Oct 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.

* Fri Oct 11 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.0-alt2
- Fixed FTBFS: adjusted test_json_schema() for Pydantic 2.9.

* Mon Aug 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.0-alt1
- Updated to 2.9.0.

* Fri Jun 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.8.2-alt1
- 2.7.0 -> 2.8.2.

* Thu May 02 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Initial build for ALT Sisyphus.

