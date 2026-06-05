%define _unpackaged_files_terminate_build 1
%define pypi_name sqlfluff
%define mod_name sqlfluff
%def_with check

Name: python3-module-%pypi_name
Version: 4.2.2
Release: alt1

Summary: The SQL Linter for Humans

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sqlfluff/
VCS: https://github.com/sqlfluff/sqlfluff

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter import-linter
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%description
SQLFluff is an open source, dialect-flexible and configurable SQL linter.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# deselect some tests due to incorect plugin registration
%pyproject_run_pytest -n auto -vra test \
    --deselect='test/core/plugin_test.py::test__plugin_default_config_read[Example_L001-forbidden_columns]' \
    --deselect='test/core/plugin_test.py::test__plugin_example_rules_returned[Rule_Example_L001]' \
    --deselect='test/core/plugin_test.py::test__plugin_manager_registers_example_plugin'

%files
%doc LICENSE* *.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 05 2026 Anton Vyatkin <toni@altlinux.org> 4.2.2-alt1
- New version 4.2.2.

* Fri May 15 2026 Anton Vyatkin <toni@altlinux.org> 4.2.1-alt1
- New version 4.2.1.

* Wed May 13 2026 Anton Vyatkin <toni@altlinux.org> 4.1.0-alt1
- New version 4.1.0.

* Tue Jul 15 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.2-alt1
- Update to 3.4.2.

* Tue Jun 17 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.1-alt1
- Update to 3.4.1.

* Tue May 13 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.0-alt1
- Update to 3.4.0.

* Tue Feb 11 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.3.1-alt1
- Initial Build for Sisyphus.
