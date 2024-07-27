%define pypi_name django-crum

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.9
Release: alt1

Summary: Django middleware to capture current request and user
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/ninemoreminutes/django-crum

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Django CRUM (Current Request User Middleware) captures the current request
and user in thread local storage.

%prep
%setup -n %pypi_name-%version

sed -i '/addopts/d' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/crum
%python3_sitelibdir/django_crum-%version.dev0.dist-info

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 0.7.9-alt1
- Initial build for Sisyphus
