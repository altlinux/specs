%define pypi_name social-app-django

%def_with check

Name:    python3-module-%pypi_name
Version: 5.8.0
Release: alt1

Summary: Python Social Auth - Application - Django
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/python-social-auth/social-app-django

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-social-core
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

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
%doc *.md
%python3_sitelibdir/social_django/
%python3_sitelibdir/%{pyproject_distinfo social_auth_app_django}

%changelog
* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 5.8.0-alt1
- New version 5.8.0.

* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 5.7.0-alt1
- New version 5.7.0.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 5.6.0-alt1
- New version 5.6.0.

* Mon Jul 28 2025 Alexander Burmatov <thatman@altlinux.org> 5.5.1-alt1
- New version 5.5.1.

* Fri Mar 14 2025 Alexander Burmatov <thatman@altlinux.org> 5.4.3-alt1
- New version 5.4.3.

* Tue Oct 03 2023 Alexander Burmatov <thatman@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
