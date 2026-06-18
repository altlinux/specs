%define _unpackaged_files_terminate_build 1

%define pypi_name allure-python-commons
%define mod_name allure_commons
%define pkg_version 2.16.0

%define test_pypi_name allure-python-commons-test
%define test_mod_name allure_commons_test

%define pytest_pypi_name allure-pytest
%define pytest_mod_name allure_pytest

%def_with check

Name: python3-module-%pypi_name
Version: %pkg_version
Release: alt1
Summary: Contains the API for end users as well as helper functions and classes to build Allure adapters for Python test frameworks
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/allure-python-commons/
Vcs: https://github.com/allure-framework/allure-python.git
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- allure_commons_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps -- allure_commons_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- allure_commons_test_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- allure_pytest_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}

%if_with check
%pyproject_builddeps -- allure_commons_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- allure_commons_test_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- allure_pytest_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- check %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%endif

%package -n python3-module-allure-python-commons-test
Version: %pkg_version
Summary: A collection of PyHamcrest matchers to test Allure adapters for Python test frameworks
Group: Development/Python3
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- allure_commons_test_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%package -n python3-module-allure-pytest
Version: %pkg_version
Summary: Allure pytest integration
Group: Development/Python3
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- allure_pytest_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description
Simple. Fun. Language and Framework agnostic. Designed to create fancy and clear testing reports in minutes.
Loved by the community, developed by Qameta Software & Open-source contributors.

%description -n python3-module-allure-python-commons-test
A collection of PyHamcrest matchers to test Allure adapters for Python test frameworks.

%description -n python3-module-allure-pytest
Allure integration for pytest framework.

%prep
%setup
%pyproject_scm_init %pkg_version
%autopatch -p1

cd allure-python-commons
%pyproject_deps_resync allure_commons_pep518 pep518
%pyproject_deps_resync allure_commons_pep517 pep517
%pyproject_deps_resync allure_commons_metadata metadata
cd -

cd allure-python-commons-test
%pyproject_deps_resync allure_commons_test_pep518 pep518
%pyproject_deps_resync allure_commons_test_pep517 pep517
%pyproject_deps_resync allure_commons_test_metadata metadata
cd -

cd allure-pytest
%pyproject_deps_resync allure_pytest_pep518 pep518
%pyproject_deps_resync allure_pytest_pep517 pep517
%pyproject_deps_resync allure_pytest_metadata metadata
cd -

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/testing.txt
%endif

%build
for package in allure-python-commons allure-python-commons-test allure-pytest; do
    pushd $package
    %pyproject_build
    popd
done

%install
for package in allure-python-commons allure-python-commons-test allure-pytest; do
    pushd $package
    %pyproject_install
    popd
done

%check
export PYTHONPATH=%buildroot%python3_sitelibdir:$PYTHONPATH
python3 -m pytest -vra tests/allure_pytest/ \
    --ignore=tests/allure_pytest/externals/ \
    -k "not test_duration and not test_with_fixture_duration"

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/allure/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-allure-python-commons-test
%doc allure-python-commons-test/README.*
%python3_sitelibdir/%test_mod_name/
%python3_sitelibdir/%{pyproject_distinfo %test_pypi_name}/

%files -n python3-module-allure-pytest
%doc allure-pytest/README.*
%python3_sitelibdir/%pytest_mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pytest_pypi_name}/

%changelog
* Mon Jun 08 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 2.16.0-alt1
- New version (2.16.0).

* Thu Apr 09 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 2.15.3-alt1
- Initial build for ALT.
