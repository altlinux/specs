%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-dependencies
%define mod_name taskiq_dependencies

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: FastAPI-like dependency injection implementation
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/taskiq-dependencies/
Vcs: https://github.com/taskiq-python/taskiq-dependencies

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter types-
%add_pyproject_deps_check_filter wemake-python-styleguide
%add_pyproject_deps_check_filter yesqa
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This project is used to add FastAPI-like dependency injection to
projects.

This project is a part of the taskiq, but it doesn't have any
dependencies, and you can easily integrate it in any project.

%prep
%setup
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
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 22 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Tue Aug 08 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Wed Jun 14 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.3-alt1
- New version.

* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- New version.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt2
- Updated BR for %%check.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt1
- New version.

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
