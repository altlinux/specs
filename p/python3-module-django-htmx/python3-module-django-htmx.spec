%define pypi_name django-htmx
%define mod_name django_htmx

%def_with check

Name:    python3-module-%pypi_name
Version: 1.18.0
Release: alt1

Summary: Extensions for using Django with htmx
License: MIT
Group:   Development/Python3
URL:     https://github.com/adamchainz/django-htmx

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
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
* Tue Jul 16 2024 Alexander Burmatov <thatman@altlinux.org> 1.18.0-alt1
- Initial build for Sisyphus.
