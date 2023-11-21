%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-order
%define mod_name pytest_order

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: pytest plugin that allows to customize the test execution order
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-order/
Vcs: https://github.com/pytest-dev/pytest-order

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest-mock
%endif

%description
pytest-order is a pytest plugin that allows you to customize the order
in which your tests are run. It uses the marker order that defines
when a specific test shall run, either by using an ordinal number,
or by specifying the relationship to other tests.

pytest-order is a fork of pytest-ordering that provides additional
features like ordering relative to other tests.

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
%pyproject_run_pytest -vra

%files
%doc LICENSE AUTHORS CHANGELOG.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- Built for ALT Sisyphus.

