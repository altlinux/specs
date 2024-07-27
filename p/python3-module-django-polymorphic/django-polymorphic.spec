%define _unpackaged_files_terminate_build 1
%define pypi_name django-polymorphic

%def_without check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1
Summary: Seamless polymorphic inheritance for Django models
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-polymorphic
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Django-polymorphic simplifies using inherited models in Django projects.
When a query is made at the base model, the inherited model classes are returned.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/polymorphic
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 23 2024 Anton Vyatkin <toni@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus.
