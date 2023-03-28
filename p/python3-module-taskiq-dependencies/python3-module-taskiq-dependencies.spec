%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-dependencies

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt1

Summary: FastAPI-like dependency injection implementation
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/taskiq-dependencies
Vcs: https://github.com/taskiq-python/taskiq.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(poetry.core)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
This project is used to add FastAPI-like dependency injection to
projects.

This project is a part of the taskiq, but it doesn't have any
dependencies, and you can easily integrate it in any project.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/taskiq_dependencies/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt1
- New version.

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
