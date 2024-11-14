%define pypi_name django-qr-code
%define mod_name qr_code

%def_with check

Name:    python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: An application that provides tools for displaying QR codes on your Django site
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/dprog-philippe-docourt/django-qr-code

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-django
BuildRequires: python3-module-segno
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
python3 manage.py test

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 08 2024 Alexander Burmatov <thatman@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus.
