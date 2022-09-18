%define _unpackaged_files_terminate_build 1
%define pypi_name pydantic

%def_with check

Name: python3-module-%pypi_name
Version: 1.10.2
Release: alt2

Summary: Data parsing and validation using Python type hints
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(cython)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(mypy)
BuildRequires: python3(hypothesis)
BuildRequires: python3(email)
BuildRequires: python3(email_validator)
BuildRequires: python3(dotenv)
BuildRequires: python3(devtools)
%endif

%description
Data validation and settings management using Python type hints.

Fast and extensible, pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.7+; validate it
with pydantic.

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
%doc *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.2-alt2
- build with Cython
- update description
- use modern %%pyproject macros
- reformat and clean up spec

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus.
