%define _unpackaged_files_terminate_build 1
%def_with check

%define pypi_name pydantic

Name: python3-module-%pypi_name
Version: 2.8.2
Release: alt1

Summary: Data parsing and validation using Python type hints
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic
Vcs: https://github.com/pydantic/pydantic

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter eval-type-backport
%add_pyproject_deps_check_filter pytest-codspeed
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra email
%pyproject_builddeps_check
%endif

# Manually manage extras dependencies with metadata.
AutoReq: yes, nopython3

%description
Data validation and settings management using Python type hints.

Fast and extensible, pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.7+; validate it
with pydantic.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pdm testing
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_docs.py: skip testing of documentation
#
# --benchmark-skip:
# Skip executing tests from tests/benchmark. These tests don't have sense for
# our check section, because of they test only pydantic work speed.
# Also generating north_star_data.json at each test exec and comparing it with
# expected md5sum leads to failed build, because of Faker or something else has
# been updated.
%pyproject_run_pytest -Wignore --ignore='tests/test_docs.py' --benchmark-skip

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 12 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.8.2-alt1
- 2.8.0 -> 2.8.2.

* Wed Jul 03 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.8.0-alt1
- 2.7.3 -> 2.8.0.

* Thu Jun 06 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.3-alt1
- 2.7.2 -> 2.7.3.

* Wed May 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2.

* Tue Apr 23 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.1-alt1
- 2.7.0 -> 2.7.1.

* Sun Apr 21 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- 2.6.4 -> 2.7.0.

* Thu Mar 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.4-alt1
- 2.6.3 -> 2.6.4

* Mon Mar 04 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.3-alt1
- 2.6.1 -> 2.6.3

* Mon Feb 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.1-alt1
- 2.5.3 -> 2.6.1

* Sat Jan 20 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.3-alt1
- 2.5.2 -> 2.5.3

* Thu Nov 23 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.2-alt1
- 2.4.2 -> 2.5.2

* Wed Nov 08 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.2-alt3
- Fixed FTBFS: skip benchmark tests with their often changed expected md5sum of
  testing data

* Sun Oct 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.2-alt2
- Fixed FTBFS: delete workaround for mismatching of EXPECTED_NORTH_STAR_DATA_MD5
  because of updating Faker to 19.11.0

* Fri Sep 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.2-alt1
- 2.3.0 -> 2.4.2

* Thu Aug 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.0-alt1
- 2.1.1 -> 2.3.0

* Tue Aug 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.1.1-alt1
- 1.10.7 -> 2.1.1
- built with tests
- used rpm-build-pyproject

* Thu Mar 23 2023 Grigory Ustinov <grenka@altlinux.org> 1.10.7-alt1
- Automatically updated to 1.10.7.

* Thu Mar 09 2023 Grigory Ustinov <grenka@altlinux.org> 1.10.6-alt1
- Automatically updated to 1.10.6.

* Thu Feb 16 2023 Grigory Ustinov <grenka@altlinux.org> 1.10.5-alt1
- Automatically updated to 1.10.5.

* Wed Jan 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.10.4-alt1
- Automatically updated to 1.10.4 (Closes: #44879).
- Build without check.

* Sun Sep 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt4
- Build with Cython.
- Update description.
- Use modern %%pyproject macros.
- Add extra BuildRequires for tests.
- Great thanks for ancieg@.

* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.2-alt3
- rollback to 1.10.2-alt1 state

* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.2-alt2
- build with Cython
- update description
- use modern %%pyproject macros
- reformat and clean up spec

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus.
