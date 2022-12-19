%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq

# due to too new importlib-metadata in the repository
%def_without check

Name: python3-module-%pypi_name
Version: 0.1.4
Release: alt1

Summary: Distributed task queue with full async support 
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq
Vcs: https://github.com/taskiq-python/taskiq.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(poetry.core)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pydantic)
BuildRequires: python3(pycron)
BuildRequires: python3(watchdog)
BuildRequires: python3(importlib-metadata)
%endif

BuildArch: noarch

%description
Taskiq is an asynchronous distributed task queue for python. This
project takes inspiration from big projects such as Celery and Dramatiq.
But taskiq can send and run both the sync and async functions. Also, we
use PEP-612 to provide the best autosuggestions possible. But since it's
a new PEP, I encourage you to use taskiq with VS code because Pylance
understands all types correctly.

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
%doc README.md LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 19 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.3-alt1
- initial build for Sisyphus
