%define pypi_name django-pglocks

# Need PostgreSQL for run tests
%def_without check

Name:    python3-module-%pypi_name
Version: 1.0.4
Release: alt1

Summary: PostgreSQL locking context managers and functions for Django
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/django-pglocks/

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.txt
%python3_sitelibdir/django_pglocks/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus.
