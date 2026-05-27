%define pypi_name django-oauth-toolkit
%define mod_name oauth2_provider

%def_with check

Name:    python3-module-%pypi_name
Version: 3.2.0
Release: alt1

Summary: OAuth2 goodies for the Djangonauts
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/jazzband/django-oauth-toolkit

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django
BuildRequires: python3-module-jwcrypto
BuildRequires: python3-module-oauthlib
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-requests
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
export DJANGO_SETTINGS_MODULE=tests.settings
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 28 2026 Anton Vyatkin <toni@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Tue May 13 2025 Alexander Burmatov <thatman@altlinux.org> 3.0.1-alt1
- Update version to 3.0.1.

* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
