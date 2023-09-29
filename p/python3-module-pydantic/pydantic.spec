%define _unpackaged_files_terminate_build 1
%def_with check

%define  pypi_name pydantic

Name: python3-module-%pypi_name
Version: 2.4.2
Release: alt1

Summary: Data parsing and validation using Python type hints
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pydantic
Vcs: https://github.com/pydantic/pydantic

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra email
%pyproject_builddeps_check
%endif

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
# It seems error with new Faker 19.6.2-alt1. See https://github.com/pydantic/pydantic/issues/7607
# Replace digest temporary for passing the tests.
sed -i -E "s/(_EXPECTED_NORTH_STAR_DATA_MD5 =) .+/\1 'e0fb021af00010f90e9348d8c7fc8da4'/" tests/benchmarks/test_north_star.py
# tests/test_docs.py: skip testing of documentation
%pyproject_run_pytest -vra --ignore='tests/test_docs.py'

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
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
