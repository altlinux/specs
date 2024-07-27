%define pypi_name django-radius

%def_without check

Name: python3-module-%pypi_name
Version: 1.5.1
Release: alt1

Summary: A RADIUS authentication backend for Django
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/django-radius

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/radiusauth/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus.
