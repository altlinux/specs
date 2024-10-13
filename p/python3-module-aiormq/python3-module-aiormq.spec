%define _unpackaged_files_terminate_build 1
%define pypi_name aiormq
%define mod_name %pypi_name

# tests require running amql broker
%def_without check

Name: python3-module-%pypi_name
Version: 6.8.1
Release: alt1

Summary: Pure python AMQP 0.9.1 asynchronous client library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiormq/
Vcs: https://github.com/mosquito/aiormq

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter collective-checkdocs
%add_pyproject_deps_check_filter coveralls
%add_pyproject_deps_check_filter pytest-rst
%add_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc COPYING README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 6.8.1-alt1
- Updated to 6.8.1.

* Wed Feb 07 2024 Anton Zhukharev <ancieg@altlinux.org> 6.8.0-alt1
- Updated to 6.8.0.

* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 6.7.7-alt1
- Updated to 6.7.7.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 6.7.4-alt1
- Initial build for ALT Sisyphus.

