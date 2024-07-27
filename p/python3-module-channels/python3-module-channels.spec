%define pypi_name channels

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: Developer-friendly asynchrony for Django
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/channels
VCS: https://github.com/django/channels

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-daphne
BuildRequires: python3-module-async-timeout
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
