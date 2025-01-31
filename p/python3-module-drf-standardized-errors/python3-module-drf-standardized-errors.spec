%define _unpackaged_files_terminate_build 1

%define pypi_name drf-standardized-errors
%define mod_name drf_standardized_errors

%def_with check

Name: python3-module-%pypi_name
Version: 0.14.1
Release: alt1

Summary: Standardize your DRF API error responses.
License: MIT
Group: Development/Python3
Url: https://github.com/ghazi-git/drf-standardized-errors.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-drf-spectacular
BuildRequires: python3-module-django-filter
BuildRequires: python3-module-flit
%endif

%description
This package is a DRF exception handler, so it standardizes errors that
reach a DRF API view. That means it cannot handle errors that happen at
the middleware level for example. To handle those as well, you can customize
the necessary django error views.

%prep
%setup
sed -i 's|ip.error_codes == {"invalid", "null_characters_not_allowed"}|ip.error_codes == {"max_length", "invalid", "null_characters_not_allowed"}|g' tests/test_openapi_utils.py

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%python3_sitelibdir/%mod_name-%version/docs

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jan 31 2025 Alexander Burmatov <thatman@altlinux.org> 0.14.1-alt1
- Update version to 0.14.1.

* Mon Aug 05 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.14.0-alt1
- Initial build for ALT Linux

