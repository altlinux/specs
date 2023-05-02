%define _unpackaged_files_terminate_build 1
%define pypi_name devtools

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt2

Summary: Dev tools for python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devtools

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(executing)
BuildRequires: python3(asttokens)
BuildRequires: python3(numpy)
BuildRequires: python3(multidict)
BuildRequires: python3(asyncpg)
BuildRequires: python3(sqlalchemy)
BuildRequires: python3(pygments)
%endif

BuildArch: noarch

%description
Python's missing debug print command and other development tools.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# Ignore SQLAlchemy deprecation warnings until the package been updated.
%pyproject_run_pytest -W ignore::sqlalchemy.exc.MovedIn20Warning

%files
%doc README.md HISTORY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue May 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt2
- Temporary ignore SQLAlchemy's deprecation warning.
- Don't package LICENSE file.

* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus

