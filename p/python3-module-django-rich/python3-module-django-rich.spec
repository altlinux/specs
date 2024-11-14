%define pypi_name django-rich
%define mod_name django_rich

%def_with check

Name:    python3-module-%pypi_name
Version: 1.13.0
Release: alt1

Summary: Extensions for using Rich with Django
License: MIT
Group:   Development/Python3
URL:     https://github.com/adamchainz/django-rich

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-rich
BuildRequires: python3-module-django
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus.
